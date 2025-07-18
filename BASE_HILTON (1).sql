-- ELIMINAR Y CREAR BASE DE DATOS
DROP DATABASE IF EXISTS HotelHilton;
CREATE DATABASE HotelHilton;
USE HotelHilton;

-- TABLA: Categoria
CREATE TABLE Categoria (
    idCategoria INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    tipo VARCHAR(45) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    servicio VARCHAR(100) NOT NULL,
    PRIMARY KEY(idCategoria)
);

-- TABLA: hotel
CREATE TABLE hotel (
  idhotel INT AUTO_INCREMENT NOT NULL,
  Nombre_Hotel VARCHAR(45) NOT NULL,
  Descripcion VARCHAR(100) NOT NULL,
  Fecha_apertura DATE NOT NULL,
  Direccion VARCHAR(48) NOT NULL,
  ciudad VARCHAR(45) NOT NULL,
  Pais VARCHAR(45) NOT NULL,
  Telefono_contacto VARCHAR(45) NOT NULL,
  correo_electronico VARCHAR(45) NOT NULL,
  idCategoria INT NOT NULL,
  estado ENUM('abierto','cerrado') DEFAULT 'abierto',
  PRIMARY KEY (idhotel),
  FOREIGN KEY (idCategoria) REFERENCES Categoria (idCategoria)
);


-- TABLA: Temporada
CREATE TABLE Temporada (
  idTemporada INT AUTO_INCREMENT NOT NULL,
  nombreTemporada VARCHAR(45) NOT NULL,
  descripcionTemporada VARCHAR(45) NOT NULL,
  PRIMARY KEY (idTemporada)
);

-- TABLA: Hotel_has_Temporada
CREATE TABLE Hotel_has_Temporada(
  idTemporada INT NOT NULL, 
  idHotel INT NOT NULL,
  fechaInicio DATE NOT NULL,
  fechaFin DATE NOT NULL,
  PRIMARY KEY (idTemporada, idHotel),
  FOREIGN KEY (idTemporada) REFERENCES Temporada (idTemporada),
  FOREIGN KEY (idhotel) REFERENCES hotel (idhotel)
);

-- TABLA: usuario
CREATE TABLE usuario (
  id_usuario INT AUTO_INCREMENT NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  correo_usuario VARCHAR(100) NOT NULL,
  contraseña VARCHAR(45) NOT NULL,
  origen ENUM("colombiano","extranjero"),
  PRIMARY KEY (id_usuario)
);

-- TABLA: MotivoEstancia
CREATE TABLE MotivoEstancia (
  idMotivoEstancia INT AUTO_INCREMENT NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  descripcion VARCHAR(45) NOT NULL,
  PRIMARY KEY (idMotivoEstancia)
);

-- TABLA: Reserva
CREATE TABLE Reserva (
  idReserva INT AUTO_INCREMENT NOT NULL,
  fechaInicio DATE NOT NULL,
  fechaFin DATE NOT NULL,
  idMotivoEstancia INT NOT NULL,
  PRIMARY KEY (idReserva),
  FOREIGN KEY (idMotivoEstancia) REFERENCES MotivoEstancia (idMotivoEstancia)
);

-- TABLA: TipoHabitacion
CREATE TABLE TipoHabitacion (
  idTipoHabitacion INT AUTO_INCREMENT NOT NULL,
  nombreTipoHabitacion VARCHAR(45) NOT NULL,
  descripcion VARCHAR(45) NOT NULL,
  PRIMARY KEY (idTipoHabitacion)
);

-- TABLA: Habitacion
CREATE TABLE Habitacion (
  Codigo INT AUTO_INCREMENT NOT NULL,
  piso VARCHAR(45) NOT NULL,
  idTipoHabitacion INT NOT NULL,
  id_usuario INT NOT NULL,
  idhotel INT NOT NULL,
  PRIMARY KEY (Codigo),
  FOREIGN KEY (idTipoHabitacion) REFERENCES TipoHabitacion (idTipoHabitacion),
  FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
  FOREIGN KEY (idhotel) REFERENCES hotel (idhotel)
);

-- TABLA: DetalleReserva
CREATE TABLE DetalleReserva (
  idDetalleReserva INT AUTO_INCREMENT NOT NULL,
  idReserva INT NOT NULL,
  precio VARCHAR(45) NOT NULL,
  Codigo INT NOT NULL,
  idHotel INT NOT NULL,
  PRIMARY KEY (idDetalleReserva),
  FOREIGN KEY (idReserva) REFERENCES Reserva (idReserva),
  FOREIGN KEY (Codigo) REFERENCES Habitacion (Codigo),
  FOREIGN KEY (idhotel) REFERENCES hotel (idhotel)
);

-- TABLA: Factura
CREATE TABLE Factura (
  idFactura INT AUTO_INCREMENT NOT NULL,
  fechaEmision DATE NOT NULL,
  metodoPago VARCHAR(45) NOT NULL,
  idDetalleReserva INT NOT NULL,
  idReserva INT NOT NULL,
  Codigo INT NOT NULL,
  idHotel INT NOT NULL,
  PRIMARY KEY (idFactura),
  FOREIGN KEY (idDetalleReserva) REFERENCES DetalleReserva (idDetalleReserva),
  FOREIGN KEY (idReserva) REFERENCES Reserva (idReserva),
  FOREIGN KEY (Codigo) REFERENCES Habitacion (Codigo),
  FOREIGN KEY (idhotel) REFERENCES hotel (idhotel)
);

-- INSERTS DE PRUEBA

-- Categoria (10 registros)
INSERT INTO Categoria (nombre,tipo,descripcion,servicio) VALUES
("Económico","1 estrella","Básico para estadía corta","Cama, baño compartido"),
("Estándar","2 estrella","Comodidad esencial","Baño privado, desayuno"),
("Confort","3 estrella","Buena relación precio/calidad","Wi-Fi, restaurante"),
("Superior","4 estrella","Alta calidad","Piscina, gimnasio"),
("Lujo","5 estrella","Lujo y exclusividad","Spa, concierge"),
("Boutique","Especial","Diseño exclusivo","Decoración única"),
("Resort","Especial","Enfoque recreativo","Todo incluido"),
("Ecohotel","Especial","Enfoque ecológico","Energías renovables"),
("Hostal","Sin estrellas","Informal y económico","Ambiente familiar"),
("Aparthotel","Especial","Estancias largas","Cocina equipada");

-- Temporada (3 registros)
INSERT INTO Temporada (nombreTemporada, descripcionTemporada) VALUES
('Alta', 'Vacaciones'),
('Media', 'Temporada intermedia'),
('Baja', 'Entre semana');

-- usuario (10 registros)
INSERT INTO usuario (nombre, correo_usuario, contraseña, origen) VALUES
('Laura Mendoza', 'laura@correo.com', '123', 'colombiano'),
('David Ruiz', 'david@correo.com', 'abc', 'colombiano'),
('Sara Gómez', 'sara@correo.com', 'pass', 'extranjero'),
('Juan Pérez', 'juan@correo.com', 'xyz', 'colombiano'),
('Ana Torres', 'ana@correo.com', 'qwe', 'extranjero'),
('Luis Rojas', 'luis@correo.com', 'asd', 'colombiano'),
('Camila Díaz', 'camila@correo.com', 'zxc', 'extranjero'),
('Carlos Mesa', 'carlos@correo.com', '000', 'colombiano'),
('Julia Rey', 'julia@correo.com', 'mnb', 'colombiano'),
('Felipe León', 'felipe@correo.com', 'lkj', 'extranjero');

-- hotel (10 registros)
INSERT INTO hotel (Nombre_Hotel, Descripcion, Fecha_apertura, Direccion, ciudad, Pais, Telefono_contacto, correo_electronico, idCategoria) VALUES
('SolMar', 'Frente a la playa', '2020-01-01', 'Calle 1', 'Cartagena', 'Colombia', '300123456', 'solmar@hotel.com', 1),
('GreenLife', 'Ecohotel en las montañas', '2021-05-15', 'Cra 2', 'Medellín', 'Colombia', '301234567', 'green@hotel.com', 8),
('CityView', 'Vista panorámica urbana', '2018-08-10', 'Av 3', 'Bogotá', 'Colombia', '302345678', 'city@hotel.com', 3),
('LuxeStay', 'Hotel de lujo', '2019-11-30', 'Calle 4', 'Cali', 'Colombia', '303456789', 'luxe@hotel.com', 5),
('RelaxInn', 'Ambiente tranquilo', '2022-03-05', 'Cra 5', 'Santa Marta', 'Colombia', '304567890', 'relax@hotel.com', 2),
('Boutique X', 'Diseño exclusivo', '2021-09-12', 'Calle 6', 'Manizales', 'Colombia', '305678901', 'boutique@hotel.com', 6),
('Resort Playa', 'Vacacional', '2020-12-20', 'Cra 7', 'San Andrés', 'Colombia', '306789012', 'resort@hotel.com', 7),
('EcoCasa', 'Ecológico y moderno', '2019-07-18', 'Calle 8', 'Armenia', 'Colombia', '307890123', 'eco@hotel.com', 8),
('Hostal Luz', 'Económico', '2023-01-10', 'Cra 9', 'Pereira', 'Colombia', '308901234', 'luz@hostal.com', 9),
('AptHotel', 'Estancias largas', '2021-06-25', 'Calle 10', 'Bucaramanga', 'Colombia', '309012345', 'apt@hotel.com', 10);

-- Hotel_has_Temporada (10 registros)
INSERT INTO Hotel_has_Temporada (idTemporada, idHotel, fechaInicio, fechaFin) VALUES
(1, 1, '2025-06-01', '2025-08-15'),
(2, 2, '2025-04-01', '2025-05-31'),
(3, 3, '2025-02-01', '2025-03-31'),
(1, 4, '2025-12-01', '2026-01-15'),
(2, 5, '2025-03-10', '2025-04-10'),
(3, 6, '2025-01-05', '2025-01-25'),
(1, 7, '2025-06-15', '2025-07-30'),
(2, 8, '2025-05-01', '2025-06-10'),
(3, 9, '2025-02-15', '2025-03-01'),
(1, 10, '2025-07-01', '2025-08-10');

-- MotivoEstancia (5 registros)
INSERT INTO MotivoEstancia (nombre, descripcion) VALUES
('Vacaciones', 'Descanso y turismo'),
('Negocios', 'Trabajo y reuniones'),
('Salud', 'Tratamiento o cirugía'),
('Evento', 'Asistencia a eventos'),
('Estudio', 'Capacitación o estudio');

-- Reserva (10 registros)
INSERT INTO Reserva (fechaInicio, fechaFin, idMotivoEstancia) VALUES
('2025-07-01', '2025-07-05', 1),
('2025-07-10', '2025-07-15', 2),
('2025-07-20', '2025-07-25', 3),
('2025-08-01', '2025-08-07', 1),
('2025-09-10', '2025-09-12', 4),
('2025-10-05', '2025-10-10', 5),
('2025-11-01', '2025-11-03', 2),
('2025-12-15', '2025-12-20', 1),
('2025-06-05', '2025-06-07', 3),
('2025-04-20', '2025-04-25', 4);

-- TipoHabitacion (5 registros)
INSERT INTO TipoHabitacion (nombreTipoHabitacion, descripcion) VALUES
('Individual', 'Para una persona'),
('Doble', 'Para dos personas'),
('Triple', 'Para tres personas'),
('Suite', 'De lujo'),
('Familiar', 'Para familias');

-- Habitacion (10 registros)
INSERT INTO Habitacion (piso, idTipoHabitacion, id_usuario, idhotel) VALUES
('1A', 1, 1, 1),
('1B', 2, 2, 2),
('2A', 3, 3, 3),
('2B', 4, 4, 4),
('3A', 5, 5, 5),
('3B', 1, 6, 6),
('4A', 2, 7, 7),
('4B', 3, 8, 8),
('5A', 4, 9, 9),
('5B', 5, 10, 10);

-- DetalleReserva (10 registros)
INSERT INTO DetalleReserva (idReserva, precio, Codigo, idHotel) VALUES
(1, '200000', 1, 1),
(2, '300000', 2, 2),
(3, '400000', 3, 3),
(4, '350000', 4, 4),
(5, '250000', 5, 5),
(6, '500000', 6, 6),
(7, '280000', 7, 7),
(8, '320000', 8, 8),
(9, '270000', 9, 9),
(10, '450000', 10, 10);

-- Factura (10 registros)
INSERT INTO Factura (fechaEmision, metodoPago, idDetalleReserva, idReserva, Codigo, idHotel) VALUES
('2025-07-06', 'Tarjeta', 1, 1, 1, 1),
('2025-07-16', 'Efectivo', 2, 2, 2, 2),
('2025-07-26', 'Transferencia', 3, 3, 3, 3),
('2025-08-08', 'Tarjeta', 4, 4, 4, 4),
('2025-09-13', 'Efectivo', 5, 5, 5, 5),
('2025-10-11', 'Tarjeta', 6, 6, 6, 6),
('2025-11-04', 'Transferencia', 7, 7, 7, 7),
('2025-12-21', 'Efectivo', 8, 8, 8, 8),
('2025-06-08', 'Tarjeta', 9, 9, 9, 9),
('2025-04-26', 'Transferencia', 10, 10, 10, 10);

-- VERIFICAR
SHOW TABLES;
SELECT * FROM Categoria;
SELECT * FROM hotel;
SELECT * FROM usuario;
SELECT * FROM Habitacion;
SELECT * FROM Reserva;
SELECT * FROM Factura;


