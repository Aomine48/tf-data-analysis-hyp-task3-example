import pandas as pd
import numpy as np


chat_id = 515069313 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = mannwhitneyu(x, y, alternative='less')
    return res.pvalue < 0.05 # Ваш ответ, True или False
