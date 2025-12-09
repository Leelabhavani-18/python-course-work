#1.Calculate BMI:
def calculate_bmi(weight_kg, height_m):
    print('%.2f'%(weight_kg / (height_m ** 2)))
    calculate_bmi(70, 1.75)
    calculate_bmi(85, 1.8)