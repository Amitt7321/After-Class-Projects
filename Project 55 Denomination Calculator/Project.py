import random
import tkinter as tk
from tkinter import messagebox

# Initialize global tracking variables for game history and metrics
user_score = 0
computer_score = 0
tie_count = 0
round_number = 1
game_history = []


def get_computer_choice():
    """Generates a random selection for the computer opponent."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def determine_winner(player, computer):
    """Evaluates rules via conditional statements to find the winner."""
    if player == computer:
        return "Tie"

    win_conditions = {
        "Rock": "Scissors",  # Rock beats Scissors
        "Paper": "Rock",  # Paper beats Rock
        "Scissors": "Paper",  # Scissors beats Paper
    }

    if win_conditions[player] == computer:
        return "Player"
    else:
        return "Computer"


def play_round(player_choice):
    """Executes a complete single round of play and updates the UI components."""
    global user_score, computer_score, tie_count, round_number

    comp_choice = get_computer_choice()
    result = determine_winner(player_choice, comp_choice)

    if result == "Player":
        user_score += 1
        verdict_text = "🎉 You Win This Round!"
        color_theme = "lightgren"  # Emerald Green
    elif result == "Computer":
        computer_score += 1
        verdict_text = " Computer Wins This Round!"
        color_theme = "lightblue"  # Alizarin Red
    else:
        tie_count += 1
        verdict_text = "🤝 It's a Tie Round!"
        color_theme = "lightpink"  # Sun Yellow

    game_history.append(
        {
            "round": round_number,
            "player": player_choice,
            "computer": comp_choice,
            "outcome": result,
        }
    )

    round_number += 1

    lbl_choices.config(
        text=f"Your Move: {player_choice}   |   Computer's Move: {comp_choice}"
    )
    lbl_outcome.config(text=verdict_text, fg=color_theme)
    lbl_scoreboard.config(
        text=f"Score - Player: {user_score}  |  Computer: {computer_score}  |  Ties: {tie_count}"
    )


def display_history():
    """Loops over stored items to assemble log data into a pop-up window."""
    if not game_history:
        messagebox.showinfo("History Log", "No rounds played yet!")
        return

    history_window = tk.Toplevel(root)
    history_window.title("Match History Logs")
    history_window.geometry("400x300")
    history_window.configure(bg="burlywood")

    txt_area = tk.Text(
        history_window, wrap=tk.WORD, font=("Courier", 10), bg="Grey", fg="white"
    )
    txt_area.pack(fill=tk.BOTH, expand=True, padx=10, yard=10)

    log_accumulator = "--- MATCH HISTORICAL RECORD ---\n\n"
    for record in game_history:
        log_accumulator += f"Round {record['round']}: {record['player']} vs {record['computer']} -> Result: {record['outcome']}\n"

    txt_area.insert(tk.END, log_accumulator)
    txt_area.config(state=tk.DISABLED)

def reset_match():
    """Resets tracking variables and wipes out text fields back to base state."""
    global user_score, computer_score, tie_count, round_number, game_history
    user_score = 0
    computer_score = 0
    tie_count = 0
    round_number = 1
    game_history.clear()

    lbl_choices.config(text="Select an option below to initiate the match.")
    lbl_outcome.config(text="Status: Awaiting First Move", fg="#dbdbdb")
    lbl_scoreboard.config(text="Score - Player: 0  |  Computer: 0  |  Ties: 0")

root = tk.Tk()
root.title("Rock Paper Scissors Engine")
root.geometry("550x450")
root.configure(bg="burlywood")  # Dark Slate Blue Theme

lbl_title = tk.Label(
    root,
    text="ROCK, PAPER, SCISSORS",
    font=("Helvetica", 22, "bold"),
    bg="burlywood",
    fg="white",
)
lbl_title.pack(pady=20)

lbl_choices = tk.Label(
    root,
    text="Select an option below to initiate the match.",
    font=("Helvetica", 12, "italic"),
    bg="burlywood",
    fg="white",
)
lbl_choices.pack(pady=10)

lbl_outcome = tk.Label(
    root,
    text="Status: Awaiting First Move",
    font=("Helvetica", 16, "bold"),
    bg="burlywood",
    fg="white",
)
lbl_outcome.pack(pady=15)

btn_frame = tk.Frame(root, bg="burlywood")
btn_frame.pack(pady=15)

button_styles = {
    "font": ("Helvetica", 12, "bold"),
    "width": 10,
    "bd": 0,
    "cursor": "hand2",
    "activebackground": "burlywood",
    "activeforeground": "white",
}

btn_rock = tk.Button(
    btn_frame,
    text=" Rock",
    bg="white",
    fg="black",
    command=lambda: play_round("Rock"),
    **button_styles,
)
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(
    btn_frame,
    text=" Paper",
    bg="#ecf0f1",
    fg="black",
    command=lambda: play_round("Paper"),
    **button_styles,
)
btn_paper.grid(row=0, column=1, padx=10)

btn_scissors = tk.Button(
    btn_frame,
    text=" Scissors",
    bg="#3498db",
    fg="white",
    command=lambda: play_round("Scissors"),
    **button_styles,
)
btn_scissors.grid(row=0, column=2, padx=10)

lbl_scoreboard = tk.Label(
    root,
    text="Score - Player: 0  |  Computer: 0  |  Ties: 0",
    font=("Helvetica", 12, "bold"),
    bg="#34495e",
    fg="#ffffff",
    padx=15,
    pady=8,
    relief=tk.RIDGE,
)
lbl_scoreboard.pack(pady=20)

util_frame = tk.Frame(root, bg="#2c3e50")
util_frame.pack(pady=10)

btn_history = tk.Button(
    util_frame,
    text="View Logs",
    font=("Helvetica", 10),
    bg="#f39c12",
    fg="white",
    command=display_history,
)
btn_history.grid(row=0, column=0, padx=5)

btn_reset = tk.Button(
    util_frame,
    text="Reset Game",
    font=("Helvetica", 10),
    bg="#e74c3c",
    fg="white",
    command=reset_match,
)
btn_reset.grid(row=0, column=1, padx=5)

root.mainloop()