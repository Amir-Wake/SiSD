#track of a person's ideal weight
age = input("Enter your age: ")
while (not age.isdigit()):
    age = input("Please enter a digit!" + "\n" + "Enter your age: ")

weight = input("Enter your weight: ")
while (not weight.isdigit()):
    weight = input("Please enter a digit!" + "\n" + "Enter your weight: ")

height = input("Enter your height: ")
while (not height.isdigit()):
    height = input("Please enter a digit!" + "\n" + "Enter your height: ")

ideal_weight = (int(height) - 100 + int(age) / 10) * 0.9
print("Your ideal weight is: ", ideal_weight)

if (int(weight) == ideal_weight):
    print("You have an ideal weight!")
elif (int(weight) > ideal_weight):
    print("You are overweight!")
else:
    print("You are underweight!")