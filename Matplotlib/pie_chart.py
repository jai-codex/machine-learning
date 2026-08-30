import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [40, 35, 25]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")

plt.title("Marks Distribution")

plt.show()