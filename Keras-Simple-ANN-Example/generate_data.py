import random 

data = ""

for x in range(10000):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    sum = num1+num2
    data += "{},{},{}\n".format(num1, num2, sum)

f = open("data.txt", "w")
f.write(data)
f.close()


