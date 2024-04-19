
import pickle
import time

import simuladores.simuladorScanner as simSCAN

#Diego Franco - 20240 prueba
def WS():
	print('WHITESPACE')

def INTEGER():
	print("ENTEROS")

def FLOAT():
	print("DECIMALES")

def IF():
	print("IF")

def FOR():
	print("FOR")

def IDENTIFICADOR():
	print("IDENTIFICADOR")

def CADENAS():
	print("CADENA DE CARACTERES")

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

#Diego Franco - 20240}