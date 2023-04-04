import random

#Global constants that will be used throughout the program.
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Defining the number of symbols that will be used (frequency of each symbol).
symbol_count = {
    "♠": 2,
    "♣": 4,
    "♥": 6,
    "♦": 8
}

# Defining the value of each symbol that will be used.
symbol_value = {
    "♠": 5,
    "♣": 4,
    "♥": 3,
    "♦": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines
            
# Generating the output of the slot machine using RANDOM module.
def get_slot_machine_spin(rows, cols, symbols):
# Generating a list that stores the symbols
    all_symbols = []
# Loop that will iterate through our symbol dictionary
    for symbol, symbol_count in symbols.items():
# Loop that will iterate through the symbol count and add to the "all_symbols" list
        for _ in range(symbol_count):
            all_symbols.append(symbol)
# Select what values will go in every column     
    columns = []
# Generate a column for every single column that we have.(i.e. if we have 3 columns, will iterate 3 times)
    for _ in range(cols):
        column = []
# Creating a copy of the "all_symbols" list so we do not alter the original one
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
# Remove the value so we do not pick it again
            current_symbols.remove(value)
# Add that value to our column
            column.append(value)
            
        columns.append(column)
        
    return columns
    

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()

    # Colect the user input. Gets the deposit from the user.
def deposit():
    #Loop that asks the user to insert a value until they add a valid amount for the deposit.
    while True:             
        amount = input("What would you like to deposit? €")
    # Validate the input. (Digit and greater than 0.)
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a number!")
    return amount

    # Colect the user input. Get the number of lines the user will bet on.
def get_number_of_lines():
    #Loop that asks the user to insert a value until they add a valid amount for the number of lines the user will bet.
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ") ?")
    # Validate the input. (Digit and between 1 - MAX_LINES.)
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a number!")
    return lines
    
    # Colect the user input. Get the amount of money to bet.    
def get_bet():
    #Loop that asks the user to insert a value until they add a valid amount for the user to bet.
    while True:
        amount = input("What would you like to bet on each line? €")
    # Validate the input. (Digit and between MIN_BET - MAX_BET.)
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between €{MIN_BET} - €{MAX_BET}.")
        else:
            print("Enter a number!")
    return amount
    
    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money! Your current balance is: €{balance}")
        else:
            break
        
    print(f"You are betting €{bet} on {lines} lines. Total bet is equal to: €{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won €{winnings}.")
    print(f"You won on line(s): ", *winning_lines)
    return winnings - total_bet
    
 
def main(): 
    balance = deposit()
    while True:
        print(f"Current balance is €{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"Thank you for playing. You left with €{balance}")
            
    
    
main()