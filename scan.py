import pickle
import simuladorScanner as simSCAN

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
    
    # for key in DFAMin:
    #     print("\n\n\n",key, ": \n")
    #     if type(DFAMin[key]) == list:
    #         for item in DFAMin[key]:    
    #             print(item)
    #     else:
    #         print(DFAMin[key])

    # # Execute the code

    # code = """
    # number = 1234
    # print(number)
    # """

    # print("hola")

    # # Remove leading spaces from each line in the string
    # code = '\n'.join(line.lstrip() for line in code.split('\n'))

    # exec(code)
        
    # hola 1234 + - * / ( )

    i = 0
    contador = 0

    lengthData = len(data)

    while i < lengthData:
        print("\ni: " + str(i))
        num, valores = simSCAN.exec(DFAMin["transitions"], DFAMin["start_states"], DFAMin["final_states"], data, i)
        print("Command: " + valores)
        try:
            exec(valores)
        except:
            print("Error al momento de ejecutar el comando")
        contador += 1
        i = num
        continue

if __name__ == "__main__":
    main()
