numbers = []
x = 0
n = int(input('enter the length of array'))
for i in range(n):
    x = input('enter next no')
    numbers.append(x)

# print(numbers)
numbers.sort()
# print(numbers)

z = 0
k = 0
a = 0

total = []

for number in numbers:
    z = z + int(number)
    k = k+1

# print(z)
# print(k)
mean = z/k
print(f'mean = {mean}')
# h = 0
# g = 0
# if k % 2 != 0:
median = numbers[int(k/2)]
print(f'median = {median}')

# elif k % 2 == 0:
   # h = int((k/2) - 1)
   # m = numbers[h]
   # g = int(k/2)
   # n = numbers[g])/2

print(f'median = {median}')

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
# print(uniques)

for no in uniques:
    a = a + 1
# print(a)

for no in uniques:
    if no in numbers:
        total.append(numbers.count(no))

# print(total)
total.sort()
total.reverse()
max = total[0]

# for ids in total:
    # if total[max+1] > total[max]:
           # max = total[max + 1]

print(f'mode = {max}')




