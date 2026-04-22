# Agenda telefónica basada en diccionario
def mostrar_menu():
	print("\n=== AGENDA TELEFÓNICA ===")
	print("1. Agregar amigo")
	print("2. Buscar número")
	print("3. Eliminar amigo")
	print("4. Mostrar agenda")
	print("5. Salir")


def pedir_nombre():
	nombre = input("Nombre de tu amigo (MAYÚSCULAS): ").strip().upper()
	return nombre


def agregar_contacto(agenda):
	nombre = pedir_nombre()
	if not nombre:
		print("No ingresaste un nombre válido.")
		return

	numero = input("Número de teléfono: ").strip()
	if not numero:
		print("No ingresaste un número válido.")
		return

	agenda[nombre] = numero
	print(f"Contacto '{nombre}' guardado con el número {numero}.")


def buscar_numero(agenda):
	nombre = pedir_nombre()
	if not nombre:
		print("No ingresaste un nombre válido.")
		return

	if nombre in agenda:
		print(f"El número de {nombre} es: {agenda[nombre]}")
	else:
		print(f"No se encontró el contacto '{nombre}'.")


def eliminar_contacto(agenda):
	nombre = pedir_nombre()
	if not nombre:
		print("No ingresaste un nombre válido.")
		return

	if nombre in agenda:
		del agenda[nombre]
		print(f"Contacto '{nombre}' eliminado.")
	else:
		print(f"No se encontró el contacto '{nombre}'.")


def mostrar_agenda(agenda):
	if not agenda:
		print("La agenda está vacía.")
		return

	print("\nContactos guardados:")
	for nombre, numero in agenda.items():
		print(f"- {nombre}: {numero}")


def main():
	agenda = {}

	while True:
		mostrar_menu()
		opcion = input("Elige una opción (1-5): ").strip()

		if opcion == "1":
			agregar_contacto(agenda)
		elif opcion == "2":
			buscar_numero(agenda)
		elif opcion == "3":
			eliminar_contacto(agenda)
		elif opcion == "4":
			mostrar_agenda(agenda)
		elif opcion == "5":
			print("Saliendo de la agenda. ¡Hasta luego!")
			break
		else:
			print("Opción no válida. Elige un número del 1 al 5.")


if __name__ == "__main__":
	main()
