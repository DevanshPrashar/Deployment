print("Docker Container Executed")
try:
    a = input("Enter your name: ")
except EOFError:
    a = "Unknown"
print("Welcome", end=" ")
print(a, end=" ")
print("in the world of Docker")
