import tkinter as tk
from tkinter import messagebox

# Function to handle the submit button click
def submit_candidate():
  candidate_name = candidate_var.get()
  party_name = party_var.get()

  if candidate_name == "" or party_name == "":
    messagebox.showerror("Error", "Some fields are empty.")
  elif candidate_name in candidate_party_dict:
    if candidate_party_dict[candidate_name] == party_name:
      messagebox.showinfo(
          "Info", "Candidate already exists for this political party.")
    else:
      messagebox.showinfo("Info", "Candidate already exists.")
  else:
    candidate_party_dict[candidate_name] = party_name
    messagebox.showinfo("Info", "Candidate added successfully.")


# Initialize the tkinter window
root = tk.Tk()
root.title("Political Candidate Assignment")

# Set the window size to 500x300
root.geometry("500x300")

# Create a label for the candidate dropdown menu
candidate_label = tk.Label(root, text="Select a candidate:")
candidate_label.pack(pady=20)

# Initialize a StringVar to store the selected candidate
candidate_var = tk.StringVar()

# Create the candidate dropdown menu
candidates = [
    "Akash Chaubey", "Mayank Raj Agarwal", "Payal Zonas Agarwal",
    "Lakhan Leela Bhargav"
]
candidate_var.set("")  # Set default value to an empty string
candidate_dropdown = tk.OptionMenu(root, candidate_var, *candidates)
candidate_dropdown.pack()

# Create a label for the political party dropdown menu
party_label = tk.Label(root, text="Select a political party:")
party_label.pack()

# Initialize a StringVar to store the selected political party
party_var = tk.StringVar()

# Create the political party dropdown menu
political_parties = ["BJP", "AAP", "CONGRESS", "MANSE", "NOTA"]
party_var.set("")  # Set default value to an empty string
party_dropdown = tk.OptionMenu(root, party_var, *political_parties)
party_dropdown.pack()

# Create a submit button
submit_button = tk.Button(root,
                          text="Submit Candidate",
                          command=submit_candidate)
submit_button.pack(pady=20)

# Initialize a dictionary to store candidate-party assignments
candidate_party_dict = {}

# Start the tkinter main loop
root.mainloop()
