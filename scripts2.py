import numpy as np
import pandas as pd
from math import sqrt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from tabulate import tabulate
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def graphics_linear_regression(data1, data2, data1_copy, data2_copy): # Построение моделей регрессии и
                                                                      # получение коэффициентов tata0 и tata1.
    global model1

    model = LinearRegression().fit(data2_copy, data1)

    plt.scatter(sum_tomato2, people, c='r', alpha=0.5)
    plt.plot(sum_tomato2, model.predict(sum_tomato2), c='b', linewidth=3)
    plt.xlabel('Томаты')
    plt.ylabel('Покупатели')
    plt.show()

    print(f"Коэффициенты первой модели:\n"
        f"Θ0: {round(model.coef_[0][0], 4)};\n"
        f"Θ1: {round(model.intercept_[0], 4)}\n")

    model11 = LinearRegression()
    model1 = model11.fit(data1_copy, data2)

    plt.scatter(people2, sum_tomato, c='r', alpha=0.5)
    plt.plot(people2, model1.predict(people2), c='b', linewidth=3)
    plt.xlabel('Покупатели')
    plt.ylabel('Томаты')
    plt.show()

    print(f"Коэффициенты второй модели:\n"
        f"Θ0: {round(model1.coef_[0][0], 4)};\n"
        f"Θ1: {round(model1.intercept_[0], 4)}\n")

    return round(model1.intercept_[0], 4), round(model1.coef_[0][0], 4)


data = pd.read_excel("data.xlsx", usecols='L:M').to_dict() # Организация ввода данных.

data['Покупатели'] = data['Вариант 3']
data['Томаты'] = data['Unnamed: 12']

people = np.array(list(data['Покупатели'].values())[2:]).reshape((-1, 1)); people2 = people.copy()
sum_tomato = np.array(list(data['Томаты'].values())[2:]).reshape((-1, 1)); sum_tomato2 = sum_tomato.copy()

tata1, tata0 = graphics_linear_regression(people, sum_tomato, people2, sum_tomato2) # Получение коэффициентов регрессии.

# Оценка полученных коэффициентов, по статистике Стьюдента.
errors = sum_tomato2 - np.mean(sum_tomato2)
error_variance = np.var(errors)
weights = 1 / error_variance

X = sm.add_constant(people)
model__ = sm.WLS(sum_tomato2, X, weights=weights)
results = model__.fit()

print(results.summary())

f_stat = round(results.fvalue, 4)
f_stat_znach = results.f_pvalue

fxi_data = model1.predict(people2)
average_sum_tomato = np.mean(sum_tomato)
sum_yi_sum_tomato = sum([(y - average_sum_tomato) ** 2 for y in sum_tomato])

# Расчёт сумм квадратов.
ess = round(sum([(fxi - average_sum_tomato) ** 2 for fxi in fxi_data])[0], 4)
rss = round(sum([(yi - fxi) ** 2 for yi, fxi in zip(sum_tomato2, fxi_data)])[0], 4)
tss = round(sum_yi_sum_tomato[0], 4)

# Построение таблицы дисперсионного анализа.
headers = ['Источник дисперсии', 'Число степеней свободы', 'Сумма квадратов',
            'Средняя сумма квадратов', 'F-статистика', 'F-критическое', 'Значимость']

data_for_table1 = ['Регрессия', 1, rss, round(rss / 1, 4), f_stat, 4.08, 'Да']
data_for_table2 = ['Ошибка', 48, ess, round(ess / 48, 4), '––', '––', '––']
data_for_table3 = ['Итог', 49, tss, round(tss / 49, 4), '--', '--', '--']

print(tabulate([data_for_table1, data_for_table2, data_for_table3],
                headers=headers, tablefmt='pretty'), '\n\n')

# Проведение точечного и интервального прогнозирования.
x_prognoz = 2500; std_error = 5.027
y_dot_analys = tata1 + tata0 * x_prognoz
average_people = float(np.mean(people))
std_people = np.std(people)
sum_xi_people = sum([(x - average_people) ** 2 for x in people2])

mark_std_error = round((std_error * sqrt((1 / 50) + ((x_prognoz - average_people) ** 2 / sum_xi_people))), 4)

gran1 = round(y_dot_analys - 2.007 * mark_std_error, 4)
gran2 = round(y_dot_analys + 2.007 * mark_std_error, 4)
interval_for_all_data = stats.norm.interval(0.95, loc=average_people, scale=std_people)

print(f"Результат расчёта прогнозируемой точки: {y_dot_analys}\n")
print(f"Оценка стандартной ошибки: {mark_std_error}\n")
print(f"Доверительный интервал для прогнозируемой точки: {y_dot_analys}, равен:\n"
        f"[{gran1}; {gran2}]\n")


x = [2500, 2500]; y = [gran1, gran2]

plt.scatter(x_prognoz, y_dot_analys, color='r')
plt.plot(people2, model1.predict(people2), c='black', linewidth=3)
plt.scatter(average_people, average_sum_tomato, color='g')
plt.scatter(people2, sum_tomato, color='y')
plt.scatter(x, y, color='cyan')
sns.regplot(x=np.array(people), y=np.array(sum_tomato))
plt.show()
