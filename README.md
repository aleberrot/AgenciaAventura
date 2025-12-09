
---

## 🌍 **AgenciaAventura – Sistema de Gestión para Agencia de Viajes**

Proyecto académico desarrollado en **Python** para la asignatura **Programación Orientada a Objeto Seguro (TI3021)** del programa de **Analista Programador en INACAP**.

Este sistema permite gestionar destinos turísticos, paquetes personalizados y reservas seguras, implementando **autenticación por roles**, **persistencia en MySQL**, **arquitectura en capas** y **patrones de diseño**.

---

## ✅ Estado actual del proyecto

- ✅ Autenticación segura con **PBKDF2 + sal única**
- ✅ Conexión a **MySQL (XAMPP)** mediante variables de entorno
- ✅ Arquitectura modular: `models`, `dao`, `auth`, `agencia`, `main`
- ✅ `requirements.txt` y archivo de configuración centralizado
- 🔜 **En desarrollo**:  
  - CRUD completo de destinos y paquetes  
  - Sistema de reservas con validación de disponibilidad  
  - Menús CLI diferenciados por rol (cliente / administrador)

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje**: Python 3.9+
- **Base de datos**: MySQL 8.0 (vía XAMPP)
- **Conector**: `PyMySQL`
- **Seguridad**: bcrypt
- **Gestión de entorno**: `python-dotenv`
- **Arquitectura**: Capas (Presentación, Lógica, Persistencia, Seguridad)
- **Patrones**: Fachada (`AgenciaViajes`), Singleton (`conexion.py`)

---

## 📁 Estructura del proyecto

```
AgenciaAventura/
├── DTO/                   # Clases DTO (Usuario, Destino, Paquete, Reserva)
├── DAO/                   # DAOs para acceso a base de datos
├── AUTH/                  # Hashing seguro y verificación de credenciales
├── DB/                    # Conexión Singleton a MySQL
├── UI/                    # Interfaz CLI (menús interactivos)
├── config.py              # Carga de variables de entorno
├── requirements.txt       # Dependencias
├── main.py                # Arranque de la app
└── README.md
```

---

## ⚙️ Instalación y configuración

### 1. **Requisitos previos**
- Python 3.9 o superior
- XAMPP (con **MySQL** y **phpMyAdmin** activos)
- Acceso a terminal o IDE de desarrollo

### 2. **Configurar base de datos**
1. Inicia **MySQL** desde XAMPP.
2. Abre **phpMyAdmin** (`http://localhost/phpmyadmin`).
3. Crea una base de datos vacía con el nombre que desees (ej: `agencia_viajes`).
4. **Ejecuta el script** `agencia_viajes.sql` para crear las tablas.

### 3. **Configurar variables de entorno**
1. Crea un archivo `.env` en la raíz del proyecto:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=
   DB_NAME=agencia_viajes
   DB_PORT=3306
   ```
2. Asegúrate de que el valor de `DB_NAME` coincida con el nombre de tu base de datos en MySQL.

> 📌 El sistema **lee `DB_NAME` desde las variables de entorno** mediante `config.py`.

### 4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 5. **Ejecutar la aplicación**
```bash
python main.py
```

---

## 🔐 Seguridad implementada

- **Hashing de contraseñas**: Usando bcrypt
- **Comparación segura**: Para prevenir *timing attacks*
- **Consultas parametrizadas**: prevención total de inyección SQL
- **Roles diferenciados**: cliente vs administrador

---

## 📚 Documentación técnica

- **Diagrama de clases**: modelo orientado a objetos con 5 entidades principales
- **Diagrama de casos de uso**: 11 casos, 2 actores (cliente/admin)
- **BPMN**: proceso "Reservar Paquete Turístico" con validaciones y transacciones
- **Metodología ágil**: Product Backlog, Sprint Backlog de 4 semanas
- **Arquitectura en capas**: preparada para migrar a interfaz web (Flask/Django)

---

## 🧪 Funcionalidades esperadas (al finalizar)

| Módulo | Funcionalidades |
|-------|----------------|
| **Autenticación** | Registro, login, roles, hashing seguro |
| **Cliente** | Ver destinos/paquetes, realizar reservas, ver historial |
| **Administrador** | CRUD de destinos, gestión de paquetes, reportes de reservas |
| **Base de datos** | 5 tablas, relaciones N:N, claves foráneas, transacciones ACID |

---

## 📎 Entrega académica

Este repositorio acompaña la **Evaluación Sumativa 4 (ES4)** de la Unidad 4, que incluye:
- Informe técnico (`AgenciaAventura.pdf`)
- Diagramas UML y BPMN
- Código fuente en Python
- Script SQL de base de datos
- Documentación de instalación y uso

