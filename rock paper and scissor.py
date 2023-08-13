# import random module
import random

print("Rules for rock paper and scissor:\n"
      "1. Rock vs paper >> Paper\n"
      "2. paper vs scissor >> scissor\n"
      "3. scissor vs rock >> rock\n")

print("Enter your choice\n"
      "1. Rock \n"
      "2. paper \n"
      "3. Scissor \n")


choice = int(input("Enter your choice:"))

if choice > 3:
    print("Give a correct choice!")

# computer generated choice using randomint
Choice_pc = random.randint(1,3)

if choice == Choice_pc:
    print("Its a tie, Play again!")
elif (choice == 1 and Choice_pc == 2):
    print("pc choose paper and won")
elif (choice == 2 and Choice_pc == 3):
    print("Pc choose scissor and won")
elif (choice ==3 and Choice_pc == 1):
    print("pc choose stone and won")
elif (choice == 2 and Choice_pc == 1):
    print("pc choose paper and won")
elif (choice == 3 and Choice_pc == 2):
    print("Pc choose scissor and won")
elif (choice ==1 and Choice_pc == 3):
    print("pc choose stone and won")


