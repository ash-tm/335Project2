# TODO: Exhaustive approach
def exhaustive(items, stocks_and_values, amount):
    pass

# TODO: Dynamic approach
def dynamic(items, stocks_and_values, amount):
    pass

def main():
    # Read input from file
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    i = 0

    # While loop to go to next line for each variable
    while i < len(lines):
        if lines[i] == "\n":
            i += 1

        items = int(lines[i].strip())
        stocks_and_values = eval(lines[i+1].strip())
        amount = int(lines[i+2].strip())
        i += 3


        # Reset
        items.clear()
        stocks_and_values.clear()
        amount.clear()

if __name__== "__main__":
    main()