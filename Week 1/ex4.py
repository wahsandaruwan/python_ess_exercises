# ======Variables and Value Assigning=========

# ------The = operator can be used to assign values to variables------
bakers_dozen = 12 + 1
temperature = 93

# --------Variables can be used as values and in expressions---------
print(temperature,bakers_dozen)
print("Celsius : ",(temperature - 32) * 5 / 9)
print("Fahrenheit : ", float(temperature))

# ---------You can assign a different value to an existing variable---------
temperature = 26
print("New Value : ", temperature)

# ----------Multiple variables can be used in arbitrary expressions----------
offset = 32
multiplier = 5.0 / 9.0
celsius = (temperature - offset) * multiplier
print("Celsius Value : ",celsius)

