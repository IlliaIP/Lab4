import texttable as tt
import numpy as np

def culc(count, imp, ex_1, ex_2, ex_3, ex_4, i_e):
    list_ = []
    for i in range(0, len(count)):
        list_.append(imp[i_e] * sum([ex_1[i][i_e],ex_2[i][i_e],ex_3[i][i_e],ex_4[i][i_e]]))
    return list_

expert_1 = np.loadtxt("ex 1.txt", dtype=int)
expert_2 = np.loadtxt("ex 2.txt", dtype=int)
expert_3 = np.loadtxt("ex 3.txt", dtype=int)
expert_4 = np.loadtxt("ex 4.txt", dtype=int)

importance = []
with open('importance.txt', 'r') as file:
    data_importance = file.read().split()
    for elem in data_importance:
        try:
            importance.append(float(elem))
        except ValueError:
            pass

countries = []
with open('countries.txt', 'r') as file:
    for line in file:
        countries.append(line[:-1])
file.close()        

criterion = []
with open('criterian.txt', 'r', encoding="utf-8") as file:
    for line in file:
        criterion.append(line[:-1])
file.close()        

Cuisine = culc(countries, importance, expert_1, expert_2, expert_3, expert_4, 0)
Climate = culc(countries, importance, expert_1, expert_2, expert_3, expert_4, 1)
Fashion = culc(countries, importance, expert_1, expert_2, expert_3, expert_4, 2)
Music = culc(countries, importance, expert_1, expert_2, expert_3, expert_4, 3)
Language = culc(countries, importance, expert_1, expert_2, expert_3, expert_4, 4)
Attraction = culc(countries, importance, expert_1, expert_2, expert_3, expert_4, 5)
Culture = culc(countries, importance, expert_1, expert_2, expert_3, expert_4, 6)

All = [Cuisine, Climate, Fashion, Music, Language, Attraction, Culture]

Sum = [sum(x) for x in zip(*All)]

table = tt.Texttable()
data = [[]]
i = 0
for i in range(0, len(criterion)):
    data.append([i + 1, criterion[i], importance[i], All[i][0], All[i][1], All[i][2], All[i][3],
                 All[i][4], All[i][5], All[i][6], All[i][7], All[i][8]])
data.append([i + 2, 'Сума', sum(importance), Sum[0], Sum[1], Sum[2], Sum[3], Sum[4], Sum[5], Sum[6], Sum[7], Sum[8]])
table.add_rows(data)
width = [1, 10, 5]
header = ['№', 'Параметри', 'Вага']
for i in range(len(countries)):
    width.append(len(countries[i])+1)
    header.append(countries[i])
align = []
valign = []
for i in range(len(header)):
    align.append('c')
    valign.append('m')
table.set_cols_align(align)
table.set_cols_valign(valign)

table.set_cols_width(tuple(width))
table.header(header)
print(table.draw())

