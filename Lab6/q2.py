from random import choices, uniform, randint
import csv

size = 80
matrix = [[0]*size for x in range(size)]
deg = [4]

cnt = 0
for r in range(len(matrix)):
  for _ in range(choices(deg)[0]):
    cnt += 1
    sel = randint(0, size-1)
    matrix[r][sel] = 1
    matrix[sel][r] = 1
print(f"Connected {cnt}/{size*size}")

with open(f"q2-matrix.csv","w", newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerow([x for x in range(0, len(matrix)+1)])
    for index, row in enumerate(matrix):
        csvWriter.writerow([index+1] + row)
