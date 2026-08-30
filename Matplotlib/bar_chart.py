import matplotlib.pyplot as plt

students = ["Rahul", "Amit", "Sneha"]
marks = [80, 90, 75]

plt.bar(students, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks")
plt.show()