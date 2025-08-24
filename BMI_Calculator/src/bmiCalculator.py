import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Please enter positive values for weight and height.")
            return

        # Convert cm → meters
        height = height_cm / 100  

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

# GUI Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# Title
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), bg="#f0f8ff")
title_label.pack(pady=10)

# Weight input
weight_label = tk.Label(root, text="Enter Weight (kg):", font=("Arial", 12), bg="#f0f8ff")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

# Height input (now in cm)
height_label = tk.Label(root, text="Enter Height (cm):", font=("Arial", 12), bg="#f0f8ff")
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=calculate_bmi)
calc_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#f0f8ff")
result_label.pack(pady=10)

# Run the app
root.mainloop()
