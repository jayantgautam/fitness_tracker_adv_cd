
class BMICalculator:
    @staticmethod
    def calculate_bmi(weight, height):
        return weight / (height ** 2)
    
    @staticmethod
    def get_bmi_status(bmi):
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi < 24.9:
            return "normal weight"
        elif 25 <= bmi < 29.9:
            return "overweight"
        else:
            return "obese"
