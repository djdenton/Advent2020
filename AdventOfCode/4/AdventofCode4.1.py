import csv

with open('input.txt', 'r') as batchFile:
    passport = ''
    passports = []

    for line in batchFile:
        if line == '\n':
            passports.append(passport.strip())
            passport = ''
        else: 
            passport = passport + ' ' + line.strip()

    passports.append(passport.strip()) #append the last line
    passports = [x.replace(" ","','").replace(":","':'") for x in passports] #Remove empty rows
    passports = [eval(f"{{'{x}'}}") for x in passports] # Convert strings to dictionaries

    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    valid = 0
    for passport in passports:
        if set(required).issubset(passport):
            valid += 1
    print (valid)
