import tkinter as tk

def cm_to_feet():
    try:
        cm = float(cm_entry.get())
        feet = cm / 30.48
        result_label.config(text=f"{cm} cm = {feet:.2f} feet")
    except ValueError:
        result_label.config(text="Invalid input")

def feet_to_inches():
    try:
        feet = float(feet_entry.get())
        inches = feet * 12
        result_label.config(text=f"{feet} feet = {inches:.2f} inches")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_sqmtrs():
    try:
        sqft = float(sqft_entry.get())
        sqmtrs = sqft * 0.092903
        result_label.config(text=f"{sqft} sqft = {sqmtrs:.2f} sqmtrs")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_hectares_acres():
    try:
        sqft = float(sqft_hectares_entry.get())
        hectares = sqft * 2.2957e-5
        acres = sqft * 2.2957e-5 * 2.47105
        result_label.config(text=f"{sqft} sqft = {hectares:.4f} hectares = {acres:.4f} acres")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Unit Conversion Tool")

# Create input fields
cm_label = tk.Label(root, text="Centimeters:")
cm_label.pack()
cm_entry = tk.Entry(root)
cm_entry.pack()

feet_label = tk.Label(root, text="Feet:")
feet_label.pack()
feet_entry = tk.Entry(root)
feet_entry.pack()

sqft_label = tk.Label(root, text="Square Feet:")
sqft_label.pack()
sqft_entry = tk.Entry(root)
sqft_entry.pack()

sqft_hectares_label = tk.Label(root, text="Square Feet:")
sqft_hectares_label.pack()
sqft_hectares_entry = tk.Entry(root)
sqft_hectares_entry.pack()

# Create buttons for conversions
cm_to_feet_button = tk.Button(root, text="CM to Feet", command=cm_to_feet)
cm_to_feet_button.pack()

feet_to_inches_button = tk.Button(root, text="Feet to Inches", command=feet_to_inches)
feet_to_inches_button.pack()

sqft_to_sqmtrs_button = tk.Button(root, text="Sqft to Sqmtrs", command=sqft_to_sqmtrs)
sqft_to_sqmtrs_button.pack()

sqft_to_hectares_acres_button = tk.Button(root, text="Sqft to Hectares/Acres", command=sqft_to_hectares_acres)
sqft_to_hectares_acres_button.pack()

# Create a label to display results
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
