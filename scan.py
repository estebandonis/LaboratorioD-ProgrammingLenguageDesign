import pickle

def main():
    print("scan.py: main()")

    DFAMin = {}
    # Load the data
    with open("DFAMin.pickle", "rb") as f:
        DFAMin = pickle.load(f)
    
    for key in DFAMin:
        print("\n\n\n",key, ": \n")
        if type(DFAMin[key]) == list:
            for item in DFAMin[key]:    
                print(item)
        else:
            print(DFAMin[key])

if __name__ == "__main__":
    main()