P = float(input("Enter money lent : "))
R = float(input("Enter rate of interest : "))
T = float(input("Enter time in years : "))

SI = (P * R * T) / 100
amount_payable = P + SI
print("Amount payable is : ", amount_payable)
