def busqueda_binaria(lista, objetivo):
	"""Devuelve el índice de objetivo en una lista ordenada o -1 si no existe."""
	izquierda = 0
	derecha = len(lista) - 1

	while izquierda <= derecha:
		medio = (izquierda + derecha) // 2
		print(f"Izquierda: {izquierda}, Derecha: {derecha}, Medio: {medio}")

		if lista[medio] == objetivo:
			print(f"Objetivo encontrado en el índice {medio}")
			return medio
		if lista[medio] < objetivo:
			print(f"{lista[medio]} es menor que {objetivo}; buscando a la derecha")
			izquierda = medio + 1
		else:
			print(f"{lista[medio]} es mayor que {objetivo}; buscando a la izquierda")
			derecha = medio - 1

	print("Objetivo no encontrado")
	return -1

busqueda_binaria([1,2,3,4,5,6,7,8], 9)
