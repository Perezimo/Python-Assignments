"""Pseudocode.
Prompt, enter the current age of the father
Prompt, enter the current age of the son
Father age is twice that of the age of the son
Years ago, fathers age equals minus twice the age of the son
print years ago"""

"""Comparing the ages of a father and his son"""


father_age = int(input("Enter father's current age: "))

son_age = int(input("Enter son's current age: "))

age_ago = int(father_age - 2*(son_age))

if age_ago>0:
	print(age_ago ,"years ago the father age was twice that of his son")

else:
	print("Past is not catered for")
	



