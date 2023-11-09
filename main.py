import numpy as np

def Fibona(n):
    arr = [1, 1]
    if n == 1:
        return [1]
    elif n == 2:
        return arr
    else:
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])
        return arr

def puz(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def calcul(a, b, sim):
    if sim == '+':
        return a + b
    elif sim == '-':
        return a - b
    elif sim == '*':
        return a - b
    elif sim == '/':
        if b == 0:
            return "Деление на ноль"
        return a / b
    else:
        return "Нет такоого символа"