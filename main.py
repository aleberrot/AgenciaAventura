from UI.MenuPrincipal import MenuPrincipal

def main():
	try:
		MenuPrincipal.mostrar()

	except Exception as e:
		print(f"Ha ocurrido un error: {e}")

	print("Gracias por usar!")


if __name__ == "__main__":
	main()