import matplotlib.pyplot as plt

marks = [40, 45, 50, 52, 55, 60, 65, 70, 72, 80, 85, 90]

plt.hist(marks)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")

plt.show()