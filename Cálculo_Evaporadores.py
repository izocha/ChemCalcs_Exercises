#*---------------------importando modulos necesarios---------------------------------*

from os import system

#*---------------------función presentación------------------------------------------*

def presentación():
	print(f"""
		*------------------------------------------------------------------------*
		| Cálculos para ejercicios de evaporadores -> Presiona q o Q para salir  |
		| Ingresa los datos cuando se te pidan para ejecutar bien el programa    |
		*------------------------------------------------------------------------*""")

#---------------------función validación de valores----------------------------------*

def value(x):
	a = True
	while a:
		try:
			y = input(f"Valor {x}: ")
			if y.isnumeric():
				y = int(y)
			else:
				y = float(y)
			a = False
		except:
			print("Por favor ingresa un valor numérico")
	return y

#--------------------función explicación L---------------------------------------------*

def calculosL():
	print(f"""
		*------------------------------------------------------------------------*
		| F*xF = V*xV + L*xL -> Si se supone no hay sólidos en V, xV = 0         |
		| Entonces queda: L = (F*xF)/xL                                          |
		*------------------------------------------------------------------------*""")

#--------------------función cálculo de L---------------------------------------------*

def liquid(F,xF,xL):
	L = (F*xF)/xL
	print(f"Valor L: {L}")
	return L

#--------------------función explicación L---------------------------------------------*

def calculosV():
	print(f"""
		*------------------------------------------------------------------------*
		|                            V = F - L                                   |
		| Se halla V sin los %sólidos para no trabajar con xV porque xV vale 0   |
		*------------------------------------------------------------------------*""")

#--------------------función cálculo de V---------------------------------------------*

def vapour(F,L):
	V = F-L
	print(f"Valor V: {V}")
	return V

#--------------------función explicación de P------------------------------------------*

def pressure(Pe,Pm):
	Pabs = Pe + Pm
	print(f"Valor Pabs: {Pabs}")
	return Pabs

#--------------------función explicación de S------------------------------------------*

def calculosS():
	print(f"""
		*------------------------------------------------------------------------*
		|             Ef * S(hs - hc) = (V*hF + L*hL) - F*hF                     |
		| Despejando S para obtener valor de steam:                              |
		|             S = ((V*hF + L*hL)- F*hF)/ S*(hs - hc)                     |
		| Donde:                                                                 |
		|S:  Steam en kg/h                                                       |
		|hs: entalpía de steam en la entrada del evaporador(como vapor)          |
		|hc: entalpía de steam en la entrada del evaporador(como condensado)     |
		|hF: entalpía en F a la presión del evaporador                           |
		|hV: entalpía en V a la presión del evaporador                           | 
		|hL: entalpía en L a la presión del evaporador                           |
		| Puedes sacar estos valores de tu tabla o interpolando                  |
		| Otro punto a tener en cuenta es la alimentación, en esos casos         |
		| si la alimentación es una solución, utiliza Duhring si lo amerita      |
		| Para coloides y suspensiones en cambio, no es tan necesario es uso.    |
		*------------------------------------------------------------------------*""")

#--------------------función cálculo de S------------------------------------------*

def steam(hs,hc,Ef,F,hF,V,hV,L,hL):
	Qp = (Ef*(hs-hc))
	entrance = (F*hF)
	exit = (V*hV + L*hL)
	Qg = (exit - entrance)
	S = Qg/Qp
	print(f"Valor S: {S}")
	return S

#--------------------función cálculo de E------------------------------------------*

def economy(V,S):
	E = S/V
	print(f"Valor E: {E}")
	return E

def execution():
	presentación()
	F = value("F")
	xF = value("xF")
	xL = value("xL")
	calculosL()
	L = liquid(F,xF,xL)
	calculosV()
	V = vapour(F,L)
	Pe = value("Pe")
	Pm = value("Pm")
	pressure(Pe,Pm)
	calculosS()
	hs = value("hs")
	hc = value("hc")
	Ef = value("Ef")
	hF = value("hF")
	hL = value("hL")
	hV = value("hV")
	S = steam(hs,hc,Ef,F,hF,V,hV,L,hL)
	E = economy(V,S)

execution()
