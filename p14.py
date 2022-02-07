from random import random, choice, seed
import matplotlib.pyplot as plt

sign = lambda x: 1 if x >= 0 else -1


def calculate_initial_w(data):
    positives = [p for p, label in data if label == 1]
    negatives = [p for p, label in data if label == -1]
    d = len(positives[0])
    w = []
    avg_points = []
    for i in range(d):
        avg_pos_xi = sum([p[i] for p in positives]) / len(positives)
        avg_neg_xi = sum([p[i] for p in negatives]) / len(negatives)

        w.append(avg_pos_xi - avg_neg_xi)
        avg_points.append((avg_pos_xi, avg_neg_xi))

    w0 = sum([-(pi ** 2 - ni ** 2) / 2 for pi, ni in avg_points])

    return [w0] + w


def linearly_separable_multidim(origin, box, n):
    w = [random() for _ in box]
    b = sum(
        [
            wi * (-dim_orig - dim_len / 2)
            for wi, dim_orig, dim_len in zip(w, origin, box)
        ]
    )

    f = lambda x: 1 if sum([wi * xi for wi, xi in zip(w, x)]) + b >= 0 else -1

    data = []
    for _ in range(n):
        x = [random() * dim_len + dim_orig for dim_orig, dim_len in zip(origin, box)]
        data.append((x, f(x)))

    return data, [b] + w


def plot_data(data, ax):
    X_pos = [point[0] for point, label in data if label == 1]
    Y_pos = [point[1] for point, label in data if label == 1]
    X_neg = [point[0] for point, label in data if label == -1]
    Y_neg = [point[1] for point, label in data if label == -1]
    ax.scatter(X_pos, Y_pos, marker="o", color="blue", label="positive")
    ax.scatter(X_neg, Y_neg, marker="x", color="red", label="negative")


def plot_line(w, x1, x2, ax, color="black", label=""):
    C, A, B = w

    y1 = (-C - A * x1) / B
    y2 = (-C - A * x2) / B

    ax.plot([x1, x2], [y1, y2], color=color, label=label)


def perceptron(data, max_iter=-1, first_or_choice=True):
    perceptron = lambda w, x: 1 if sum([a * b for a, b in zip(w, x)]) >= 0 else -1
    d = len(data[0][0])
    data = [([1] + x, y) for x, y in data]
    w = [0] * (d + 1)

    it = 0
    while max_iter == -1 or it < max_iter:
        it += 1
        incorrect = [(x, y) for x, y in data if perceptron(w, x) != y]
        if len(incorrect) == 0:
            break
        if it % 1000 == 0:
            print(f"Iteration: {it}, incorrect: {len(incorrect)}")

        if first_or_choice:
            xw, yw = incorrect[0]
        else:
            xw, yw = choice(incorrect)
        w = [a + yw * b for a, b in zip(w, xw)]

    return w, it, len([(x, y) for x, y in data if perceptron(w, x) != y])


if __name__ == "__main__":
    import sys

    item = "a" if len(sys.argv) < 2 else sys.argv[1]
    assert item in list("abcdefgh")

    print(f"EXPERIMENT FOR ITEM ({item})")

    # ==== ADJUSTABLE PARAMETERS ==== #

    # (a)(b)(c)
    dim = 2
    points = 20
    max_iter = -1
    first_misclassified = True
    number_experiments = 1  # makes sense to be > 1 only if first_misclassified=False
    verbose = True  # print each experiment results
    plot_outcome = True  # only valid if dim=2
    plot_histogram = False  # makes sense only if number of experiments is large

    # (d)
    if item == "d":
        points = 100

    # (e)
    if item == "e":
        points = 1000

    # (f)
    if item == "f":
        # The reported results didn't use this seed, so it won't reproduce them.
        # The code was refactored this way after the results were reported.
        seed(0)
        dim = 10
        points = 1000
        plot_outcome = False

    # (g)
    if item == "g":
        seed(0)
        dim = 10
        points = 1000
        number_experiments = 100
        plot_outcome = False
        first_misclassified = False
        plot_histogram = True

    # =============================== #

    origin = [0] * dim
    box = [1] * dim

    data, w = linearly_separable_multidim(origin, box, points)

    exps = []
    for i in range(number_experiments):
        w_learned, n_it, incorrect = perceptron(
            data, max_iter=max_iter, first_or_choice=first_misclassified
        )
        exps.append((w_learned, n_it))
        if verbose:
            print(f"Experiment {i+1} iterations: {n_it}, incorrect: {incorrect}")

    if plot_outcome and dim == 2:
        w_learned, _ = exps[0]
        width = box[0]
        height = box[1]
        fig, ax = plt.subplots()
        plot_data(data, ax)
        plot_line(w, origin[0], origin[0] + width, ax, label="f")
        plot_line(
            w_learned, origin[0], origin[0] + width, ax, color="orange", label="g"
        )
        ax.set_xlim(origin[0], origin[0] + width)
        ax.set_ylim(origin[1], origin[1] + width)
        ax.set_xlabel("salary")
        ax.set_ylabel("age")
        ax.legend()
        plt.show()

    if plot_histogram:
        exps = [exp[1] for exp in exps]
        plt.hist(exps, bins=10)
        plt.gca().set(xlabel="iterations", ylabel="frequency")
        plt.show()
