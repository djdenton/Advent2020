import csv
with open('input.txt') as csvfile:
    passwords = list(csv.reader(csvfile))

passwords = [password[0].split(' ') for  password in passwords]
passwords = [[password[0].split('-'),password[1][0],password[2]] for  password in passwords]

x=0
for password in passwords:
    if (password[2][int(password[0][0])-1] == password[1]) is not (password[2][int(password[0][1])-1] == password[1]):
        x+=1

print (x)
