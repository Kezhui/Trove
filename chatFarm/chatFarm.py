import pydirectinput
import keyboard
pydirectinput.PAUSE=0.01

def enviarTexto(texto):
        pydirectinput.press('enter')
        keyboard.write(texto)
        print(texto)
        pydirectinput.press('enter')

def definido(startingNumber,totalNumber,phrase):
    while startingNumber <= totalNumber:
        texto = f"{phrase} {startingNumber}/{totalNumber}"
        if keyboard.read_key() == '+':
            enviarTexto(texto)
            startingNumber += 1

def indefinido(startingNumber,phrase):
    while True:
        texto = f"{phrase} #{startingNumber}"
        if keyboard.read_key() == '+':
            enviarTexto(texto)
            startingNumber += 1
 
def opçao():    
    print("\n=========OPÇÕES=========")
    print("1. Definido\t1/200  2/200  3/200...")
    print("2. Indefinido\t#1  #2  #3...")
    op = int(input("\nDIGITE SUA OPÇÃO: "))
    while op !=1 and op != 2:
        op = int(input("DIGITE SUA OPÇÃO: "))
    return op

def main():
    print("=========INFORMAÇÕES=========")
    print("-> Pressione a tecla '+' para usar o programa.")
    print("-> Cada vez que apertar irá aumentar 1 na quantidade farm.")
    print("-> As quantidades do farm serão inseridas sempre no final da frase.\n")

    print("=========EXEMPLOS=========")
    print("-> Frase: Host 5* farm | U10 | ADD & JOIN |")
    print("-> Farm definido:   Host 5* farm | U10 | ADD & JOIN | 1/100")
    print("-> Farm indefinido: Host 5* farm | U10 | ADD & JOIN | #1\n")

    phrase = input("-> Digite a frase: ")

    op = opçao()

    if op == 1:
        startingNumber = int(input("\n-> Digite o número inicial do farm (geralmente 1): "))
        totalNumber = int(input("-> Digite a quantidade total do farm: "))
        print("\n-> Pressione a tecla '+' para usar o programa.")
        definido(startingNumber,totalNumber,phrase)
    elif op == 2:
        startingNumber = int(input("\n-> Digite o número inicial do farm (geralmente 1): "))
        print("\n-> Pressione a tecla '+' para usar o programa.\n")
        indefinido(startingNumber,phrase)
    
main()
