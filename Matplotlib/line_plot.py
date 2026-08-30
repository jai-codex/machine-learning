import matplotlib.pyplot as plt

tests = [1, 2, 3, 4, 5]
marks = [60, 70, 65, 80, 90]

plt.plot(tests, marks)

plt.xlabel("Test")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()