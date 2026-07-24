
#Question 1
#Create a variable:
#age = 17 If the age is 18 or above
#Print Eligible to Vote Else Not Eligible

#Solution 1

age = 17
if age >=18 :
    print("Eligible to Vote") 
else :
    print("not eligible")

#Question 2
#marks = 45 If marks are 50 or above Print Pass 
# Else Fail

#Solution 2

marks = 45
if marks >= 50 :
    print("Pass")
else:
    print("Fail")

#Question 3 temperature = 39 If temperature is greater than 37
#Print Fever Else Normal

# Solution 3

temperature = 39
if temperature > 37:
    print("Fever")
else :
    print("Normal")


# Question 4
# Marks = 82
#
# Rules:
# 90 and above  -> Grade A
# 75 and above  -> Grade B
# 50 and above  -> Grade C
# Else          -> Fail

# Solution 4

Marks = 82

if Marks >= 90 :
    print("Grade A")
elif Marks >= 75:
    print("Grade B")
elif Marks >= 50:
    print("Grade C")
else :
    print("Fail")


# Question 5
# Salary = 65000
#
# Rules:
# 100000 and above -> Excellent
# 50000 and above  -> Good
# Else             -> Average
#
# Solution 5

Salary = 65000
if Salary >= 100000 :
    print("Excellent")
elif Salary >= 50000:
    print("Good")
else :
    print("Average")

# Question 6
# Experience = 3
#
# Rules:
# 5 years or more -> Senior Data Engineer
# 2 years or more -> Data Engineer
# Else            -> Junior Data Engineer

# Solution 6

Experience = 3
if Experience >= 5:
    print("Senior Data Engineer")
elif Experience >=2:
    print("Data Engineer")
else:
    print("Junior Data Engineer")


# Question 7
# Records = 1250
#
# Rules:
# 1000 or more -> Process in Batch Mode
# 500 or more  -> Process in Standard Mode
# Else         -> Process Manually

# Solution 7

records = 1250
if records >= 1000 :
    print("Process in Batch Mode")
elif records >= 500:
    print("Process in Standard Mode")
else:
    print("Process Manually")

# Question 8
# Data Quality Score = 91
#
# Rules:
# 95 and above -> Excellent Quality
# 80 and above -> Good Quality
# Else         -> Needs Cleaning

# Solution 8 
dqs = 91
if dqs >= 95 :
    print("Excellent quality")
elif dqs >80:
    print("Good Quality")
else:
    print("Needs Cleaning")

# Question 9
# Daily Sales = 145000
#
# Rules:
# 100000 and above -> Target Achieved
# 50000 and above  -> On Track
# Else             -> Needs Improvement

# Solution 9
daily_sales = 145000
if daily_sales >= 100000:
    print("Target achieved")
elif daily_sales >= 50000:
    print("On Track")
else:
    print("Needs Improvement")