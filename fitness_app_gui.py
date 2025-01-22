
import tkinter as tk
from tkinter import messagebox
from tracker.data_persistence import DataPersistence
from tracker.bmi_calculator import BMICalculator

class FitnessAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker")
        self.data_persistence = DataPersistence()
        self.bmi_calculator = BMICalculator()

        # Create main menu
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Fitness Tracker", font=("Arial", 20)).pack(pady=20)
        
        tk.Button(self.root, text="Add Fitness Data", command=self.add_fitness_data_window, width=25, height=2).pack(pady=5)
        tk.Button(self.root, text="View Fitness Data", command=self.view_fitness_data_window, width=25, height=2).pack(pady=5)
        tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi_window, width=25, height=2).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=25, height=2).pack(pady=5)

    def add_fitness_data_window(self):
        self.clear_window()
        tk.Label(self.root, text="Add Fitness Data", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Activity:").pack(pady=5)
        activity_entry = tk.Entry(self.root)
        activity_entry.pack(pady=5)
        
        tk.Label(self.root, text="Duration (minutes):").pack(pady=5)
        duration_entry = tk.Entry(self.root)
        duration_entry.pack(pady=5)

        def save_data():
            activity = activity_entry.get()
            duration = duration_entry.get()
            if activity and duration.isdigit():
                self.data_persistence.save_data(activity, int(duration))
                messagebox.showinfo("Success", "Fitness data saved successfully!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "Please enter valid data.")

        tk.Button(self.root, text="Save", command=save_data).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def view_fitness_data_window(self):
        self.clear_window()
        tk.Label(self.root, text="View Fitness Data", font=("Arial", 16)).pack(pady=20)
        
        data = self.data_persistence.load_data()
        if data:
            for record in data:
                tk.Label(self.root, text=f"{record['Activity']}: {record['Duration']} minutes").pack(pady=5)
        else:
            tk.Label(self.root, text="No data available.").pack(pady=5)
        
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def calculate_bmi_window(self):
        self.clear_window()
        tk.Label(self.root, text="Calculate BMI", font=("Arial", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Weight (kg):").pack(pady=5)
        weight_entry = tk.Entry(self.root)
        weight_entry.pack(pady=5)

        tk.Label(self.root, text="Height (cm):").pack(pady=5)
        height_entry = tk.Entry(self.root)
        height_entry.pack(pady=5)

        def calculate_bmi():
            try:
                weight = float(weight_entry.get())
                height = float(height_entry.get()) / 100  # Convert cm to meters
                bmi = self.bmi_calculator.calculate_bmi(weight, height)
                messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numbers.")

        tk.Button(self.root, text="Calculate", command=calculate_bmi).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessAppGUI(root)
    root.geometry("400x400")
    root.mainloop()
