import tkinter as tk
from tkinter import messagebox

# Function to handle the submit button click
def submit_vote():
    voter_id = voter_id_var.get()
    password = password_var.get()

    if len(voter_id) != 10 or len(password) < 8:
        messagebox.showerror("Error", "Invalid input. Check the limits.")
    else:
        voter_name = "John Doe"  # Replace with actual voter name
        vote_count = 1  # Example vote count
        past_votes = ["Party A", "Party B"]  # Example past votes
        output_message = f"Voter Name: {voter_name}\nVote Count: {vote_count}\nPast Votes: {', '.join(past_votes)}"
        messagebox.showinfo("Info", output_message)

# Initialize the tkinter window
root = tk.Tk()
root.title("Election Voting")

# Set the window size to 500x400
root.geometry("500x400")

# Create labels for Voter ID and Password
voter_id_label = tk.Label(root, text="Voter ID (10 characters):")
voter_id_label.pack(pady=20)

password_label = tk.Label(root, text="Password (8 characters or more):")
password_label.pack()

# Initialize StringVars to store the input values
voter_id_var = tk.StringVar()
password_var = tk.StringVar()

# Create entry widgets for Voter ID and Password
voter_id_entry = tk.Entry(root, textvariable=voter_id_var)
voter_id_entry.pack()

password_entry = tk.Entry(root, textvariable=password_var, show="*")  # Use 'show' to hide password characters
password_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit Vote", command=submit_vote)
submit_button.pack(pady=20)

# Start the tkinter main loop
root.mainloop()
