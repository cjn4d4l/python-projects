numbers = [2, 4, 5, 7, 3, 6, 4]
sum = 0
for i in numbers:
    sum += i
mean = round(sum / len(numbers), 2)
print(mean)