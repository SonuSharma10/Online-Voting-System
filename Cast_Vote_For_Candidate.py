import tkinter as tk
from tkinter import messagebox

# Function to handle the submit button click
def submit_vote():
  global voted
  if voted:
    messagebox.showinfo("Info", "You already voted once.")
  elif cast_vote.get() == "":
    output_label.config(text=f"Your vote is registered for: NOTA")
    messagebox.showerror(
        "Error",
        "Due to NO vote or system timeout your vote is registered as NOTA.")
  else:
    voted = True
    output_label.config(text=f"You voted for: {cast_vote.get()}")


# Initialize the tkinter window
root = tk.Tk()
root.title("Election Voting")

# Set the window size to 500x500
root.geometry("500x300")

# Initialize a StringVar to store the selected vote
cast_vote = tk.StringVar()

# Create a label to display the dropdown menu
label = tk.Label(root, text="Select a party to vote:")
label.pack(pady=20)

# Create the dropdown menu
party_options = ["BJP", "AAP", "CONGRESS", "MANSE", "NOTA"]
cast_vote.set("")  # Set default value to an empty string
dropdown = tk.OptionMenu(root, cast_vote, *party_options)
dropdown.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit Vote", command=submit_vote)
submit_button.pack(pady=20)

# Create a label to display the output
output_label = tk.Label(root, text="", font=("Helvetica", 16))
output_label.pack()

# Initialize a flag to track if the user has already voted
voted = False

# Start the tkinter main loop
root.mainloop()

