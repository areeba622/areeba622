age = int(input("Enter age of the person : "))
if age < 2:
    print("The person is a baby.")
elif age <= 4 and age >= 2:
    print("The person is a toddler.")
elif age <= 13 and age > 4:
    print("The person is a kid.")
elif age <= 20 and age > 13:
    print("The person is a teenager")
elif age <= 65 and age > 20:
    print("The person is an adult")
elif age > 65:
    print("The person is old")
else:
    print("Invalid input")

    
