# ==========================================
# Day 3 - Strings
# ==========================================

# Question 1

# Create a variable called `name`
# Store your name.
# Print the variable.

# Solution 1
name = 'Sreya'
print(name)

# Question 2

# Create a variable called `city`
# Store your city.
# Print the variable.
# Print its datatype.


# Solution 2
city = 'Chennai'
print(city)
print(type(city))


# Question 3

# Create three variables:
# company
# role
# country
#
# Store suitable string values.
# Print all three.


# Solution 3
company = "abc"
role = "data analyst"
country ="India"

print(company)
print(role)
print(country)

# ==========================================
# String Methods
# ==========================================


# Question 1

# name = "sreya reddy"
#
# Print:
# 1. Original string
# 2. Uppercase
# 3. Lowercase


# Solution 1

name = 'sreya reddy'
print(name)
print(name.upper())
print(name.lower())



# Question 2

# sentence = "python is fun"
#
# Print:
# 1. Title Case
# 2. Capitalize


# Solution 2
sentence = 'python is fun'
print(sentence.title())
print(sentence.capitalize())


# Question 3

# company = "microsoft fabric"
#
# Print:
# Original
# Uppercase
# Title Case



# Solution 3
company = 'microsoft fabric'
print(company)
print(company.upper())
print(company.title())

# ==========================================
# String Methods - Part 2
# ==========================================


# Question 4

# name = "   Sreya Reddy   "
#
# Print:
# 1. Original
# 2. After removing extra spaces



# Solution 4

name = "   Sreya Reddy   "
print(name)
print(name.strip())




# Question 5

# sentence = "I love SQL"
#
# Replace SQL with Python.
# Print the new sentence.



# Solution 5
sentence = 'i love sql'
print(sentence.replace('sql','python'))




# Question 6

# company = "Microsoft Fabric"
#
# Print:
# 1. Company name
# 2. Number of characters using len()



# Solution 6
company ='Microsoft Fabric'
print(company)
print(len(company))

# ==========================================
# String Methods - Part 3
# ==========================================


# Question 7

# name = "Sreya Reddy"
#
# Print the list obtained after splitting the name.


# Solution 7
name = "Sreya Reddy"
print(name.split())
 


# Question 8

# sentence = "I love Python"
#
# Find the position of the word "Python".
# Then find the position of "SQL".


# Solution 8
sentence = "I love Python"
print(sentence.find("Python"))
print(sentence.find("SQL"))


# Question 9

# filename = "sales_data.csv"
#
# Check whether:
# 1. The filename starts with "sales"
# 2. The filename ends with ".csv"


# Solution 9
filename = "sales_data.csv"
print(filename.startswith('sales'))
print(filename.endswith('.csv'))

# ==========================================
# Method Chaining Practice
# ==========================================

# Question 10
# customer = "   sreya reddy   "
#
# Remove extra spaces.
# Convert to title case.
# Print the result.

# Solution 10
customer = "   sreya reddy   "
print(customer.strip().title())

# Question 11
# city = "   coimbatore   "
#
# Remove spaces.
# Convert to uppercase.
# Print the result.

# Solution 11
city = "   coimbatore   "
print(city.strip().upper())


# Question 12
# email = "   sreya@gmail.com   "
#
# Remove extra spaces.
# Convert everything to lowercase.
#replace @gmail
# Print the cleaned email.

# Solution 12
email = "   sreya@gmail.com   "
print(email.strip().lower().replace('@gmail','@outlook'))