from prompt_toolkit import prompt
height=float(input('Height_in_cm:'))
weight=float(input('Weight_in_kg:'))
height/=100
if height>0 and weight>0:
    BMI=weight/(height**2)
    if BMI<18.5:
        status="Under weight"
    elif 18.5<=BMI<25:
        status="Normal range"
    elif 25<=BMI<30:
        status="Overweight"
    else:
        status="Obesity range"        
    print(f"BMI      : {BMI:.1f}kg/m²")
    print(f"Category : {status}")
else:
    print(f"It is either invalid height or weight!")
