import pandas as pd
import random

random.seed(42)

data = {
    "year": [y for y in [2020, 2021, 2022] for _ in range(4)],
    "quarter": [1, 2, 3, 4] * 3,
    "sales": [random.randint(100, 500) for _ in range(12)],
    "returns": [random.randint(10, 80) for _ in range(12)]
}

frame = pd.DataFrame(data)
# frame["difference"] = frame["y"] - frame["x"]

# print(frame.sort_values("y", ascending=True))
# print(frame.describe())
# print(frame)
# print(frame.groupby("year")["sales"].mean())

print(frame.groupby("year")[["sales", "returns"]].mean())