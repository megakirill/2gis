import openpyxl

file = open('admin_level_4.txt', 'r', encoding='utf-8')
text = file.read()
text2 = file.read()


lastmas = []
mass = text.split('{"id":')
mass2 = mass

mass.pop(0)
for i in mass:
    mass[mass.index(i)] = i.split('"coordinates":[[')

for i in mass:
    lastmas.append(i[1])

for i in range(len(lastmas) - 1):
    lastmas[i] = lastmas[i][:-7]
lastmas[len(lastmas) - 1] = lastmas[len(lastmas) - 1][:-7]             #.replace(lastmas[i], ']]}}')


mass1 = []
mass1 = text.split(':"Feature","name":"')
lastmas1 = []

mass1.pop(0)

for i in range(len(mass1)):
    mass1[i] = mass1[i].split('","properties":{')

for i in mass1:
    lastmas1.append(i[0])
print(lastmas1)


if __name__ == '__main__':
    am = {}
    for i in range(len(lastmas)):
        am[lastmas1[i]] = lastmas[i]

