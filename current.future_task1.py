from concurrent.futures import ProcessPoolExecutor


def sum_row(i, matrix):
    if i <= len(matrix):
        sum = 0
        for w in range(len(matrix[i])):
            sum += matrix[i][w]
    return sum


if __name__ == "__main__":
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = list()
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите элемент [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    index = []
    matrixs = []
    for i in range(rows):
        index.append(i)
        matrixs.append(matrix)
    total_sum = 0
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(sum_row, index, matrixs))
    for j in range(len(res)):
        total_sum += res[j]
    print(total_sum)
