print("Personal Goals Planner")
print("----------------------")

name = input("What is your name? ")
goal = input("What is one goal you want to achieve? ")
time_frame = input("When do you want to achieve it? ")

print("\nGoal Plan")
print("Name:", name)
print("Goal:", goal)
print("Time frame:", time_frame)

print("\n", end="")
print("Keep going, ", end="")
print(name + "!")

# Ask Python to list its reserved words
import keyword
print("\nPython reserved words:")
print(keyword.kwlist)