userInput = int(input("Enter a number to create multiplication table for; "))
print("Here's the multiplication table of ", userInput, "from 1 to 12")
i = 1
while i < 13:
  print(userInput, "* ", i, "=", userInput * i)
  i += 1