# Marks of 3 students in 3 subjects
marks = [
    [80, 85, 90],  # Student 1
    [70, 75, 80],  # Student 2
    [60, 65, 70]   # Student 3
]

# Calculate total and average marks for each student
for i in range(3):
    total = marks[i][0] + marks[i][1] + marks[i][2]
    average = total / 3
    print("Student", i+1, "- Total:", total, "Average:", average)
