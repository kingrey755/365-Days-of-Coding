current=set()
numbers = []
for i in range(5):
    a = int(input())
    numbers.append(a)

for number in numbers:
    current.add(number)
print(current)
