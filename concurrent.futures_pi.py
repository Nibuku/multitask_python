from concurrent.futures import ProcessPoolExecutor
import random


def point(i):
    sum = 0.0
    x = random.random()
    y = random.random()
    sum += (x * x + y * y < 1.0)
    return sum


if __name__ == "__main__":
    number = int(input("Введите количество точек для генерации"))
    iter = [i for i in range(number)]
    total_sum = 0
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(point, iter))
        for j in range(len(res)):
            total_sum += res[j]
        result = (4*total_sum/number)
        print(result)
