
import tkinter as tk
from fitness_app_gui import FitnessAppGUI

def main():
    root = tk.Tk()
    root.geometry("400x400")  # Set the window size
    app = FitnessAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
