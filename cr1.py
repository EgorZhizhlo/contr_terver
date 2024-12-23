import pandas as pd
from collections import Counter
from scipy.stats import chi2
import matplotlib.pyplot as plt

# Считывание данных в виде строки
sample_str = "D; D; B; D; A; B; D; D; NA; NA; B; C; D; D; B; D; C; D; C; D; D; D; D; D; D; B; C; D; NA; D; A; D; B; NA; D; B; D; NA; D; B; C; B; D; D; D; B; NA; D; NA; D; D; D; NA; B; D; B; D; B; C; D; B; B; A; D; D; D; B; C; D; B; C; D; D; D; A; C; D; D; D; B; D; C; D; D; D; D; B; D; NA; B; D; B; D; D; B; D; D; B; D; B; D; D; B; D; A; D; D; B; B; C; D; D; D; D; B; D; B; B; B; B; D; A; D; D; NA; C; D; D; D; A; A; D; B; NA; NA; NA; A; D; A; D; D; D; D; B; D; A; D; D; C; B; C; D; D; D; B; NA; D; D; B; B; B; A; D; C; D; B; B; A; D; D; B; C; D; C; D; D; D; D; D; D; D; NA; B; D; D; B; D; D; NA; B; C; A; D; D; NA; D; D; D; D; D; D; B; A; D; C; B; D; B; A; B; D; D; D; B; B; D; B; C; D; D; B; D; B; B; B; A; D; A; B; NA; NA; C; D; A; A; A; C; B; B; D; D; C; D; D; D; D; D; B; A; D; D; D; B; D; D; B; D; NA; NA; D; D; A; A; D; D; C; D; D; D; A; C; D; D; D; A; A; D; D; B; B; D; B; NA; D; D; A; D; D; B; B; D; D; B; D; D; NA; D; D; D; D; D; D; D; D; C; D; D; A; D; D; D; D; D; D; D; C; D; D; D; D"
# Преобразование строки в список
sample = sample_str.split('; ')

# Преобразование в DataFrame
df = pd.DataFrame(sample, columns=["A"])
df.to_csv("cr.csv")

# Очистка от NA
df_cleaned = df[df['A'] != 'NA']
print("NA количество", len(sample) - len(df_cleaned))

# 1. Объем очищенной выборки
print("Объем очищенной выборки:", len(df_cleaned))

# 2. Количество уникальных ответов
unique_answers = df_cleaned['A'].nunique()
print("Количество различных вариантов ответов:", unique_answers)

# 3. Количество ответов 'B'
count_bl = df_cleaned['A'].value_counts().get('B', 0)
print("Количество ответов 'B':", count_bl)

# 4. Доля ответов 'B'
count_red = df_cleaned['A'].value_counts().get('B', 0)
red_ratio = count_red / len(df_cleaned)
print("Доля ответов 'B':", red_ratio)

# 5-6. Доверительный интервал для 'B'(в excel)
n = len(df_cleaned)
# 7-10. Хи-квадрат критерий
expected = n / unique_answers
observed = df_cleaned['A'].value_counts()
chi2_stat = sum((observed - expected) ** 2 / expected)
df_chi2 = unique_answers - 1
critical_value = chi2.ppf(1 - 0.1, df_chi2)
reject_h0 = int(chi2_stat > critical_value)
print("Степени свободы:", df_chi2)
print("Критическое значение хи-квадрат:", critical_value)
print("Наблюдаемое значение хи-квадрат:", chi2_stat)
print("Отвергнуть H0:", reject_h0)

# 11. Гистограмма
df_cleaned['A'].value_counts().plot(kind='bar')
plt.title('Распределение ответов респондентов')
plt.xlabel('Ответы')
plt.ylabel('Частота')
plt.show()
