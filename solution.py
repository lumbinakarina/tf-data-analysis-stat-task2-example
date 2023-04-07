import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 484112867 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 86
    mean1 = 2 / t ** 2 * (gamma.ppf((1 - p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    mean2 = 2 / t ** 2 * (gamma.ppf((1 + p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    return mean1, mean2
