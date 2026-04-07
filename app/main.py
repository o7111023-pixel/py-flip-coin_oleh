# write your code here
import matplotlib.pyplot as plt

import random
from typing import Dict


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results: Dict[int, int] = {i: 0 for i in range(11)}  # 0 to 10 heads

    for _ in range(num_trials):
        heads: int = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    percentages: Dict[int, float] = {}
    for k, v in results.items():
        percentages[k] = round(v / num_trials * 100, 2)

    return percentages


def draw_gaussian_distribution_graph() -> None:
    data: Dict[int, float] = flip_coin(20000)

    x: list[int] = list(data.keys())
    y: list[float] = list(data.values())

    plt.bar(x, y)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of Heads in 10 Coin Tosses")
    plt.show()


draw_gaussian_distribution_graph()


print(flip_coin())
