
from .user_interface import UserInterface
from .data_persistence import DataPersistence
from .bmi_calculator import BMICalculator

class FitnessTracker:
    def __init__(self):
        self.ui = UserInterface()
        self.data = DataPersistence()
        self.bmi_calculator = BMICalculator()
    
    def run(self):
        while True:
            choice = self.ui.display_menu()
            if choice == "1":
                self.ui.add_fitness_data(self.data)
            elif choice == "2":
                self.ui.view_fitness_data(self.data)
            elif choice == "3":
                self.ui.calculate_bmi(self.bmi_calculator)
            elif choice == "4":
                self.ui.exit_program()
                break
