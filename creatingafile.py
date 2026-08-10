import os

print("Current directory:", os.getcwd())

text = input("Enter sample text: ")
print("You entered:", text)

with open("myfile.txt", "a") as f:
    f.write(text + "\n")

print("Saved!")