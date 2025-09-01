
from lenguajes import L1, L2, L3, L4, L5

def interseccion(LA, LB):
    """Devuelve la intersección de dos lenguajes finitos."""
    return LA.intersection(LB)

def mostrar_ejercicio(num, LA, LB, nombreA, nombreB):
    print(f"\nEjercicio {num}: {nombreA} ∩ {nombreB}")
    print(f"{nombreA} = {LA}")
    print(f"{nombreB} = {LB}")
    resultado = interseccion(LA, LB)
    print(f"Resultado: {resultado}")
    return resultado

if _name_ == "_main_":
    # 10 ejercicios
    mostrar_ejercicio(1, L1, L2, "L1", "L2")
    mostrar_ejercicio(2, L1, L3, "L1", "L3")
    mostrar_ejercicio(3, L1, L4, "L1", "L4")
    mostrar_ejercicio(4, L1, L5, "L1", "L5")
    mostrar_ejercicio(5, L2, L3, "L2", "L3")
    mostrar_ejercicio(6, L2, L4, "L2", "L4")
    mostrar_ejercicio(7, L2, L5, "L2", "L5")
    mostrar_ejercicio(8, L3, L4, "L3", "L4")
    mostrar_ejercicio(9, L3, L5, "L3", "L5")
    mostrar_ejercicio(10, L4, L5, "L4", "L5")