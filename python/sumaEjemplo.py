def suma(numeros):
	"""Suma una lista recorriéndola repetidamente (O(n²))."""
	total = 0

	for i in range(len(numeros)):
		for j in range(len(numeros)):
			if i == j:
				total += numeros[j]

	return total


if __name__ == "__main__":
	valores = [1, 2, 3, 4, 5]
	print("Suma:", suma(valores))
