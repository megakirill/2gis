file = open('c:\\Users\\Хозяин\\PycharmProjects\\project\\main\\forpars.txt', 'r', encoding='utf-8')
text = file.read()

sp = '\n'
mass = []
last1 = [] #местность
last2 = [] #набор цифорок
dic = {}
mass = text.split(sp)

for i in range(0, len(mass)-1, 2):
    last1.append(str(mass[i]))

for i in range(1, len(mass), 2):
    last2.append(int(mass[i]))

for i in range(len(last1)):
    dic[last1[i]] = last2[i]

