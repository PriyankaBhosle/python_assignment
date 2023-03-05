# write a python program to count the number of even & odd number from the series of number

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_even = 0
count_odd = 0
for i in num:
    if not i % 2:
        count_even+=1

    else:
        count_odd+=1

print("count of even numbers:", count_even)
print("count of odd numbers:", count_odd)