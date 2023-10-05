
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small = 0 
medium = 0 
large = 0

if size == 'S':
    small += 15
    if add_pepperoni == 'Y':
        small +=2
        if extra_cheese == 'Y':
            small += 1
            print(small)
    else:
        print(small)
else:
    print(small)

if size == 'M':
    medium += 20
    if add_pepperoni == 'Y':
        medium += 3
        if extra_cheese == 'Y':
            medium += 1
            print(medium)
        else:
            print(medium)
    else:
        print(medium)
else:
    print(medium)

if size == 'L':
    large += 25
    if add_pepperoni == 'Y':
        large += 3
        if extra_cheese == 'Y':
            large += 1
        else:
            print(large)
    else:
        print(large)        
else:
    print(large)