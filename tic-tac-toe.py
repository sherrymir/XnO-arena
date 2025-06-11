import random

positions = ["TopL", "TopC", "TopR",
"MidL", "MidC", "MidR",
"BotL", "BotC", "BotR"]

table = {"TopL": " ","TopC": " ","TopR": " ",
         "MidL": " ","MidC": " ","MidR": " ",
         "BotL": " ","BotC": " ","BotR": " "}

win_conditions = [ 
    ["TopL", "TopC", "TopR"], ["MidL", "MidC", "MidR"], ["BotL", "BotC", "BotR"],
    ["TopL", "MidL", "BotL"], ["TopC", "MidC", "BotC"], ["TopR", "MidR", "BotR"],  
    ["TopL", "MidC", "BotR"], ["TopR", "MidC", "BotL"]
    ]
    

def The_Table(board):
    print(board["TopL"]+"|"+board["TopC"]+"|"+board["TopR"])
    print("-+-+-")
    print(board["MidL"]+"|"+board["MidC"]+"|"+board["MidR"])
    print("-+-+-")
    print(board["BotL"]+"|"+board["BotC"]+"|"+board["BotR"])

def Check_Winner(table: dict,turn: str) -> bool:
    global win_conditions
    for condition in win_conditions:
        if all(table[pos] == turn for pos in condition):
            return True
    return False

def advanced_ai():
    global win_conditions
    for condition in win_conditions:
        if table[condition[0]] == "O" and table[condition[1]] == "O" and table[condition[2]] == " ":
            return condition[2]
        elif table[condition[0]] == "O" and table[condition[2]] == "O" and table[condition[1]] == " ":
            return condition[1]
        elif table[condition[1]] == "O" and table[condition[2]] == "O" and table[condition[0]] == " ":
            return condition[0]
    return None

def computer_move() -> str:
    global positions
    while True:
        random.shuffle(positions)
        random_move = random.choice(positions)
        if table[random_move] != " ":
            continue
        if table[random_move] == " ":
            return random_move
    return None

def Main():
    
    The_Table(table)
    turn = "X"

    while " " in table.values(): 
        if turn == "X":
            choice = input(f"Where do you wanna put {turn} e.g(TopL,MidC,BotR): ")

            if choice not in table:
                print("Please enter the Valid position.")
                continue

            if table[choice] != " ":
                print("The square is already occupied.")
                continue

            table[choice] = turn
            The_Table(table)
            print()

            if Check_Winner(table,turn):
                print(f"\n{turn} is the winner!")
                return
            
            print("Computer's turn".center(50,"-"))

        if turn == "O":
            ai = advanced_ai()
            if not ai:
                ai = computer_move()
            if ai:
                table[ai] = turn
                The_Table(table)
                
                if Check_Winner(table,turn):
                    print(f"\n{turn} is the winner!")
                    return


        if turn == "X":
            turn = "O"
        else:
            turn  = "X"

    print("\nIts a draw")

if __name__ == "__main__":
    Main()
