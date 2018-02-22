score = int(input("Your score: "))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print("%d belong to %s"%(score,grade))
