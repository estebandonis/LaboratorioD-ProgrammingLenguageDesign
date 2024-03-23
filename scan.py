import pickle
import simuladorScanner as simSCAN
import time

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

    # # Remove leading spaces from each line in the string
    # code = '\n'.join(line.lstrip() for line in code.split('\n'))

    i = 0
    contador = 0

    lengthData = len(data)

    start_time = time.time()

    while i < lengthData:
        print("\ni: " + str(i))
        num, valores = simSCAN.exec(DFAMin["transitions"], DFAMin["start_states"], DFAMin["final_states"], data, i)
        print("m: " + str(num))
        print("Command: " + valores)
        try:
            exec(valores)
        except:
            print("Error al momento de ejecutar el comando")
        contador += 1
        i = num
        continue

    end_time = time.time()

    time_taken = end_time - start_time

    print(f"\nTime taken by the operation is {time_taken} seconds")

if __name__ == "__main__":
    main()
