number = [i for i in range(1, 31)]

for i in range(28):
    n = int(input())
    number.remove(n)

print(min(number))
print(max(number))