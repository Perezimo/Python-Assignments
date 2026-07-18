"""Calculating the average of three scores and assigning their grades.
Prompt, enter the first score
Prompt, enter the second score
Prompt, enter the third score
get total score, add all the scores entered
get average of scores by dividing the total scores by 3
Get average score.
If average scores is >=90 and <=100
print A and average

If average scores is >=80 and <90
print B and average score

If average scores is >=70 and <80
print C and average  score

If average scores is >=60 and <70
print D and average score

If average scores is >0 and <59
print F and average
"""


first_score = int(input("Enter the first score: "))

second_score = int(input("Enter the second score: "))

third_score = int(input("Enter the third score: "))

total_scores = int(first_score + second_score + third_score)

average_score = total_scores/ 3.

if(average_score>=90 and average_score<=100):
	print("A", average_score)

if(average_score>=80 and average_score<90):
	print("B", average_score)

if(average_score>=70 and average_score<80):
	print("C", average_score)

if(average_score>=60 and average_score<70):
	print("D", average_score)

if(average_score>=0 and average_score<59):
	print("F", average_score)

