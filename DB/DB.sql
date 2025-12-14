
-- Tabla: usuarios
CREATE  TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    rol ENUM('ADMIN', 'CLIENTE') NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

-- Tabla: destinos
CREATE TABLE destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    actividades TEXT ,
    costo DECIMAL(10,2) NOT NULL CHECK (costo >= 0)
);

-- Tabla: paquetes
CREATE TABLE paquetes (
    id_paquete INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    precio_total DECIMAL(10,2) NOT NULL CHECK (precio_total >= 0),
    CHECK (fecha_fin >= fecha_inicio)
);

-- Tabla intermedia: paquetes_destinos (relación muchos a muchos)
CREATE TABLE paquetes_destinos (
    id_paquete INT,
    id_destino INT,
    PRIMARY KEY (id_paquete, id_destino),
    FOREIGN KEY (id_paquete) REFERENCES paquetes(id_paquete) ON DELETE CASCADE,
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino) ON DELETE CASCADE
);

-- Tabla: reservas
CREATE TABLE reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_paquete INT NOT NULL,
    fecha_reserva DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) NOT NULL DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'confirmada', 'cancelada')),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_paquete) REFERENCES paquetes(id_paquete) ON DELETE CASCADE
) ;
