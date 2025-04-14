#Question 2:
number = 0

while number < 50:
    try:
        number = number + 1
        print("Number = ", number, ".  Continuing to count to 50.\n")
        continue
    finally:
        if number >= 50:
            print ("Number = ", number, ".  Counting has ended\n" )
            exit
            
#Question 3:


for int2 in range (20):
    print("Current number is:", int2 + 1, "Still going...\ncl")
    continue

print("Count has reached: ", int2 + 1, "Counting has concluded.\n")
exit

#Question 4:
import random

random_integer = random.randint(1, 15)
print("\n>>>Computer is generating a random integer!>>>")
print(f"Random integer between 1 and 15: {random_integer}\n")
    

#Question 5:
for i in range(1, 11):  # 1 through 10 inclusive
    print("Current number + 5 is: ", i + 5)
    
#Question 6:
word1 = "Ready, "
word2 = "Set, "
word3 = "Go!"

print(f"{word1}{word2}{word3}")

#Question 7:
print("You will be asked to enter two random numbers below, the cannot be the same number as the other")

firstNum = float(input("Enter your first number: "))
secondNum = float(input("Enter your second number: "))

if firstNum > secondNum:
    print("Frist!")
else:
    print("Second!")
    
#Question 8:
sentence = "There is no way a bee should be able to fly."

print(sentence[:15])

#Question 9:

num1 = 50
num2 = 2
result = 0
def newMath(num1, num2):
    multiplication = num1 * num2
    return multiplication

result = newMath(num1, num2)
print(result)

#Question 10:
apples = 0.50
oranges = 0.75
bananas = 0.25

def priceCheck(apples, oranges, bananas):
    try:
        choice = input("Check to see how much apples, oranges, or bananas are.\nEnter the name of the fruit you want to check (apples, oranges, or bananas): ").strip().lower()
        
        if choice == "apples":
            return f"Apples cost ${apples:.2f} each."
        elif choice == "oranges":
            return f"Oranges cost ${oranges:.2f} each."
        elif choice == "bananas":
            return f"Bananas cost ${bananas:.2f} each."
        else:
            raise ValueError
    except ValueError:
        return "Please enter either apples, oranges, or bananas only."

print(priceCheck(apples, oranges, bananas))
