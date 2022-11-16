import sys
from collections.abc import Iterable
from dataclasses import dataclass
from typing import TextIO

from algoritmia.schemes.bab_scheme import BoundedDecisionSequence, bab_max_solve

Weight = int
Value = int
Solution = tuple[Value, Weight, tuple[int, ...]]
Score = Value
State = tuple[int, Weight]


def read_data(f: TextIO) -> tuple[int, list[Value], list[Weight]]:
    peso = int(f.readline())
    v = []
    w = []
    for line in f.readlines():
        elems = line.strip().split()
        v.append(int(elems[0]))
        w.append(int(elems[1]))
    return peso, v, w


@dataclass
class Extra:
    accum: Weight
    valor: Value


def process(peso: int, v: list[Value], w: list[Weight]) -> Solution:

    class KnapsackBDS(BoundedDecisionSequence):

        def is_solution(self) -> bool:
            return len(self) == n

        def solution(self) -> Solution:
            return self.extra.valor, self.extra.accum, self.decisions()

        def successors(self) -> Iterable["KnapsackBDS"]:
            if not self.is_solution():
                if not self.is_solution():
                    yield self.add_decision(0, self.extra)
                    i = len(self)
                    naccum = self.extra.accum + w[i]
                    if naccum <= peso:
                        nvalue = self.extra.valor + v[i]
                        yield self.add_decision(1, Extra(naccum, nvalue))

        def calculate_opt_bound(self) -> Score:
            value = self.extra.valor
            free = peso - self.extra.valor
            for i in range(len(self), n):
                if w[i] <= free:
                    value += v[i]
                    free -= w[i]
                else:
                    r = free/w[i]
                    value += r*v[i]
                    break
            return value

        def calculate_pes_bound(self) -> Score:
            value = self.extra.valor
            free = peso - self.extra.valor
            for i in range(len(self), n):
                if w[i] <= free:
                    value += v[i]
                    free -= w[i]
            return value

        def state(self) -> State:
            return len(self), self.extra.accum

    n = len(v)
    return bab_max_solve(KnapsackBDS(Extra(0, 0)))


def show_results(sol: Solution):
    print(sol[0])
    print(sol[1])
    for decision in sol[2]:
        print(decision)


if __name__ == "__main__":
    mochila, valores, pesos = read_data(sys.stdin)
    solucion = process(mochila, valores, pesos)
    show_results(solucion)
