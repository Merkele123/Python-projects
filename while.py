# Program 1: Prints "hello" n times
n = int(input())  # Requests an integer from the user and stores it in `n`
i = 1  # Initializes a counter variable `i` with a value of 1

while i <= n:  # Loop runs as long as `i` is less than or equal to `n`
    print("hello")  # Prints "hello"
    i = i + 1  # Increments `i` by 1 in each iteration


# Program 2: Prints numbers from 20 to 1, decreasing by 2
i = 20  # Sets variable `i` to 20

while i >= 1:  # Loop continues as long as `i` is greater than or equal to 1
    print(i)  # Prints the current value of `i`
    i = i - 2  # Decreases `i` by 2 in each iteration


# Program 3: Asks the user for input until they enter 0
a = int(input())  # Requests an integer from the user and stores it in `a`

while a != 0:  # Loop runs as long as `a` is not equal to 0
    print("Another digit:")  # Asks for another number
    a = int(input())  # Requests a new number


# Program 4: Asks for a password and keeps prompting until the correct one is entered
guess = input()  # Requests a string input from the user
password = "QWERTY"  # Sets the correct password

while guess != password:  # Loop continues until `guess` matches `password`
    print("Another try:")  # Asks the user to try again
    guess = input()  # Requests new input

print("Welcome in")  # Prints welcome message when the correct password is entered


# Program 5: Same as above but counts the number of attempts
guess = input()  # Requests a string input from the user
password = "QWERTY"  # Sets the correct password
count = 1  # Initializes attempt counter

while guess != password:  # Loop continues until `guess` matches `password`
    print("Another try:")  # Prompts user to retry
    count = count + 1  # Increments attempt counter
    guess = input()  # Requests new input

print(f"Welcome in, you tried to get in {count} times")  # Prints attempt count when successful


# Program 6: Creates a repeated list and removes all occurrences of 3
a = [1, 2, 3] * 5  # Creates a list repeating [1, 2, 3] five times
print(a)  # Prints the list

while 3 in a:  # Loop continues while 3 is present in the list
    a.remove(3)  # Removes the first occurrence of 3
    print(a)  # Prints updated list after each removal


# Program 7: Removes characters from a string one by one
s = "hello"  # Defines a string `s`

while len(s) > 0:  # Loop runs as long as the string has characters
    print(s[0], s[1:])  # Prints the first character and the rest of the string
    s = s[1:]  # Removes the first character from `s`


# Program 8: Categorizes characters in a string as uppercase, lowercase, digits, or symbols
s = "%&/rfgDRDC49puf4823g"  # Defines a string with mixed characters

while len(s) > 0:  # Loop runs as long as the string has characters
    letter = s[0]  # Extracts the first character

    if "a" <= letter <= "z":  # Checks if it's a lowercase letter
        print(letter, "small")
    elif "A" <= letter <= "Z":  # Checks if it's an uppercase letter
        print(letter, "big")
    elif letter.isdigit():  # Checks if it's a digit
        print(letter, "digit")
    else:  # If it's not a letter or digit, it must be a symbol
        print(letter, "is symbol")

    s = s[1:]  # Removes the first character from `s`


# Program 9: Analyzes the digits of an input number
x = int(input())  # Requests an integer from the user

amount = 0  # Counter for total digits
amount2 = 0  # Counter for even digits
s = 0  # Sum of all digits
mul = 1  # Product of all digits
max_digit = 0  # Maximum digit
min_digit = 9  # Minimum digit

while x > 0:  # Loop runs as long as `x` is greater than 0
    last = x % 10  # Extracts the last digit
    amount += 1  # Increments total digit count

    if last % 2 == 0:  # Checks if the digit is even
        amount2 += 1  # Increments even digit count

    s += last  # Adds the digit to the sum
    mul *= last  # Multiplies the digit to the product

    if last > max_digit:  # Checks if the digit is the largest found
        max_digit = last

    if last < min_digit:  # Checks if the digit is the smallest found
        min_digit = last

    x = x // 10  # Removes the last digit from `x`

# Prints the results
print(f"Total digit amount: {amount}")
print(f"Total even digits: {amount2}")
print(f"Sum of all digits: {s}")
print(f"Product of all digits: {mul}")
print(f"Max digit: {max_digit}")
print(f"Min digit: {min_digit}")


# Program 10: Prints the remainder when a number is divided by 5 repeatedly
x = int(input())  # Requests an integer from the user

while x > 0:  # Loop continues while `x` is greater than 0
    last = x % 5  # Finds the remainder when `x` is divided by 5
    print(last)  # Prints the remainder
    x = x // 5  # Removes the last "base-5 digit" from `x`


# Program 11: Finds the greatest common divisor (GCD) using subtraction
a = int(input())  # Requests the first number
b = int(input())  # Requests the second number

while a != b:  # Loop continues until `a` equals `b`
    if a > b:  # If `a` is greater, subtract `b` from `a`
        a = a - b
    else:  # If `b` is greater, subtract `a` from `b`
        b = b - a

print(a)  # Prints the greatest common divisor (GCD)


# Program 12: Finds the greatest common divisor (GCD) using the Euclidean algorithm
a, b = map(int, input().split())  # Requests two space-separated integers from the user

while b > 0:  # Loop continues while `b` is greater than 0
    a, b = b, a % b  # Replaces `a` with `b`, and `b` with `a % b`

print(a)  # Prints the greatest common divisor (GCD)
