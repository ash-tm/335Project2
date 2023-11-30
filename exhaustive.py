import itertools

def exhaustive(items, stocks_and_values, amount):
    """ 
        The exhaustive approach to the Stock Purchase Maximization problem.
        Evaluates the number of stocks and values from all possible combinations.
        Recomputes combinations at every state.
    """
    best_candidate = []
    highest_stocks = 0
    best_value = 0

    # Generate all possible combinations given stocks_and_values
    for i in range(1, items + 1):
        combined = itertools.combinations(stocks_and_values, i) # O(nCr)

        # Checks each combination and gets the sum for stocks and values
        for candidate in combined: # o(n log n)
            num_of_stocks = sum(combination[0] for combination in candidate)
            current_value = sum(combination[1] for combination in candidate)

            # Checks to see if the candidate is a higher value than the previous
            if num_of_stocks > best_value and current_value <= amount: # O(1)
                highest_stocks = num_of_stocks
                best_candidate = candidate
                best_value = current_value
            
    return best_value, best_candidate, highest_stocks

def main():
    # Read input from file
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    i = 0
    testCaseNum = 1

    # While loop to go to next line for each variable
    while i < len(lines): # O(n)
        if lines[i] == "\n":
            i += 1

        items = int(lines[i].strip())
        stocks_and_values = eval(lines[i+1].strip())
        amount = int(lines[i+2].strip())
        i += 3
    
        best_sum, best_combination, highest_stocks = exhaustive(items, stocks_and_values, amount)
        
        # Append to an output file
        with open('exhaustive_output.txt', 'a') as f:
            f.write("Case #{}".format(testCaseNum) + '\n')
            f.write("Number of stocks: {}".format(str(highest_stocks)) + '\n')
            f.write("Best Combination: " + str(best_combination) + '\n')
            f.write("Monetary value: {}".format(str(best_sum)) + '\n\n')

        testCaseNum += 1

        # Reset
        items = 0
        stocks_and_values = []
        amount = 0

if __name__== "__main__":
    """Runs the main function"""
    main()