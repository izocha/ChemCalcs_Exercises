import numpy as np
import matplotlib.pyplot as plt
from math import *


def rect_line():
	rxy = np.arange(0,1.1,0.1)
	return rxy


def R_factor(L,D):
	R = L/D
	return R

def Rectification_line(R,D,xD,xn):
	Rline = ((R/(R+D))*xn)+(xD/(R+D))
	Rline = np.array(Rline)
	return Rline

def Q_sensible(Ce,Teb,Tent):
	qS = Ce*(Teb - Tent)
	return qS

def q_data(qS,qL):
 	q = (qS + qL)/qL
 	return q

def Q_line(q,xF,q1):
	Q =  ((q/(q-1))*q1)-(xF/(q-1))
	return Q

def McCabe():
	rxy = rect_line()
	R = R_factor(L,D) 
	xn = rect_line()
	Rline = np.array(Rectification_line(R,D,xD,xn))
	qS = Q_sensible(Ce,Teb,Tent)
	q = q_data(qS,qL)
	q1 = rect_line()
	Q = Q_line(q,xF,rxy)

	plt.figure()
	plt.plot(rxy,rxy,"b--p")      # Graficando recta de 45°
	plt.plot(X,Y,"r--p")          # Graficando datos de X e Y
	plt.plot(xn,Rline, "k--p")    # Graficando línea de rectificación
	plt.plot(q1,Q, "c--p")        # Graficando línea Q(Q line)
	plt.arrow(xD,0.0,0.0,xD,linestyle=":")
	plt.xlabel("X")               # Nombre de eje
	plt.ylabel("Y")               # Nombre de eje
	plt.xlim(0,1)                 # Rango de eje X
	plt.ylim(0,1)                 # Rango de eje Y
	plt.grid(color='b', linestyle='-', linewidth=0.1)
	plt.xticks(lines, size="xx-small")
	plt.yticks(lines, size="xx-small")
	plt.show()

#Método gráfico McCabe Thiele
#Instrucciones
lines = np.arange(0,1.05,0.05)

#Datos de fraccióm

X = np.array([0,0.08,0.185,0.300,0.42,0.575,0.762,1])
Y = np.array([0,0.165,0.325,0.490,0.635,0.77,0.895,1])

#Datos de concentración en fracción molar del más volatil de la mezcla

xF = 0.45 #Fracción molar del componente a destilar(más volatil) en el alimento 
xD = 0.92 #Fracción molar del componente a destilar(más volatil) en destilado
xW = 0.15 #Fracción molar del componente a destilar(más volatil) en los fondos 

#Datos para el reflujo
L = 4 
D = 1

#Datos termodinámicos

Tent = 131 #Temperatura a la entrada de la columna
Teb = 210 #Temperatura de ebullición a condiciones de trabajo en columna
Ce = 40 # Capacidad calorífica molar de la mezcla
qL = 13700 # Calor latente de la mezcla en BTU/mol F -> Se puede sacar de tabla como: hVsat - hLsat

McCabe()
