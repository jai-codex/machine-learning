def function(x):
    return x ** 2


def gradient(x):
    return 2 * x


x = 10
learning_rate = 0.1
iterations = 20

print("Starting x:", x)

for i in range(iterations):

    x = x - learning_rate * gradient(x)

    print(
        "Iteration:", i + 1,
        "| x:", round(x, 4),
        "| Function value:", round(function(x), 4)
    )

print("\nFinal x:", round(x, 4))
print("Final function value:", round(function(x), 4))
