def print_board(board):
    print(board["TopL"] + "|" + board["TopC"] + "|" + board["TopR"])
    print("-+-+-")
    print(board["MidL"] + "|" + board["MidC"] + "|" + board["MidR"])
    print("-+-+-")
    print(board["BotL"] + "|" + board["BotC"] + "|" + board["BotR"])

def check_winner(board, turn):
    win_conditions = [
        ["TopL", "TopC", "TopR"], ["MidL", "MidC", "MidR"], ["BotL", "BotC", "BotR"],
        ["TopL", "MidL", "BotL"], ["TopC", "MidC", "BotC"], ["TopR", "MidR", "BotR"],
        ["TopL", "MidC", "BotR"], ["TopR", "MidC", "BotL"]
    ]
    
    for condition in win_conditions:
        if all(board[pos] == turn for pos in condition):
            return True
    return False

def main():
    board = {
        "TopL": " ", "TopC": " ", "TopR": " ",
        "MidL": " ", "MidC": " ", "MidR": " ",
        "BotL": " ", "BotC": " ", "BotR": " "
    }

    print_board(board)
    turn = "X"

    for _ in range(9):
        choice = input(f"\n{turn}'s turn! Where do you want to place {turn}? (e.g., TopL, MidC, BotR): ")
        
        if board[choice] != " ":
            print("\nSquare occupied! Try again.")
            continue

        board[choice] = turn
        print_board(board)

        if check_winner(board, turn):
            print(f"\n{turn} wins the game! 🎉")
            return

        turn = "O" if turn == "X" else "X"

    print("\nIt's a draw!")

if __name__ == "__main__":
    main()
