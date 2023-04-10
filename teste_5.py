#Fazendo de uma forma mais manual
userInput = input("Digite algo e eu irei Inverter para você: ")

reverse_word = ""

for iteracao in range(len(userInput) - 1, -1, -1):
    reverse_word += f"{userInput[iteracao]}"

print(f"Sua palavra ao contrário ficou assim: {reverse_word}")

# Usando o técnica "slicing"
# print(f"Sua palavra ao contrário ficou assim: {userInput[::-1]}")
