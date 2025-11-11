# Student Grade Calculator

marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
    message = "Excellent work"
elif marks >= 75:
    grade = "B"
    message = "Good job! Keep it up"
elif marks >= 50:
    grade = "C"
    message = "You passed! Try to improve"
else:
    grade = "F"
    message = "Don't give up! Study harder next time"

print(f"\nYour Grade: {grade}")
print(message)
