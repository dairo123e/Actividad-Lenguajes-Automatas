# ejercicios_concatenacion.py
"""
Ejercicios de CONCATENACIÓN de lenguajes (Rama dairo).
Nota: ε se representa como cadena vacía "" cuando aplique.
"""

from lenguajes import (
    L1, L2, L3, L4, L5,
    concatenacion_lenguajes, pertenece
)

def mostrar(etiqueta, conjunto):
    print(f"{etiqueta}: {sorted(conjunto)}")

def main():
    # 1
    r1 = concatenacion_lenguajes(L1, L3); mostrar("L1 · L3", r1)
    # 2
    r2 = concatenacion_lenguajes(L3, L1); mostrar("L3 · L1", r2)
    # 3
    r3 = concatenacion_lenguajes(L4, L5); mostrar("L4 · L5", r3)
    # 4
    r4 = concatenacion_lenguajes(L5, L4); mostrar("L5 · L4", r4)
    # 5
    r5 = concatenacion_lenguajes(L1, L2); mostrar("L1 · L2", r5)
    # 6
    A = {"a", "b"}; B = {"a", "c"}
    r6 = concatenacion_lenguajes(A, B); mostrar("A · B", r6)
    # 7 (con ε)
    A2 = {"0", "1"}; B2 = {"", "00"}  # "" representa epsilon
    r7 = concatenacion_lenguajes(A2, B2); mostrar("A · B (ε y '00')", r7)
    # 8
    r8 = concatenacion_lenguajes(L1, L2); print('¿"aba" ∈ (L1 · L2)?', pertenece("aba", r8))
    # 9
    r9 = concatenacion_lenguajes(L3, L4); print('¿"cab" ∈ (L3 · L4)?', pertenece("cab", r9))
    # 10 (prueba adicional)
    X = {"x", ""}; Y = {"y"}  # incluye ε en X
    r10 = concatenacion_lenguajes(X, Y); mostrar("X · Y (prueba)", r10)

if __name__ == "__main__":
    main()
