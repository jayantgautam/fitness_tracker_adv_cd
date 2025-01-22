
class UserInterface:
    def display_menu(self):
        print("1. Add Fitness Data")
        print("2. View Fitness Data")
        print("3. Calculate BMI")
        print("4. Exit")
        return input("Choose an option: ")
    
    def add_fitness_data(self, data_persistence):
        date = input("Enter date (YYYY-MM-DD): ")
        activity = input("Enter activity: ")
        duration = input("Enter duration (in minutes): ")
        data_persistence.save_data(date, activity, duration)
    
    def view_fitness_data(self, data_persistence):
        data = data_persistence.load_data()
        for record in data:
            print(f"Date: {record['date']}, Activity: {record['activity']}, Duration: {record['duration']} minutes")
    
    def calculate_bmi(self, bmi_calculator):
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        bmi = bmi_calculator.calculate_bmi(weight, height)
        status = bmi_calculator.get_bmi_status(bmi)
        print(f"Your BMI is {bmi:.2f}. You are {status}.")
    
    def exit_program(self):
        print("Exiting the program. Goodbye!")
