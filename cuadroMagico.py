############################################################
#Identificacion          : cuadroMagico.py
#Version                 : 1.00
#Instalacion             : Python 2.7 Requerido
#Fecha de Entrega        : Septiempre-2014
 
###########################################################

import itertools
import sys
import time

######################################
#  Declaracion de Variables Globales #
######################################
tamanioCuadroMagico=0
numeroSoluciones=0
numeroMagico=0
tamanioMaximo=0
debugEnable = False
numeroTotaldeCuadros=0
######################################


############################################################################
#Nom de la funcion       : imprimirCuadro 
#Version                 : 1.00 
#Descripcion             : Imprime un cuadro 
#Autor                   : HGT 
#
#Documentacion Params    : 
#
#Tipo          Nombre                          Descripcion 
#=========     ======================          ============================= 
# Arreglo      cuadrado                        Arreglo bidimensional 
############################################################################

def imprimirCuadro(cuadrado):
	print("--------> imprimirCuadro")
	for i in range(tamanioCuadroMagico):
		for j in range(tamanioCuadroMagico):
			print cuadrado[i][j],
		print " "
	print("<------- imprimirCuadro")

############################################################################
#Nom de la funcion       : verificarCuadroMagico 
#Version                 : 1.00 
#Descripcion             : Verifica si un cuadro es magico
#Autor                   : HGT 
#
#Documentacion Params    : 
#
#Tipo          Nombre                          Descripcion 
#=========     ======================          ============================= 
# Arreglo      cuadrado                        Arreglo bidimensional 
############################################################################

def verificarCuadroMagico(cuadrado):
	if(debugEnable):
		print("-----> verificarCuadroMagico")
	sumaPorColumna=0
	sumaPorFila=0
	sumaDiagonal1=0
	sumaDiagonal2=0
	isCuadroMagico = True 
	for i in range(tamanioCuadroMagico):
		sumaPorColumna=0
		sumaPorFila=0
		for j in range(tamanioCuadroMagico):
			sumaPorColumna=sumaPorColumna + cuadrado[i][j]
			sumaPorFila=sumaPorFila + cuadrado[j][i]
		sumaDiagonal1 = sumaDiagonal1 + cuadrado[i][i]
		sumaDiagonal2 = sumaDiagonal2 + cuadrado[(tamanioCuadroMagico-1)-i][i]
		

		if (sumaPorColumna != numeroMagico) or (sumaPorFila != numeroMagico) :
			isCuadroMagico=False


	if (sumaDiagonal1!=numeroMagico) or (sumaDiagonal2!=numeroMagico):
		isCuadroMagico=False
	
	if(debugEnable):
		print("<------- %d"%isCuadroMagico)

	return isCuadroMagico


############################################################################
#Nom de la funcion       : verificaFilaMagica 
#Version                 : 1.00 
#Descripcion             : Verifica una fila con el numero magico
#Autor                   : HGT 
#
#Documentacion Params    : 
#
#Tipo          Nombre                          Descripcion 
#=========     ======================          ============================= 
# Arreglo      cuadrado                        Arreglo bidimensional
# Integer      numFila 						   Numero de fila a verificar 
############################################################################
def verificaFilaMagica(cuadrado,numFila):
	sumaPorFila=0
	isFilaMagica = True 
	for i in range(tamanioCuadroMagico):
		sumaPorFila= sumaPorFila + cuadrado[numFila-1][i]

	if (sumaPorFila!=numeroMagico):
		isFilaMagica=False

	return isFilaMagica

############################################################################
#Nom de la funcion       : construirCandidatos 
#Version                 : 1.00 
#Descripcion             : Construye una lista de posibles candidatos 
# 						   dado un cuadrado y no repetir numeros
#Autor                   : HGT 
#
#Documentacion Params    : 
#
#Tipo          Nombre                          Descripcion 
#=========     ======================          ============================= 
# Arreglo      cuadrado                        Arreglo bidimensional
# Integer      numFila 						   Numero de fila a verificar 
############################################################################

def construirCandidatos(cuadrado,numero):
	noDisponiblesList = [0 for x in xrange(tamanioMaximo+1)]
	candidatosList = [0 for x in xrange(tamanioMaximo)]
	alternateList = []
	listaFinal    = []
	posx=(numero/tamanioCuadroMagico)
	posy=(numero%tamanioCuadroMagico)
	#print("X =%d"%posx)
	#print("Y = %d"%posy)
	columnasFaltantes=tamanioCuadroMagico-posy
	#print("columnasFaltantes %d"%columnasFaltantes)
	sumaActual=cuadrado[posx][0]
	#print ("sumaActual %d"%cuadrado[posx][0])



	for i in range(tamanioCuadroMagico):
		for j in range(tamanioCuadroMagico):
			if(cuadrado[i][j]!=0):
				noDisponiblesList[cuadrado[i][j]] = 1

	#if(debugEnable):
	#	print noDisponiblesList

	for i in range(tamanioMaximo+1):
		if(noDisponiblesList[i] != 1) and (i!=0):
			candidatosList[i-1]= i
			alternateList.append(i)

		
		#if((x[0] + x[1]+sumaActual)<numeroMagico):
		#	print x
		#	if((x[0] in alternateList)):
		#		alternateList.remove(x[0])
				
	return alternateList


#################################################################################
#Nom de la funcion       : backTrack 
#Version                 : 1.00 
#Descripcion             : Metodo que realiza el backtrack, construye
#						   soluciones parciales de manera recursiva
#						   con los diferentes candidatos hasta 
#						   tener un cuadro completo y validarlo 
# 						  
#Autor                   : HGT 
#
#Documentacion Params    : 
#
#Tipo          Nombre                          Descripcion 
#=========     ======================          ==================================
# int          numero                          Numero candidato a agregar/remover
# Array        cuadrado 					   Arreglo bidimensional del cuadro 
# int          numFila 						   Fila actual del cuadro
#################################################################################

def backTrack(numero,cuadrado,numFila):
	#imprimirCuadro(cuadrado)
	if(numero==(tamanioCuadroMagico*numFila)):
		filaCandidata=verificaFilaMagica(cuadrado,numFila)
		if(filaCandidata!=1):
			return None
	if(numero==tamanioMaximo):
		global numeroTotaldeCuadros
		numeroTotaldeCuadros +=1
		if(verificarCuadroMagico(cuadrado)):
			print("Es solucion")
			global numeroSoluciones 
			numeroSoluciones+=1
			imprimirCuadro(cuadrado)
	else:
		candidatosList=construirCandidatos(cuadrado,numFila)
		for i in range(len(candidatosList)):
			if(candidatosList[i]!=0):
				posx=(numero/tamanioCuadroMagico)
				posy=(numero%tamanioCuadroMagico)
				cuadrado[posx][posy]=candidatosList[i]
				backTrack(numero+1,cuadrado,numFila)
				cuadrado[posx][posy]=0
	return None






tamanioCuadroMagico=3
numeroMagico= tamanioCuadroMagico*(tamanioCuadroMagico*tamanioCuadroMagico+1)/2
numeroSoluciones=0
tamanioMaximo = tamanioCuadroMagico * tamanioCuadroMagico
debugEnable=False
print "Numero Magico %d " % numeroMagico 
cuadroMagico = [[0 for x in xrange(tamanioCuadroMagico)] for x in xrange(tamanioCuadroMagico)] 

#cuadroMagico[0][0]=8
#cuadroMagico[0][1]=1
#cuadroMagico[0][2]=6
#cuadroMagico[1][0]=3
#cuadroMagico[1][1]=5
#cuadroMagico[1][2]=7
#cuadroMagico[2][0]=4
#cuadroMagico[2][1]=9
#cuadroMagico[2][2]=2


#cuadroMagico[0][0]=1
#cuadroMagico[0][1]=2
#cuadroMagico[0][2]=6
#cuadroMagico[1][0]=3
#cuadroMagico[1][1]=5
#cuadroMagico[1][2]=7
#cuadroMagico[2][0]=4
#cuadroMagico[2][1]=9
#cuadroMagico[2][2]=2



#imprimirCuadro(cuadroMagico)
start_time = time.time()
backTrack(0,cuadroMagico,1)
print("--- Total de segundos transcurridos %s  ---" % (time.time() - start_time))
print("Numero de soluciones encontradas %d" % numeroSoluciones)
print("Numero total de cuadros construidos %d"%numeroTotaldeCuadros)
#print "IS cuadro Magico %d" % verificarCuadroMagico(cuadroMagico)

#print construirCandidatos(cuadroMagico,2)


