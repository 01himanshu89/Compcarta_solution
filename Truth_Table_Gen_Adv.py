def generate_advanced_truth_table():
    # Define the logic gate functions
    def AND(a, b):
        return a and b

    def OR(a, b):
        return a or b

    def NOT(a):
        return not a

    def XOR(a, b):
        return a ^ b

    def NAND(a, b):
        return not (a and b)

    def NOR(a, b):
        return not (a or b)

    def XNOR(a, b):
        return not (a ^ b)

    gates = {
        'AND': AND,
        'OR': OR,
        'NOT': NOT,
        'XOR': XOR,
        'NAND': NAND,
        'NOR': NOR,
        'XNOR': XNOR
    }

    print("Select a logic gate to generate its truth table:")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. NAND")
    print("6. NOR")
    print("7. XNOR")
    choice = input("Enter your choice (1-7): ")

    gate = ""
    if choice == '1':
        gate = 'AND'
    elif choice == '2':
        gate = 'OR'
    elif choice == '3':
        gate = 'NOT'
    elif choice == '4':
        gate = 'XOR'
    elif choice == '5':
        gate = 'NAND'
    elif choice == '6':
        gate = 'NOR'
    elif choice == '7':
        gate = 'XNOR'
    else:
        print("Invalid choice!")
        return

    print(f"\nTruth Table for {gate} gate:")
    if gate == 'NOT':
        print(" A | NOT(A)")
        print("-----------")
        for a in [0, 1]:
            result = int(gates[gate](a))
            print(f" {a} |    {result}")
    else:
        print(" A | B | {}(A,B)".format(gate))
        print("---------------")
        for a in [0, 1]:
            for b in [0, 1]:
                result = int(gates[gate](a, b))
                print(f" {a} | {b} |    {result}")

generate_advanced_truth_table()