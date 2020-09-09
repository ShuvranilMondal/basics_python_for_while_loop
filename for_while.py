# ................................while loop......................

name = input("Enter your name : ")
number = int(input("how many times you want to print? : "))
i = 1
while i <= number:
    print(F"{name}{[i]}")
    i += 1


#input:  enter your name = nil
#        how many times you want to print = 2
# output = nil*3


n = int(input("Enter your n number : "))
total = 0
i = 1
while i <= n:                  
    total += i                          # 1 + 2 + 3 ....+n = ans 
    i += 1
    print(total)

# # input = 10
# output = 55


n = int(input("Enter your n number : "))
total = 0
i = 1
while i <= n:                  
    total += i*i                         # 1^2 + 2^2 + 3^2 ....+n^2 = ans 
    i += 1
    print(total)

# input = 2
# opuput = 5


number = input("Enter your number : ")
num = number.strip()
total = 0
i = 0
while i < len(num):
    total += int(num[i])           # 123 = 1+2+3 = ans
    i += 1 
    print(total)

# input = 123
# output = 6


nam = input("Enter your name : ")
i = 0
temp = ""
while i < len(nam):
    if nam[i]  not in temp:
        temp += nam[i]
        print(F"{nam[i]} : {nam.count(nam[i])}")
    i += 1


# input = Not
# input = N : 1
#         o : 1
#         t : 1

#...................................... for loop..................................


name = input("Enter your name :")
number = int(input("enter number :"))
for i in range(0,number):
    print(name)
    i += 1


number = int(input("Enter your number : "))
total = 0
for i in range(1,number+1):
    total += i
    print(total)
    


number = input("Enter your number :")
total = 0
for i in range(len(number)):
    total += int(number[i])
    print(total)


name = input("Enter your name : ")
temp = " "
for i in range(len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(F"{name[i]} : {name.count(name[i])}")


name = input("Enter :")
for i in range(len(name)):
    print(name[i])



        