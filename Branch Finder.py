import customtkinter
import customtkinter as ctk
import json
import tkinter as tk
from tkinter import ttk, messagebox
import re

# Load data from JSON file
def load_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

# Function to show tooltip
def show_tooltip(widget, text):
    tooltip = ctk.CTkLabel(widget, text=text, bg_color="black", text_color="white", corner_radius=5)
    tooltip.place(x=widget.winfo_rootx() + widget.winfo_width() / 2, y=widget.winfo_rooty() + widget.winfo_height(),
                  anchor="n")
    widget.tooltip = tooltip

# Function to hide tooltip
def hide_tooltip(event):
    widget = event.widget
    if hasattr(widget, 'tooltip'):
        widget.tooltip.destroy()

# Function to copy the content of the entry widget to the clipboard
def copy_to_clipboard(event):
    widget = event.widget
    app.clipboard_clear()  # Clear the clipboard
    app.clipboard_append(widget.get())  # Append the content of the widget to the clipboard
    app.update()  # Update the application to ensure the clipboard data is set
    show_tooltip(widget, "Copied")  # Show tooltip
    widget.after(1000, hide_tooltip, event)  # Hide tooltip after 1 second

# Function to validate the search term
def validate_search_term(term):
    term = term.strip()
    alphanumeric_count = len(re.findall(r'[a-zA-Z0-9]', term))
    if alphanumeric_count < 2:
        return False
    return True

# Function to update the data grid view based on search criteria
def update_grid(search_term, tab_name, strict_mode):
    search_term = search_term.upper()
    filtered_data = []

    for entry in data:
        if tab_name == "Branch":
            branch_number = entry.get("Number1", "").upper()
            number2 = entry.get("Number2", "").upper()
            port_code = entry.get("Port Code", "").upper()

            if len(search_term) == 2:
                if strict_mode:
                    if search_term == branch_number or search_term == number2:
                        filtered_data.append(entry)
                else:
                    if search_term in branch_number or search_term in number2:
                        filtered_data.append(entry)
            elif len(search_term) >= 3:
                if strict_mode:
                    if search_term == branch_number or search_term == number2 or search_term == port_code:
                        filtered_data.append(entry)
                else:
                    if search_term in branch_number or search_term in number2 or search_term in port_code:
                        filtered_data.append(entry)

        elif tab_name == "Country":
            country_code = entry.get("Country Code", "").upper()
            country = entry.get("Country", "").upper()

            if strict_mode:
                if search_term == country_code or search_term == country:
                    filtered_data.append(entry)
            else:
                if search_term in country_code or search_term in country:
                    filtered_data.append(entry)

    if tab_name == "Branch":
        # Clear the Branch Tab
        for widget in branch_frame.winfo_children():
            widget.destroy()

        # Populate Branch Tab with Labels and Read-Only Entry Widgets
        for entry in filtered_data:
            # Branch Number, Port Code, and Airport Name on the first row
            branch_number = entry.get("Number1", "")
            number2 = entry.get("Number2", "")
            branch_number_text = f"{branch_number} / {number2}" if number2.lower() != "none" else branch_number

            label_branch_number = ctk.CTkLabel(branch_frame, text="Branch Number:")
            label_branch_number.grid(row=0, column=0, padx=5, pady=5, sticky="e")

            entry_branch_number = ctk.CTkEntry(branch_frame, width=150)
            entry_branch_number.insert(0, branch_number_text)
            entry_branch_number.configure(state="readonly")
            entry_branch_number.bind("<Double-1>", copy_to_clipboard)
            entry_branch_number.grid(row=0, column=1, padx=5, pady=5, sticky="w")

            label_port_code = ctk.CTkLabel(branch_frame, text="Port Code:")
            label_port_code.grid(row=0, column=2, padx=5, pady=5, sticky="e")

            entry_port_code = ctk.CTkEntry(branch_frame, width=150)
            entry_port_code.insert(0, entry.get("Port Code", ""))
            entry_port_code.configure(state="readonly")
            entry_port_code.bind("<Double-1>", copy_to_clipboard)
            entry_port_code.grid(row=0, column=3, padx=5, pady=5, sticky="w")

            label_airport_name = ctk.CTkLabel(branch_frame, text="Airport Name:")
            label_airport_name.grid(row=0, column=4, padx=5, pady=5, sticky="e")

            entry_airport_name = ctk.CTkEntry(branch_frame, width=150)
            entry_airport_name.insert(0, entry.get("Airport Name", ""))
            entry_airport_name.configure(state="readonly")
            entry_airport_name.bind("<Double-1>", copy_to_clipboard)
            entry_airport_name.grid(row=0, column=5, padx=5, pady=5, sticky="w")

            # City, Country, and Country Code on the second row
            label_city = ctk.CTkLabel(branch_frame, text="City:")
            label_city.grid(row=1, column=0, padx=5, pady=5, sticky="e")

            entry_city = ctk.CTkEntry(branch_frame, width=150)
            entry_city.insert(0, entry.get("City", ""))
            entry_city.configure(state="readonly")
            entry_city.bind("<Double-1>", copy_to_clipboard)
            entry_city.grid(row=1, column=1, padx=5, pady=5, sticky="w")

            label_country = ctk.CTkLabel(branch_frame, text="Country:")
            label_country.grid(row=1, column=2, padx=5, pady=5, sticky="e")

            entry_country = ctk.CTkEntry(branch_frame, width=150)
            entry_country.insert(0, entry.get("Country", ""))
            entry_country.configure(state="readonly")
            entry_country.bind("<Double-1>", copy_to_clipboard)
            entry_country.grid(row=1, column=3, padx=5, pady=5, sticky="w")

            label_country_code = ctk.CTkLabel(branch_frame, text="Country Code:")
            label_country_code.grid(row=1, column=4, padx=5, pady=5, sticky="e")

            entry_country_code = ctk.CTkEntry(branch_frame, width=150)
            entry_country_code.insert(0, entry.get("Country Code", ""))
            entry_country_code.configure(state="readonly")
            entry_country_code.bind("<Double-1>", copy_to_clipboard)
            entry_country_code.grid(row=1, column=5, padx=5, pady=5, sticky="w")

            # Time Zone on the third row
            label_time_zone = ctk.CTkLabel(branch_frame, text="Time Zone:")
            label_time_zone.grid(row=2, column=0, padx=5, pady=5, sticky="e")

            entry_time_zone = ctk.CTkEntry(branch_frame, width=150)
            entry_time_zone.insert(0, entry.get("Time Zone", ""))
            entry_time_zone.configure(state="readonly")
            entry_time_zone.bind("<Double-1>", copy_to_clipboard)
            entry_time_zone.grid(row=2, column=1, padx=5, pady=5, sticky="w", columnspan=6)

            # Separator between entries
            ctk.CTkLabel(branch_frame, text="---").grid(row=3, column=0, pady=5, columnspan=6)

    elif tab_name == "Country":
        # Clear the Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Populate Treeview with filtered data
        for entry in filtered_data:
            branch_number = entry.get("Number1", "")
            number2 = entry.get("Number2", "")
            branch_number_text = f"{branch_number} / {number2}" if number2.lower() != "none" else branch_number

            tree.insert("", tk.END, values=(
                branch_number_text,
                entry.get("Port Code", ""),
                entry.get("City", ""),
                entry.get("Country", ""),
                entry.get("Country Code", ""),
                entry.get("Time Zone", "")
            ))

        # Auto-adjust column widths
        for col in columns:
            max_width = max(
                [len(str(tree.heading(col, 'text')))] +  # Width of the header text
                [len(str(tree.item(row, 'values')[columns.index(col)])) for row in tree.get_children()]
                # Width of the values
            ) * 10  # Multiply by a factor to ensure padding
            tree.column(col, width=max_width, anchor='e')  # Right-align column values

# Sorting function
def sort_by_column(treeview, column, descending):
    # Retrieve the data and sort
    data = [(treeview.item(item, "values"), item) for item in treeview.get_children()]
    data.sort(key=lambda x: x[0][columns.index(column)], reverse=descending)
    # Rearrange rows
    for index, (values, item) in enumerate(data):
        treeview.move(item, '', index)
    # Update column heading
    treeview.heading(column, command=lambda: sort_by_column(treeview, column, not descending))

# Load JSON data
data = load_data('file.json')

# Initialize the application window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Branch Finder")
app.geometry("800x360+900+500")

# Create a Tabview
tabview = ctk.CTkTabview(app, width=780, height=300)
tabview.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="n")

# Create Tabs
tabview.add("Branch")
tabview.add("Country")

# Create a frame for the Branch tab
branch_frame = ctk.CTkFrame(tabview.tab("Branch"))
branch_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Data grid view (Treeview widget) for the Country tab
columns = ("Branch Number", "Port Code", "City", "Country", "Country Code", "Time Zone")
tree = ttk.Treeview(tabview.tab("Country"), columns=columns, show="headings")

# Create a vertical scrollbar for the Treeview
vsb = ttk.Scrollbar(tabview.tab("Country"), orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Configure columns and headings
for col in columns:
    tree.heading(col, text=col, anchor='e', command=lambda c=col: sort_by_column(tree, c, False))  # Bind sort function
    tree.column(col, width=100, stretch=tk.YES, anchor='e')  # Right-align column values

tree.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)
vsb.pack(side=tk.RIGHT, fill="y")

# Search Label
search_label = ctk.CTkLabel(app, text="Enter Branch: ")
search_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Search entry
search_entry = ctk.CTkEntry(app, width=200)
search_entry.grid(row=1, column=1, padx=10, pady=10)

# Strict mode checkbox
strict_var = tk.BooleanVar(value=True)
strict_checkbox = ctk.CTkCheckBox(app, text="Strict", variable=strict_var, onvalue=True, offvalue=False)
strict_checkbox.grid(row=1, column=2, padx=10, pady=10, sticky="w")

# Submit button with validation
def submit_action():
    search_term = search_entry.get()
    if validate_search_term(search_term):
        update_grid(search_term, tabview.get(), strict_var.get())
        search_entry.delete(0, tk.END)
        search_entry.focus()
    else:
        messagebox.showwarning("Invalid Input", "Search term must be at least two alphanumeric characters.")

submit_button = ctk.CTkButton(app, text="Submit", command=submit_action)
submit_button.grid(row=1, column=3, padx=10, pady=10, sticky="e")

# Bind Return and Escape keys to actions
app.bind('<Return>', lambda event: submit_action())
app.bind('<Escape>', lambda event: app.quit())

# Focus the search entry after the window is fully rendered
app.after(100, lambda: search_entry.focus_set())

# Make the grid responsive
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(3, weight=1)

# Start the application
app.mainloop()
