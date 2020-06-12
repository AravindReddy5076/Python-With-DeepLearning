lbs = []
kgs = []
n = int(input("Enter number of students::"))
for i in range(n):
    num = int(input("Enter values:"))
    lbs.append(num)
    kilograms = num * 0.454
    kgs.append(kilograms)
print("weight of students in lbs:")
print(lbs)
print("weight of students in kgs:")
print(kgs)