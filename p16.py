from random import random

RED = "red"
GREEN = "green"


def draw_marbles(u, n=1, k=1):
    samples = [[RED if random() < u else GREEN for _ in range(n)] for _ in range(k)]
    if k == 1:
        return samples[0]
    return samples


def check_no_red(marbles):
    return all([m == GREEN for m in marbles])


def check_at_least_one_no_red(samples):
    for marbles in samples:
        if check_no_red(marbles):
            return True
    return False


def simulate(experiment, check_outcome, repetitions, *args, **kwargs):
    i = 0
    for _ in range(repetitions):
        if check_outcome(experiment(*args, **kwargs)):
            i += 1

    return i / repetitions


if __name__ == "__main__":

    # Item (a)
    repetitions = int(1e6)
    print(f"Probability that v=0 (calculated with {repetitions} simulations):")
    print("mu=0.05: ", simulate(draw_marbles, check_no_red, repetitions, 0.05, n=10))
    print("mu=0.5: ", simulate(draw_marbles, check_no_red, repetitions, 0.5, n=10))
    print("mu=0.8: ", simulate(draw_marbles, check_no_red, repetitions, 0.8, n=10))

    # Item (b)
    repetitions = int(1e3)
    print(
        f"Probability that at least one experiment out of 1000 result in v=0 (calculated with {repetitions} simulations):"
    )
    print(
        "mu=0.05: ",
        simulate(
            draw_marbles, check_at_least_one_no_red, repetitions, 0.05, n=10, k=1000
        ),
    )
    print(
        "mu=0.5: ",
        simulate(
            draw_marbles, check_at_least_one_no_red, repetitions, 0.5, n=10, k=1000
        ),
    )
    print(
        "mu=0.8: ",
        simulate(
            draw_marbles, check_at_least_one_no_red, repetitions, 0.8, n=10, k=1000
        ),
    )

    # Item (c)
    repetitions = 10
    print(
        f"Probability that at least one experiment out of 1,000,000 result in v=0 (calculated with {repetitions} simulations):"
    )
    print(
        "mu=0.05: ",
        simulate(
            draw_marbles,
            check_at_least_one_no_red,
            repetitions,
            0.05,
            n=10,
            k=int(1e6),
        ),
    )
    print(
        "mu=0.5: ",
        simulate(
            draw_marbles, check_at_least_one_no_red, repetitions, 0.5, n=10, k=int(1e6),
        ),
    )
    print(
        "mu=0.8: ",
        simulate(
            draw_marbles, check_at_least_one_no_red, repetitions, 0.8, n=10, k=int(1e6),
        ),
    )
