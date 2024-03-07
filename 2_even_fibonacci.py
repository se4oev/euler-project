import datetime

# моё топорное решение
limit = 4000000
sum = 0
prev = 1
current = 1
print(prev)
start = datetime.datetime.now()
while current < limit:
    if (current % 2 == 0):
        sum += current
    temp = current
    current = current + prev
    prev = temp

finish = datetime.datetime.now()
print(sum)
print("Estimated time: ", str(finish - start))

# решение с projecteuler.net
# используем свойство, что только каждый третий элемент четный, поэтому обрабатываем пачками по 3
sum = 0
prev = 1
current = 1
next = prev + current
start = datetime.datetime.now()
while current < limit:
    sum = sum + next
    prev = current + next
    current = next + prev
    next = prev + current
finish = datetime.datetime.now()
print(sum)
print("Estimated time: ", str(finish - start))

# там же предлагается решить третьим способом
# исходя из свойства, что четные числа фибоначи 2 8 34 144 формируются по формуле:
# F(n) = F(n - 1) * 4 + F(n - 2)

# TODO: