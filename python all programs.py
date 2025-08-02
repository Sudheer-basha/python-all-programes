#  ----------------- Pyhton All-in-One Code -----------------
 1. Basic Syntax & Variables
name = "Sudheer"
age = 23
print("Name:", name)
print("Age:", age)

# 2. Data Types
x = 10                # int
pi = 3.14             # float
is_active = True      # boolean
message = "Hello"     # string
data = None           # NoneType

# 3. Type Conversion
a = int("5")
b = float("3.5")
c = str(123)

# 4. Operators
a, b = 10, 3
print("Sum:", a + b)
print("Greater:", a > b)
print("Not Equal:", a != b)

# 5. Input/Output
# name = input("Enter your name: ")  # Uncomment to use
# print("Welcome", name)

# 6. Conditional Statements
num = 5
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 7. Loops
for i in range(3):
    print("For Loop:", i)

i = 0
while i < 3:
    print("While Loop:", i)
    i += 1

# 8. Functions
def greet(name):
    return "Hello " + name
print(greet("Sudheer"))

# 9. List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Fruit at index 1:", fruits[1])

# 10. Tuple
point = (10, 20)
print("X-coordinate:", point[0])

# 11. Set
colors = {"red", "blue", "green"}
colors.add("yellow")
print("Colors:", colors)

# 12. Dictionary
student = {"name": "Sudheer", "age": 23}
print("Student name:", student["name"])

# 13. List Comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# 14. String Methods
text = " Hello Python "
print("Formatted:", text.strip().upper())

# 15. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# 16. File Handling
with open("sample.txt", "w") as f:
    f.write("This is a test file\n")

# 17. Class & Object (OOP)
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student:", self.name)

s = Student("Sudheer")
s.show()

# 18. Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()

# 19. Modules
import math
print("Square Root of 16:", math.sqrt(16))

# 20. Lambda Function
add = lambda x, y: x + y
print("Lambda Add:", add(5, 3))



NUMPY FULL SUBTOPICS:-
# ----------------- NumPy All-in-One Code -----------------
import numpy as np

# 1. Creating Arrays
arr1d = np.array([1, 2, 3])
arr2d = np.array([[1, 2], [3, 4]])
print("1D Array:", arr1d)
print("2D Array:\n", arr2d)

# 2. Array Properties
print("Shape:", arr2d.shape)
print("Size:", arr2d.size)
print("Dimensions:", arr2d.ndim)
print("Data type:", arr2d.dtype)

# 3. Special Arrays
print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((3, 3)))
print("Identity:\n", np.eye(3))
print("Full of 7s:\n", np.full((2, 2), 7))

# 4. Range Arrays
print("Arange (0 to 10 step 2):", np.arange(0, 10, 2))
print("Linspace (5 values from 0 to 1):", np.linspace(0, 1, 5))

# 5. Reshape Arrays
a = np.array([1, 2, 3, 4, 5, 6])
reshaped = a.reshape((2, 3))
print("Reshaped 2x3 Array:\n", reshaped)

# 6. Indexing & Slicing
b = np.array([[10, 20, 30], [40, 50, 60]])
print("Element at [0][1]:", b[0][1])
print("First row:", b[0])
print("All rows, column 1 & 2:\n", b[:, 1:])

# 7. Mathematical Operations
arr = np.array([1, 2, 3])
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Square:", arr**2)

# 8. Aggregate Functions
a = np.array([[1, 2], [3, 4]])
print("Sum:", a.sum())
print("Max:", a.max())
print("Min:", a.min())
print("Mean:", a.mean())
print("Std Dev:", a.std())

# 9. Comparison & Filtering
arr = np.array([5, 10, 15, 20])
print("Greater than 10:", arr > 10)
print("Filtered (arr > 10):", arr[arr > 10])

# 10. Random Arrays
print("Random Values (0–1):\n", np.random.rand(2, 2))
print("Random Integers (1–9):\n", np.random.randint(1, 10, (2, 3)))

# 11. Copy vs View
x = np.array([1, 2, 3])
y = x.copy()  # copy creates new memory
y[0] = 100
print("Original x:", x)
print("Copied y:", y)

# 12. Stacking Arrays
a = np.array([1, 2])
b = np.array([3, 4])
print("Vertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:", np.hstack((a, b)))

# 13. Broadcasting
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
print("Broadcasted Add:\n", a + b)

# ----------------- Pandas All-in-One Code -----------------
import pandas as pd

# 1. Create a Series
data = [10, 20, 30]
s = pd.Series(data, index=["a", "b", "c"])
print("Series:\n", s)

# 2. Create a DataFrame
df = pd.DataFrame({
    "Name": ["Sudheer", "Ravi", "Priya"],
    "Age": [23, 25, 22],
    "Marks": [90, 85, 95]
})
print("\nDataFrame:\n", df)

# 3. Read CSV (simulate by creating from dict for now)
# df = pd.read_csv("data.csv")  # Uncomment if you have a file

# 4. Display Top & Bottom Rows
print("\nHead:\n", df.head())
print("Tail:\n", df.tail())

# 5. Info and Description
print("\nInfo:")
df.info()

print("\nDescribe:\n", df.describe())

# 6. Column Selection
print("\nNames Column:\n", df["Name"])

# 7. Row Selection (iloc and loc)
print("\nRow by Index (iloc[0]):\n", df.iloc[0])
print("\nRow by Label (loc[0]):\n", df.loc[0])

# 8. Filtering Data
print("\nMarks > 90:\n", df[df["Marks"] > 90])

# 9. Sorting
print("\nSort by Marks Descending:\n", df.sort_values(by="Marks", ascending=False))

# 10. Adding New Column
df["Grade"] = ["A", "B", "A"]
print("\nWith Grade Column:\n", df)

# 11. Updating Values
df.at[1, "Marks"] = 88
print("\nUpdated Marks for Ravi:\n", df)

# 12. Deleting Column
df = df.drop("Grade", axis=1)
print("\nAfter Dropping 'Grade' Column:\n", df)

# 13. Missing Data
df.loc[3] = ["Anu", None, 80]  # Add row with missing Age
print("\nWith Missing Value:\n", df)

print("Check for Null:\n", df.isnull())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\nAfter Filling Missing Age:\n", df)

# 14. Grouping
group_df = df.groupby("Marks")["Age"].mean()
print("\nGroup by Marks - Average Age:\n", group_df)

# 15. Export to CSV (optional)
# df.to_csv("updated_data.csv", index=False)

# ----------------- Matplotlib All-in-One Code -----------------
import matplotlib.pyplot as plt

# 1. Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, color='blue', marker='o', label='Line')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart
names = ['Sudheer', 'Ravi', 'Priya']
marks = [90, 85, 95]
plt.bar(names, marks, color='green')
plt.title("Marks of Students")
plt.ylabel("Marks")
plt.show()

# 3. Horizontal Bar Chart
plt.barh(names, marks, color='orange')
plt.title("Horizontal Bar Chart")
plt.xlabel("Marks")
plt.show()

# 4. Pie Chart
sizes = [30, 40, 30]
labels = ['Math', 'Science', 'English']
colors = ['red', 'blue', 'yellow']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Subject Distribution")
plt.axis('equal')  # Equal aspect ratio ensures pie is a circle.
plt.show()

# 5. Histogram
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple')
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 6. Scatter Plot
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 7. Multiple Lines in One Plot
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]
plt.plot(x, y1, label='Ascending', marker='o')
plt.plot(x, y2, label='Descending', marker='x')
plt.title("Multiple Lines Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()



