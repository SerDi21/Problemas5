import sys


Weight = int
BinNumber = int
Bin = list[Weight]


def read_weights(name) -> list[Weight]:
    f = open(name)
    f.readline()
    return [int(i) for i in f.readlines()]


def read_data(f) -> list[BinNumber]:
    return [int(i) for i in f.readlines()]


def process(bin_numbers: list[BinNumber], weights: list[Weight]) -> list[Bin]:
    d = {}
    for it, p in enumerate(bin_numbers):
        if p not in d:
            d[p] = []
        d[p].append(weights[it])
    return [sorted(d[p]) for p in sorted(d.keys())]


def show_results(bins: list[Bin]):
    for i, b in enumerate(bins):
        print(f"{i:3}: {', '.join(str(it) for it in b)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Error: necesito exactamente un parámetro, el nombre el fichero del problema")
        sys.exit(1)
    weights = read_weights(sys.argv[1])
    bin_numbers = read_data(sys.stdin)
    bins = process(bin_numbers, weights)
    show_results(bins)

