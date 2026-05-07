# 1. Check if number is between 1 and 100
print("--- Program 1 ---")
num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print("The number is between 1 and 100.")
else:
    print("The number is NOT between 1 and 100.")


# 2. Check even or odd
print("\n--- Program 2 ---")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


# 3. Display month name from number
print("\n--- Program 3 ---")
months = {1: "January", 2: "February", 3: "March", 4: "April",
          5: "May", 6: "June", 7: "July", 8: "August",
          9: "September", 10: "October", 11: "November", 12: "December"}
num = int(input("Enter a number (1-12): "))
if num in months:
    print("Month:", months[num])
else:
    print("Error: Please enter a number between 1 and 12.")


# 4. Grading system
print("\n--- Program 4 ---")
marks = float(input("Enter your marks: "))
if marks < 25:
    print("Grade: F")
elif marks < 45:
    print("Grade: E")
elif marks < 50:
    print("Grade: D")
elif marks < 60:
    print("Grade: C")
elif marks <= 80:
    print("Grade: B")
else:
    print("Grade: A")


# 5. Check divisibility by 7
print("\n--- Program 5 ---")
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is NOT divisible by 7.")


# 6. Simple calculator
print("\n--- Program 6 ---")
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
symbol = input("Enter operator (+, -, *, /): ")
if symbol == "+":
    print("Your Answer is:", a + b)
elif symbol == "-":
    print("Your Answer is:", a - b)
elif symbol == "*":
    print("Your Answer is:", a * b)
elif symbol == "/":
    if b != 0:
        print("Your Answer is:", a / b)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")


# 7. Car loan eligibility
print("\n--- Program 7 ---")
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary >= 50000 and credit_score >= 700:
    print("Eligible")
else:
    print("Not Eligible")


# 8. FizzBuzz
print("\n--- Program 8 ---")
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)


# 9. Vowel or consonant
print("\n--- Program 9 ---")
char = input("Enter a character: ").lower()
if char in "aeiou":
    print("It is a Vowel.")
elif char.isalpha():
    print("It is a Consonant.")
else:
    print("Not a letter.")


# 10. Grade based on marks (90-100 scale)
print("\n--- Program 10 ---")
marks = float(input("Enter your marks: "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
else:
    print("Fail")


# 11. Age category
print("\n--- Program 11 ---")
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")


# 12. Uppercase, lowercase, or digit
print("\n--- Program 12 ---")
char = input("Enter a character: ")
if char.isupper():
    print("It is Uppercase.")
elif char.islower():
    print("It is Lowercase.")
elif char.isdigit():
    print("It is a Digit.")
else:
    print("It is a special character.")


# 13. Traffic light action
print("\n--- Program 13 ---")
color = input("Enter a color (Red, Yellow, Green): ")
if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Get Ready")
elif color == "Green":
    print("Go")
else:
    print("Invalid color.")


# 14. Job eligibility
print("\n--- Program 14 ---")
age = int(input("Enter your age: "))
experience = int(input("Enter years of experience: "))
if age > 18 and experience >= 2:
    print("Eligible")
else:
    print("Not Eligible")


# 15. Temperature advice
print("\n--- Program 15 ---")
temp = float(input("Enter temperature in °C: "))
if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")


# 16. Menu price
print("\n--- Program 16 ---")
item = input("Enter menu option (Pizza, Burger, Pasta): ")
if item == "Pizza":
    print("Price: $10")
elif item == "Burger":
    print("Price: $7")
elif item == "Pasta":
    print("Price: $8")
else:
    print("Item not found.")


# 17. Player selection by height
print("\n--- Program 17 ---")
height = float(input("Enter height in feet: "))
if height >= 6:
    print("Selected")
else:
    print("Not Selected")


# 18. Movie eligibility by age
print("\n--- Program 18 ---")
age = int(input("Enter your age: "))
if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")


# 19. Login credentials check
print("\n--- Program 19 ---")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")


# 20. Season from month number
print("\n--- Program 20 ---")
month = int(input("Enter month number (1-12): "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month number.")