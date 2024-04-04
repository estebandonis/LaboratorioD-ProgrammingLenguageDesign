
import pickle
import time

import simuladores.simuladorScanner as simSCAN
def ws():
	print('WHITESPACE')

def id():
	print('ID')

def number():
	print('NUMBER')

def IF():
	print('IF')

def THEN():
	print('THEN')

def ELSE():
	print('ELSE')

def n43():
	print('+')

def n45():
	print('-')

def n42():
	print('*')

def n47():
	print('/')

def n40():
	print('(')

def n41():
	print(')')


def readYalexFile(file):
    with open(file, 'r') as file:
        data = file.read()
    return data


def main():
    print("scan.py: main()")

    archivo = "string.txt"

    # Leer .txt
    data = readYalexFile(archivo)

    DFAMin = {}
    # Load the data
    with open("DFAMin.pickle", "rb") as f:
        DFAMin = pickle.load(f)

    print("Returns: ", DFAMin['returns'])

    # # Remove leading spaces from each line in the string
    # code = '\n'.join(line.lstrip() for line in code.split('\n'))

    start_time = time.time()

    readString(data, DFAMin)

    end_time = time.time()

    time_taken = end_time - start_time

    print(f"\nTime taken by the operation is {time_taken} seconds")


def readString(data, DFAMin):
    i = 0
    contador = 0

    lengthData = len(data)

    while i < lengthData:
        print("\ni: " + str(i))
        num, valores, temp, error = simSCAN.exec(DFAMin["transitions"], DFAMin["start_states"], DFAMin["returns"], data, i)
        if error:
            print(f"Valor no reconocido: '{temp}'")
            i += 1
            print("m: " + str(i))
            continue

        print("m: " + str(num))
        print("Valor: " + temp)
        print("Command: " + valores)
        print("Ejecución: ")
        try:
            exec(valores)
        except:
            print("Error al momento de ejecutar el comando")
        contador += 1
        i = num
        continue

if __name__ == "__main__":
    main()

