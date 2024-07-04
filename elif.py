#elif statement
score=45
if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='F'
print(f"the score is{score},and the grade is {grade}.")
