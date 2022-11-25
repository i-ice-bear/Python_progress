

#! 3.1 Welcome message printing

welcome_message = input("Your welcome message : ")
print("Hello", welcome_message)

#! 3.2 Sum obtain of 3 numbers : 
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
sum = num1 + num2 + num3
print(sum)


#! 3.3 Program to get the area via length and bredth of the rectangele;

length = int(input("Enter length : "))
bredth = int(input("Enter bredth : "))
area = length * bredth
print("Area is : ", area)

#! 3.4 Body mass index ( BMI calculator );


weight_of_body = float(input("Enter your weight : "))
height_of_body = float(input("Enter your height : "))

def __generate_bodyMass():
    bmi = weight_of_body / (height_of_body * height_of_body)
    print("Bmi is" , bmi)


__generate_bodyMass()

#! 3.5 Cube printing program 
__cube_number_sum = int(input("Enter your number : "))
__overall_Cube = (__cube_number_sum) * (__cube_number_sum) * (__cube_number_sum)
print("Overall cube : ", __overall_Cube)


#! 3.6 Convert kilometers into miles

__kilometer_range = float(input("Enter your kilometers : "))
__miles_conversion = __kilometer_range * 0.621317
print(__miles_conversion)

"""

#! 3.7 Quintals and kilo conversion from tonns. 

"""

__tonns_input = float(input("Enter tonns : "))
__quintals = __tonns_input * 100
__kilos = __quintals * 10
print(f"Kilo is : {__kilos} Quintal is : {__quintals}")
print(__quintals)


#! 3.8 Input small poem verse;
__poem_verse = input("Enter small verse : ")
print("Poem verse : ", __poem_verse)



#! 3.9 Value swappings;

_Number_1 = int(input("Enter your number : "))
_Number_2 = int(input("Enter your number : "))
print("original state : " , _Number_1, _Number_2)

_Number_1, _Number_2 = _Number_2 , _Number_1
print("Swapped values", _Number_1, _Number_2)

#! 3.10 Swapp value via randomization. 
 
_number_x = int(input("Enter your number : "))
_number_y = int(input("Enter your number : "))
_number_z = int(input("Enter your number : "))
print(f"Original state : {_number_x} | {_number_y} | {_number_z} ")

_number_x, _number_y, _number_z = _number_y, _number_z, _number_x

print(f"Afters changes : {_number_x} | {_number_y} | {_number_z} ")

if __name__ == "__main__":
    print(__name__)