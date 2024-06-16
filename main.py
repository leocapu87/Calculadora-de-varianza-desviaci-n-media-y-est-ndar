from mean_var_std import calculate

# Prueba de la función calculate()
try:
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
except ValueError as e:
    print(e)

# Otra prueba con datos incorrectos
try:
    result = calculate([0, 1, 2])
    print(result)
except ValueError as e:
    print(e)
