# Dictionary of students
students = {1: "Amit", 2: "Priya", 3: "Rahul"}

# Search function
def search(roll):
    print("Name:", students.get(roll, "Not found"))

# Test
search(2)
search(5)
