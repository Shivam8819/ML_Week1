# Task 1: Store marks of 3 students in 3 subjects
marks = [
    [85, 78, 92],  # Student 1
    [76, 88, 80],  # Student 2
    [90, 91, 89]   # Student 3
]

# Calculate total and average for each student
for i, student_marks in enumerate(marks, start=1):
    total = sum(student_marks)
    average = total / len(student_marks)
    print(f"Student {i}: Total = {total}, Average = {average:.2f}")
