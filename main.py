from UI.MenuPrincipal import MenuPrincipal

app = MenuPrincipal()
def main():
	try:
		app.mostrar()

	except Exception as e:
		print(f"Ha ocurrido un error: {e}")
	print("Gracias por usar!")


if __name__ == "__main__":
	main()