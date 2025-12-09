import pymysql
from . import config

class Conexion:
	"""
	Clase para establecer conexión a la base de datos
	"""
	# Método estático
	@staticmethod
	def obtener_conexion():
		"""
		Método para obtener la conexión a la base de datos.

		Se conecta a la base de datos y retorna la conexión a esta.
		"""
		try:
			conexion = pymysql.connect(
				host='localhost',
				user='root',
				password='',
				database=config.AppConfig.DB_NAME,
				charset='utf8mb4',
				cursorclass=pymysql.cursors.DictCursor,
				autocommit=False
				)
			return conexion
		except pymysql.MySQLError as e:
			print(f"Ha ocurrido un error al intentar conectarse a la base de datos: {e}")

	@staticmethod
	def cerrar_conexion(conexion):
		"""
		Método para cerrar la conexión a la base de datos

		Toma como parámetro una conexión y verifica si existe y esta abierta
		para posteriormente cerrarla.
	
		"""
		if conexion and conexion.open:
			conexion.close()