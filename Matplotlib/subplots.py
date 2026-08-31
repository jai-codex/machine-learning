import matplotlib.pyplot as plt

students = ["Rahul", "Amit", "Sneha"]
marks = [80, 90, 75]

plt.subplot(1, 2, 1)
plt.plot(students, marks)
plt.title("Line Chart")

plt.subplot(1, 2, 2)
plt.bar(students, marks)
plt.title("Bar Chart")

plt.show()