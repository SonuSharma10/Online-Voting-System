import tkinter as tk
from tkinter import messagebox

# Function to handle the submit button click
def submit_vote():
    selected_year = year_var.get()
    selected_party = party_var.get()

    if not selected_year:
        messagebox.showerror("Error", "Select the year, please.")
    else:
        if selected_year == "2021" or selected_year == "2022":
            result = "BJP won the election"
        else:
            result = "AAP won the election"
        messagebox.showinfo("Election Result", result)

# Initialize the tkinter window
root = tk.Tk()
root.title("Election Results")

# Set the window size to 500x400
root.geometry("500x400")

# Create labels for the dropdown menus
state_label = tk.Label(root, text="Select a State:")
state_label.pack(pady=10)

city_label = tk.Label(root, text="Select a City:")
city_label.pack()
area_label = tk.Label(root, text="Select an Area:")
area_label.pack()

year_label = tk.Label(root, text="Select a Year:")
year_label.pack()

party_label = tk.Label(root, text="Select a Political Party:")
party_label.pack()

# Initialize StringVars to store the selected values
year_var = tk.StringVar()
party_var = tk.StringVar()

# Create the dropdown menus
states = ["Maharashtra", "Delhi"]
state_var = tk.StringVar()
state_var.set(states[0])
state_dropdown = tk.OptionMenu(root, state_var, *states)
state_dropdown.pack()

cities = ["Mumbai", "Delhi"]
city_var = tk.StringVar()
city_var.set(cities[0])
city_dropdown = tk.OptionMenu(root, city_var, *cities)
city_dropdown.pack()

areas = [“ ”,"Mumbai Suburban"]
area_var = tk.StringVar()
area_var.set(areas[0])
area_dropdown = tk.OptionMenu(root, area_var, *areas)
area_dropdown.pack()

years = ["2020", "2021", "2022", "2023"]
year_var.set(years[0])
year_dropdown = tk.OptionMenu(root, year_var, *years)
year_dropdown.pack()

parties = ["ALL", "BJP", "AAP", "CONGRESS", "MANSE", "NOTA"]
party_var.set(parties[0])
party_dropdown = tk.OptionMenu(root, party_var, *parties)
party_dropdown.pack()

# Create a submit button
submit_button = tk.Button(root, text="Show Result", command=submit_vote)
submit_button.pack(pady=20)

# Start the tkinter main loop
root.mainloop()

