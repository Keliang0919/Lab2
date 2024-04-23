def calculate_bmi(height, weight):
    print("Height="  + str(height))
    print("Weight="  + str(weight))

    #Add code here to calculate BMI
    bmi = float(weight) / (float(height) * float(height))

    #Add code here to display calculate BMI
    print("The calculated BMI is " + str(bmi) + ".")

calculate_bmi(weight="57", height="1.73")