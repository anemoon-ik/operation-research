import random

R = int(input("Введите количество строк:"))
C = int(input("Введите количество столбцов:"))
  
# Построение матрицы
m = []
print("Вводите записи по строкам:")
  
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    m.append(a)

# Критерий Вальда (максимального пессимизма)
mins = []
for i in range(len(m)):
    min = [m[i][0], i, 0]
    for j in range(len(m[0])):
        if m[i][j] < min[0]:
            min = [m[i][j], i, j]
    mins.append(min)

WaldCriterion = mins[0]
for i in mins:
    if i[0] > WaldCriterion[0]:
        WaldCriterion = i
print("Критерий Вальда: " + str(WaldCriterion[0]) + " А" + str(WaldCriterion[1] + 1))

# Критерий Сейвиджа
maxs = []
for i in range(len(m[0])):
    localMax = m[0][i]
    for j in range(len(m)):
        if m[j][i] > localMax:
            localMax = m[j][i]
    maxs.append(localMax)
risksMatrix = []  # матрица рисков
for i in range(len(m)):
    localRisk = []
    for j in range(len(m[0])):
        localRisk.append(maxs[j] - m[i][j])
    risksMatrix.append(localRisk)
maxs = []
for i in range(len(risksMatrix)):
    max = [risksMatrix[i][0], i, 0]
    for j in range(len(risksMatrix[0])):
        if risksMatrix[i][j] > max[0]:
            max = [risksMatrix[i][j], i, j]
    maxs.append(max)
min = maxs[0]
for i in maxs:
    if i[0] < min[0]:
        min = i
print("Критерий Сейвиджа: " + str(min[0]) + " A" + str(min[1] + 1))

# Критерий Гурвица
a = 0.7
mins = []
for i in range(len(m)):
    min = [m[i][0], i, 0]
    for j in range(len(m[0])):
        if m[i][j] < min[0]:
            min = [m[i][j], i, j]
    mins.append(min)
maxs = []
for i in range(len(m)):
    max = [m[i][0], i, 0]
    for j in range(len(m[0])):
        if m[i][j] > max[0]:
            max = [m[i][j], i, j]
    maxs.append(max)
GurvitsResoult = []
for i in range(len(maxs)):
    GurvitsResoult.append([(maxs[i][0] * a) + (mins[i][0] * (1 - a)), maxs[i][1]])
max = GurvitsResoult[0]
for i in GurvitsResoult:
    if i[0] > max[0]:
        max = i
print("Критерий Гурвица(для α = " + str(a) + "): " + str(max[0]) + " A" + str(max[1] + 1))

# Критерий  ̶б̶а̶б̶к̶и̶ ̶г̶а̶д̶а̶л̶к̶и̶ Байеса
randMass = []  # генерируем шизу природы
rSum = 0
for i in range(len(m[0]) - 1):
    r = random.uniform(0, 1 - rSum)
    rSum += r
    randMass.append(r)
randMass.append(1 - rSum)
maxSum = [m[0][0], 0]
for i in range(len(m)):
    sum = 0
    for j in range(len(m[0])):
        sum += (m[i][j] * randMass[j])
    if sum > maxSum[0]:
        maxSum = [sum, i]
print("Критерий Байеса: " + str(maxSum[0]) + " A" + str(maxSum[1] + 1))

#Критерий максимаксма
maxs = []
for i in range(len(m)):
    max = [m[i][0], i, 0]
    for j in range(len(m[0])):
        if m[i][j] > max[0]:
            max = [m[i][j], i, j]
    maxs.append(max)

MaximaxCriterion = maxs[0]
for i in maxs:
    if i[0] > MaximaxCriterion[0]:
        MaximaxCriterion = i
print("Критерий Максимакса: " + str(MaximaxCriterion[0]) + " А" + str(MaximaxCriterion[1] + 1))

#Критерий Лапласа

for i in range(len(m[0]) - 1):
    r = len(m[0])
maxSum = [m[0][0], 0]
for i in range(len(m)):
    sum = 0
    for j in range(len(m[0])):
        sum += (m[i][j] / r)
    if sum > maxSum[0]:
        maxSum = [sum, i]
print("Критерий Лапласа: " + str(maxSum[0]) + " A" + str(maxSum[1] + 2))
