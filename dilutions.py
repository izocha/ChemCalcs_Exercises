N1 = float(
    input("Ingrese la concentración de la solución concentrada en M:\n")
)
N2 = float(input("Ingrese la concentración deseada de la dilución en M:\n"))
V2 = float(input("Ingrese el volumen deseado de la dilución en mL:\n"))
V1 = (N2 * V2) / N1

if N2 < N1:
    print("El volumen de concentrado añadir es:", V1, " mL")
else:
    print("La concentración de la dilución es mayor que la del concentrado")
