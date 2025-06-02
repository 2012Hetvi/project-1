import tkinter as tk
from tkinter import messagebox, simpledialog

# Game state variables
current_player = "X"
game_over = False
board = [["" for _ in range(3)] for _ in range(3)]
scores = {"X": 0, "O": 0}

# Ask for player names
player_x = simpledialog.askstring("Player X", "Enter name for Player X:")
player_o = simpledialog.askstring("Player O", "Enter name for Player O:")

if not player_x: player_x = "Player X"
if not player_o: player_o = "Player O"

def update_status():
    status_label.config(text=f"{player_x if current_player == 'X' else player_o}'s turn ({current_player})")

def on_click(button, row, col):
    global current_player, game_over
    if button["text"] == "" and not game_over:
        button["text"] = current_player
        board[row][col] = current_player
        if check_winner(current_player):
            highlight_winner(current_player)
            messagebox.showinfo("Game Over", f"{player_x if current_player == 'X' else player_o} wins!")
            scores[current_player] += 1
            update_score()
            game_over = True
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
            update_status()

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return [(i, j) for j in range(3)]
        if all(board[j][i] == player for j in range(3)):
            return [(j, i) for j in range(3)]
    if all(board[i][i] == player for i in range(3)):
        return [(i, i) for i in range(3)]
    if all(board[i][2 - i] == player for i in range(3)):
        return [(i, 2 - i) for i in range(3)]
    return None

def highlight_winner(player):
    cells = check_winner(player)
    if cells:
        for (i, j) in cells:
            buttons[i][j].config(bg="lightgreen")

def is_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def reset_game():
    global current_player, board, game_over
    current_player = "X"
    game_over = False
    board = [["" for _ in range(3)] for _ in range(3)]
    update_status()
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="SystemButtonFace")

def update_score():
    score_label.config(text=f"{player_x} (X): {scores['X']} | {player_o} (O): {scores['O']}")

# GUI Setup
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]

# Grid buttons
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=('Arial', 32), width=5, height=2,
                           command=lambda r=i, c=j: on_click(buttons[r][c], r, c))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Status and controls
status_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
status_label.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(root, text="", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3)

reset_btn = tk.Button(root, text="Reset Game", font=('Arial', 14), bg='orange', command=reset_game)
reset_btn.grid(row=5, column=0, columnspan=3, pady=10)

# Initialize
update_score()
update_status()

root.mainloop()
