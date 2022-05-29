file = open('admin_level_8.txt', 'r', encoding='utf-8')
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

print(lastmas[0])

