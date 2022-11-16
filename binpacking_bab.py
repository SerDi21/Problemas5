import sys
from collections.abc import Iterable
from dataclasses import dataclass
from typing import TextIO
from algoritmia.schemes.bab_scheme import BoundedDecisionSequence, bab_min_solve

Weight = int
Value = int
Decision = int
Solution = tuple[Decision, ...]
Score = Value
State = tuple[int, Weight]


def read_data(f: TextIO) -> tuple[int, list[int]]:
    C = int(f.readline())
    w = [int(linea) for linea in f.readlines()]
    return C, w


def process(C: int, w: list[int]) -> list[int]:
    @dataclass
    class Extra:
        free: list[int]

    class BinpackingDS(BoundedDecisionSequence):
        def calculate_opt_bound(self) -> Score:
            minObjeto = w[-1]
            libre = sum(f for f in self.extra.free if f >= minObjeto)
            maxHueco = max(self.extra.free)
            caben = 0
            total = 0
            for i in range(len(self), n):
                total += w[i]
                if w[i] <= maxHueco:
                    caben += w[i]
            nuevos = (total - min(caben, libre) + C - 1)
            return len(self.extra.free) + nuevos



        def calculate_pes_bound(self) -> Score:
            pass

        def is_solution(self) -> bool:
            return len(self) == n

        def solution(self) -> Solution:
            return self.decisions()

        def succesors(self) -> Iterable["BoundedDecisionSequence"]:
            if not self.is_solution():
                obj = w[len(self)]
                for i in range(len(self.extra.free)):
                    if obj <= self.extra.free[i]:
                        free_copia = self.extra.free[:]
                        free_copia[i] -= obj
                        yield self.add_decision(i, Extra(free_copia))
                free_copia = self.extra.free[:]
                free_copia.append(C - obj)
                yield self.add_decision(len(free_copia) - 1, Extra(free_copia))


    n = len(w)
    return bab_min_solve(BinpackingDS())


def show_results(contenedores: list[int]):
    for c in contenedores:
        print(c)


if __name__ == "__main__":
    C, w = read_data(sys.stdin)
    contenedores = process(C, w)
    show_results(contenedores)