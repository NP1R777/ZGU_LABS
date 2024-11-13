import numpy as np
import pandas as pd
import scipy.stats as st
from pprint import pprint
import statsmodels.api as sm
from tabulate import tabulate
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

model1 = None

""" import statsmodels.api as sm

errors = sum_tomato2 - np.mean(sum_tomato2)
error_variance = np.var(errors)
weights = 1 / error_variance

X = sm.add_constant(people)
model__ = sm.WLS(sum_tomato2, X, weights=weights)
results = model__.fit()

print(results.summary()) """

def graphics_linear_regression(data1, data2, data1_copy, data2_copy): # Построение моделей регресии и
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

      model1 = LinearRegression().fit(data1_copy, data2)

      plt.scatter(people2, sum_tomato, c='r', alpha=0.5)
      plt.plot(people2, model1.predict(people2), c='b', linewidth=3)
      plt.xlabel('Покупатели')
      plt.ylabel('Томаты')
      plt.show()

      print(f"Коэффициенты второй модели:\n"
            f"Θ0: {round(model1.coef_[0][0], 4)};\n"
            f"Θ1: {round(model1.intercept_[0], 4)}\n")

      return round(model1.intercept_[0], 4), round(model1.coef_[0][0], 4)



data = pd.read_excel('Econometrics/laba2/data.xlsx', usecols='L:M').to_dict()

data['Покупатели'] = data['Вариант 3']
data['Томаты'] = data['Unnamed: 12']

people = np.array(list(data['Покупатели'].values())[2:]).reshape((-1, 1)); people2 = people.copy()
sum_tomato = np.array(list(data['Томаты'].values())[2:]).reshape((-1, 1)); sum_tomato2 = sum_tomato.copy()

tata1, tata0 = graphics_linear_regression(people, sum_tomato, people2, sum_tomato2)

average_people = np.mean(people)
std_people = np.std(people)
average_sum_tomato = np.mean(sum_tomato)
std_sum_tomato = np.std(sum_tomato)

sum_xi_people = sum([(x - average_people) ** 2 for x in people])
sum_yi_sum_tomato = sum([(y - average_sum_tomato) ** 2 for y in sum_tomato])

t_student_tata0 = round(tata0 / (std_people ** 2 / sum_xi_people)[0], 4)
t_student_tata1 = round(tata1 / (std_sum_tomato ** 2 / sum_yi_sum_tomato)[0], 4)
t_student_krit = 2.021

print(f"Т.к. статистика Стьюдента для тэтта0 = {t_student_tata0}, при крит. знач. {t_student_krit}\n"
      f"то гипотеза не отвергается.\n"
      f"Т.к. статистика Стьюдента для тэтта1 = {t_student_tata1}, при крит. знач. {t_student_krit}\n"
      f"то гипотеза отвергается.\n")

interval_tata1 = st.t.interval(confidence=1-0.95, df=48, loc=tata1, scale=sum_yi_sum_tomato)
print(f"Доверительный интервал для коэффициента {t_student_tata1} равен:"
      f"[{round(interval_tata1[0][0], 3)}; {round(interval_tata1[1][0], 3)}]\n")

fxi_data = model1.predict(people2)

ess = round(sum([(fxi - average_sum_tomato) ** 2 for fxi in fxi_data])[0], 4)
rss = round(sum([(yi - fxi) ** 2 for yi, fxi in zip(sum_tomato2, fxi_data)])[0], 4)
tss = round(sum_yi_sum_tomato[0], 4)
r_square = round((rss / tss), 4)

print(f"R-квадрат: {r_square}", '\n')
stat_fishera = round(48 * (r_square / (1 - r_square)), 4)
krit_fishera = 4.08

print(f"Т.к. значаени статистики Фишера равно: {stat_fishera}, а крит. знач. {krit_fishera},\n"
      f"то гипотеза не отвергается и уравнение регрессии не признаётся значимым.\n")

headers = ['Источник дисперсии', 'Число степеней свободы', 'Сумма квадратов',
            'Средняя сумма квадратов', 'F-статистика', 'F-критическое', 'Значимость']

data_for_table1 = ['Регрессия', 1, rss, round(rss / 1, 4), stat_fishera, krit_fishera, 'Нет']
data_for_table2 = ['Ошибка', 48, ess, round(ess / 48, 4), '––', '––', '––']
data_for_table3 = ['Итог', 49, tss, round(tss / 49, 4), '--', '--', '--']

print(tabulate([data_for_table1, data_for_table2, data_for_table3],
                  headers=headers, tablefmt='pretty'), '\n\n')

x_prognoz = 240
y_dot_analys = tata0 + tata1 * x_prognoz
mark_std_error = round(std_people * np.sqrt(((1 / 50) + ((x_prognoz - average_people) ** 2 / sum_xi_people)))[0], 4)
x = sm.add_constant(people2, prepend=True)
regression = sm.OLS(sum_tomato2, x).fit()
error = regression.bse

print(error[0], error[1], '\n')


print(mark_std_error, '\n') # РАССЧИТАТЬ ИНТЕРВАЛ, КОГДА УЗНАЮ ПРО КРИТИЧЕСКОЕ СТЬЮДЕНТА!!!

dover_interval = st.norm.interval(confidence=0.95, loc=np.mean(people2), scale=st.sem(people2))
gran1 = round(y_dot_analys - t_student_krit * mark_std_error, 3)
gran2 = round(y_dot_analys + t_student_krit * mark_std_error, 3)

print(gran1, gran2, sep='; ')
print(dover_interval)

""" plt.scatter(people2, sum_tomato, c='r', alpha=0.5)
plt.plot(people2, model1.predict(people2), c='b', linewidth=3)
plt.scatter(800, 30, color='green') # ЗАТЫК!!!
plt.xlabel('Покупатели')
plt.ylabel('Томаты')
plt.show() """
