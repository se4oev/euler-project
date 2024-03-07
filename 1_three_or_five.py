import datetime

print("#### Первый вариант ####")
start = datetime.datetime.now()
sum = 8
for i in range(6, 1000000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
finish = datetime.datetime.now()
print("Сумма чисел кратных 3 или 5 в диапазоне до 1000 =", sum)
print("Estimated time: ", str(finish - start))

# Этот вариант предложен на projecteuler.net.
# Основан этот алгоритм на том, что, например в диапазоне до 1000 последним числом делящимся на 5 будет 995,
# значит числа делящиеся на 5 встретятся 995 / 5 = 199 раз. 
# Целочисленное деление даёт такой же результат без необходимости нахождения последнего делящегося числа, т.е. 999 // 5 = 199 раз.
# n * (p * (p + 1)) // 2 это формула суммы последовательности
start = datetime.datetime.now()
# числа до 1млн
target = 999999;
def sumDivisibleBy(n):
    p = target // n
    return n * (p * (p + 1)) // 2
print("#### Второй вариант ####")

print("Сумма чисел кратных 3 или 5 в диапазоне до 1000 = ", sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))
finish = datetime.datetime.now()
print("Estimated time: ", str(finish - start))