sum = 0
count = 0
num = int(input("Vvedite chislo(0 chtoby zakonchit): "))
while num != 0:
    sum += num
    count += 1
    num = int(input("Vvedite chislo(0 chtoby zakonchit): "))

print("Sum:", sum)
print("Count:", count)