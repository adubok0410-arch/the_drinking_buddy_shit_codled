# Решения всех заданий с картинки на Python (печатают ответы)

import math
from itertools import product

# ---------- Вспомогательное ----------
def digits_in_base(x: int, base: int):
    if x == 0:
        return [0]
    d = []
    while x > 0:
        d.append(x % base)
        x //= base
    return d[::-1]

def to_base(n: int, b: int) -> str:
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s


# ---------- Задание 16 №25398 ----------
def task_16_25398():
    def G(n: int) -> int:
        if n >= 221337:
            return 2 * n + 50
        k = (221337 - n + 10) // 11  # ceil
        return (2 * (n + 11 * k) + 50) - 48 * k

    def F(n: int) -> int:
        if n <= 30:
            return 3 * (G(n - 5) + 13)
        k = math.ceil((n - 30) / 6)
        return F(n - 6 * k) + 2048 * k

    return F(5078)


# ---------- Задание 16 №25400 ----------
def task_16_25400():
    def G(n: int) -> int:
        if n < 28:
            return 3 * n - 4
        k = math.ceil((n - 27) / 5)
        return G(n - 5 * k) - 15 * k

    def F(n: int) -> int:
        if n >= 31054:
            return 3 * (G(n - 2) - 15)
        k = math.ceil((31054 - n) / 4)
        return F(n + 4 * k) + 3020 * k

    return F(15)


# ---------- Задание 16 №25355 ----------
def task_16_25355():
    def G(n: int) -> int:
        if n >= 248045:
            return n // 20 + 28
        k = math.ceil((248045 - n) / 9)
        return G(n + 9 * k) - 4 * k

    def F(n: int) -> int:
        if n < 19:
            return 6 * (G(n - 7) - 36)
        k = math.ceil((n - 18) / 4)  # чтобы уйти в <=18
        return F(n - 4 * k) + 3580 * k

    return F(673)


# ---------- Задание 14 №23391 ----------
def task_14_23391():
    x = 30 * pow(36, 231) + 18 * pow(6, 101) - 3 * pow(36, 45) - 2357
    digs = digits_in_base(x, 36)
    return sum(1 for d in digs if (d % 3 == 0) ^ (d % 5 == 0))


# ---------- Задание 14 №23390 ----------
def task_14_23390():
    x = 17 * pow(125, 453) + 117 * pow(5, 231) - 3 * pow(5, 13) - 2357
    digs = digits_in_base(x, 125)
    return sum(1 for d in digs if d <= 37)


# ---------- Задание 14 №23350 ----------
def task_14_23350():
    x = 39 * pow(121, 319) + 46 * pow(11, 913) - 15 * pow(1331, 15) - 1993
    digs = digits_in_base(x, 121)
    return sum(1 for d in digs if 64 <= d <= 104)


# ---------- Задание 8 №26117 ----------
def task_8_26117():
    # порядок из условия: А < Ж < И < М < Н < У < Ч
    A, ZH, I, M, N, U, CH = range(7)
    cnt = 0
    for digs in product(range(7), repeat=6):
        if digs[0] == ZH:
            continue
        if sum(1 for d in digs if d == CH) > 1:
            continue
        val = 0
        for d in digs:
            val = val * 7 + d
        if (val + 1) % 2 == 0:  # чётный номер
            cnt += 1
    return cnt


# ---------- Задание 5 №24302 ----------
def task_5_24302():
    best = None
    for N in range(167, 1_000_000 + 1):
        t = to_base(N, 3)
        s = sum(int(c) for c in t)
        if s % 9 == 0:
            t2 = t + "2"
        else:
            t2 = t + to_base(s % 9, 3)
        R = int(t2, 3)
        if best is None or R < best:
            best = R
    return best


if __name__ == "__main__":
    print(task_16_25398())
    print(task_16_25400())
    print(task_16_25355())
    print(task_14_23391())
    print(task_14_23390())
    print(task_14_23350())
    print(task_8_26117())
    print(task_5_24302())
