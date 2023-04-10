def is_fibo(value):
    num1, num2 = 0, 1

    while num2 < value:
        num1, num2 = num2, num1 + num2
    
    return num2 == value or value == 0

userInput = int(input("Digite um número para verificar se ele está na sequência de Fibonasci: "))

if(is_fibo(userInput)):
    print(f"{userInput} é um número da sequência de Fibonasci")
else:
    print(f"{userInput} não é um número da sequência de Fibonasci")