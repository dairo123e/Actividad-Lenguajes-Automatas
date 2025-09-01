# ejercicios_union.py
"""
Ejercicios de UNIÓN de lenguajes (Rama 1).
Incluye impresiones ordenadas para facilitar revisión.
"""

from lenguajes import (
    L1, L2, L3, L4, L5,
    union_lenguajes, pertenece
)

def mostrar(etiqueta, conjunto):
    print(f"{etiqueta}: {sorted(conjunto)}")

def main():
    # 1
    r1 = union_lenguajes(L1, L2); mostrar("L1 ∪ L2", r1)
    # 2
    r2 = union_lenguajes(L1, L3); mostrar("L1 ∪ L3", r2)
    # 3
    r3 = union_lenguajes(L2, L3); mostrar("L2 ∪ L3", r3)
    # 4
    r4 = union_lenguajes(L4, L5); mostrar("L4 ∪ L5", r4)
    # 5
    r5 = union_lenguajes(L1, L2, L3); mostrar("L1 ∪ L2 ∪ L3", r5)
    # 6
    A = {"cad", "aca", "ad"}; B = {"a", "d", "c"}
    r6 = union_lenguajes(A, B); mostrar("A ∪ B", r6)
    # 7
    A2 = {"10", "01", "11"}; B2 = {"0", "1"}; C2 = {"00", "10"}
    r7 = union_lenguajes(A2, B2, C2); mostrar("A ∪ B ∪ C", r7)
    # 8
    r8 = union_lenguajes(L1, L2); print('¿"abc" ∈ (L1 ∪ L2)?', pertenece("abc", r8))
    # 9
    r9 = union_lenguajes(L4, L5); print('¿"a" ∈ (L4 ∪ L5)?', pertenece("a", r9))
    # 10 (prueba adicional)
    X = {"x", "y"}; Y = {"y", "z"}
    r10 = union_lenguajes(X, Y); mostrar("X ∪ Y (prueba)", r10)

if __name__ == "__main__":
    main()
