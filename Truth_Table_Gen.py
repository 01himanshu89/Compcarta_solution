def generate_basic_truth_table():
    # Define the logic gate functions
    def AND(a, b):
        return a and b

    def OR(a, b):
        return a or b

    def NOT(a):
        return not a

    def XOR(a, b):
        return a ^ b

    gates = {
        'AND': AND,
        'OR': OR,
        'NOT': NOT,
        'XOR': XOR
    }

    print("Select a logic gate to generate its truth table:")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    choice = input("Enter your choice (1-4): ")

    gate = ""
    if choice == '1':
        gate = 'AND'
    elif choice == '2':
        gate = 'OR'
    elif choice == '3':
        gate = 'NOT'
    elif choice == '4':
        gate = 'XOR'
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
generate_basic_truth_table()