# lenguajes.py
"""
Funciones y lenguajes base para operaciones con lenguajes finitos.
Sigma = {a, b, c}
"""

from typing import Iterable, Set

# Alfabeto base
SIGMA: Set[str] = {"a", "b", "c"}

# Lenguajes dados
L1: Set[str] = {"a", "b", "ab", "ba"}
L2: Set[str] = {"b", "c", "bc", "cb"}
L3: Set[str] = {"a", "b", "c"}
L4: Set[str] = {"ab", "ac"}
L5: Set[str] = {"b", "bc", "ca", "c"}

def union_lenguajes(*lenguajes: Iterable[str]) -> Set[str]:
    """
    Devuelve la unión de N lenguajes finitos.
    Cada lenguaje se interpreta como un iterable de cadenas.
    """
    u: Set[str] = set()
    for L in lenguajes:
        u |= set(L)
    return u

def interseccion_lenguajes(*lenguajes: Iterable[str]) -> Set[str]:
    """
    Devuelve la intersección de N lenguajes finitos.
    Si no se pasa ninguno, devuelve el conjunto vacío.
    """
    it = None
    for L in lenguajes:
        it = set(L) if it is None else (it & set(L))
    return it if it is not None else set()

def concatenacion_lenguajes(A: Iterable[str], B: Iterable[str]) -> Set[str]:
    """
    Devuelve la concatenación A·B = { x+y | x∈A, y∈B }.
    Soporta ε representada como cadena vacía "" si aparece en A o B.
    """
    A, B = set(A), set(B)
    return {x + y for x in A for y in B}

def pertenece(palabra: str, lenguaje: Iterable[str]) -> bool:
    """True si la palabra pertenece al lenguaje."""
    return palabra in set(lenguaje)
