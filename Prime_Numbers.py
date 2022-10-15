prime_range = input("Which number do you want to find the prime numbers to: ")
prime_list = []

for x in range(2, int(prime_range)+ 1):
    prime_list.append(x)
for x in prime_list:
    count = 0
    for y in prime_list:
        if y % x == 0 and y != x:
            prime_list.remove(y)
            count += 1

print(prime_list)
