def paths_through_lattics(lattice_size):
    numerator = 1
    denominator = 1
    for i in range(1, lattice_size + 1):
        numerator *= lattice_size + i
        denominator *= i
    return numerator / denominator


def euler15():
    return paths_through_lattics(20)
