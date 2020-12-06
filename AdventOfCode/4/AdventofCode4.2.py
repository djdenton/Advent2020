import csv,re

with open('input.txt', 'r') as batchFile:
    passport = ''
    passports = []

    #Reduce each batch into one line
    for line in batchFile:
        if line == '\n':
            passports.append(passport.strip())
            passport = ''
        else: 
            passport = passport + ' ' + line.strip()
    passports.append(passport.strip()) #Append the last line
    passports = [x.replace(" ","','").replace(":","':'") for x in passports] #Remove empty rows
    passports = [eval(f"{{'{x}'}}") for x in passports] #Convert strings to dictionaries. Very hacky

#Functions for each test
def byr(field):
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return len(field) == 4 and 1920 <= int(field) <=2002

def iyr(field):
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return len(field) == 4 and 2010 <= int(field) <=2020

def eyr(field):
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return len(field) == 4 and 2020 <= int(field) <=2030

def hgt(field):
    #hgt (Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.
    dimension = field[-2:]
    number = field[:-2]
    if (dimension == 'cm' and 150 <= int(number) <= 193) or (dimension == 'in' and 59 <= int(number) <= 76):
        print (field)
    return (dimension == 'cm' and 150 <= int(number) <= 193) or (dimension == 'in' and 59 <= int(number) <= 76)
    
def hcl(field):
     #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return re.search('#[a-z0-9]{6}',field)

def ecl(field):
     #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return (field in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def pid(field):
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    return re.search('\d{9}',field)

# Create an array of values and functions
required = [['byr',byr],['iyr',iyr],['eyr',eyr],['hgt',hgt],['hcl',hcl],['ecl',ecl],['pid',pid]]

valid = 0
for passport in passports:
    if all(f[0] in passport and f[1](passport.get(f[0])) for f in required):
        valid += 1

print (valid)

