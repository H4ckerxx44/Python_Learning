def f(voltage_u: float = None, ampere_i: float = None, resistance_r: float = None):
	if resistance_r is None:
		result = f"R = {(voltage_u / ampere_i):.2f}"
	if ampere is None:
		result = f"I = {(voltage_u / resistance_r):.2f}"
	if resistance is None:
		result = f"U = {(resistance_r * ampere_i):.2f}"
	print(result)

