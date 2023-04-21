import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 50

ROWS = 3
COLS = 3
symbol_count = {
    "★" : 2,
    "✈" : 4,
    "☎" : 6,
    "￥" : 18
}

symbol_value = {
    "★" : 5,
    "✈" : 4,
    "☎" : 3,
    "￥" : 2
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i != len(columns)-1:
                print(col[row],end = " | ")
            else:
                print(col[row],end = "")
        print()

def deposit():
    while True:
        amount = input("What is the deposit ? Rs.")
        if(amount.isdigit()):
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("Enter a fucking number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the lines between (1-" + str(MAX_LINES) + ")? ")
        if(lines.isdigit()):
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("Lines should be in the given range.")
        else:
            print("Enter a fucking number.")
    return lines

def get_bet():
    while True:
        betamount = input("What is the bet on each line ? Rs.")
        if(betamount.isdigit()):
            betamount = int(betamount)
            if MIN_BET <= betamount <= MAX_BET:
                break
            else:
                print(f"BetAmount should be in between Rs{MIN_BET} - Rs{MAX_BET}.")
        else:
            print("Enter a fucking number.")
    return betamount
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet() 
        total_bet = bet * lines
        if(total_bet > balance):
            print(f"You are a broke mf, your balance is only Rs{balance}")
        else:
            break
    print(f"You are betting Rs{bet} on {lines} lines. Total bet is equal to: Rs{total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won Rs{winnings}.")
    print(f"You won on", *winning_lines)
    return winnings - total_bet
    
def main():
    balance = deposit()
    while True:
        print(f"Your balance is Rs{balance}")
        ans = input("Press Enter to play or q to quit.")
        if(ans == "q"):
            break
        balance += spin(balance)
    print(f"You are left with Rs{balance}")
    
main()
