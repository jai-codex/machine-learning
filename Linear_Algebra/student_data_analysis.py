import numpy as np

# Student data
# [Age, Study Hours, Marks]
students = np.array([
    [20, 5, 80],
    [21, 6, 90],
    [22, 4, 75]
])

print("Student Data:")
print(students)

# Shape of the matrix
print("\nMatrix Shape:", students.shape)

# Extract one student's data as a vector
student1 = students[0]
print("\nFirst Student Vector:", student1)

# Add bonus marks to all students
students[:, 2] = students[:, 2] + 5

print("\nAfter Adding 5 Bonus Marks:")
print(students)

# Matrix transpose
transpose = students.T

print("\nTranspose:")
print(transpose)

# Calculate average values
average = np.mean(students, axis=0)

print("\nAverage Age, Study Hours, Marks:")
print(average)
