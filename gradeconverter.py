#grade converter program
import os

def calculate_grade(hps, score):
    return (score / hps) * 100

while True:
    print("--Grade Converter---")
    try:
        hps = int(input("Enter the Highest Possible Score: "))
        score = int(input("Enter Score Attained: "))
    except:
        print("\nInvalid Inputs. Try Again\n")
        continue
    calculated_grade = calculate_grade(hps, score)
    print(f"You attained {calculated_grade}% grade from score {score}/{hps}")
    error = True
    choice = ""
    while error:
        choose = input("\nDo you want to convert again?(yes or no): ")
        if choose == "yes":
            print()
            error = False
            os.system('cls')
        elif choose == "no":
            print("\nExiting program Grade Converter Program")
            error = False
            choice = "no"
        else:
            print("\nSorry, I did not understand the input. Try again")
    if not error and choice == "no":
        break
close = input()