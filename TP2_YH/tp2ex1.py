def permuter_variables(a, b):
    temp = a
    a = b
    b = temp
    return a, b


variable1 = 5
variable2 = 10

print("Avant permutation :")
print("Variable 1 :", variable1)
print("Variable 2 :", variable2)

variable1, variable2 = permuter_variables(variable1, variable2)

print("\nAprès permutation :")
print("Variable 1 :", variable1)
print("Variable 2 :", variable2)