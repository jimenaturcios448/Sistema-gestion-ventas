CREATE DATABASE sistema_ventas;
use sistema_ventas;

CREATE TABLE clientes(
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
telefono VARCHAR(20),
email VARCHAR(100),
fecha_registro DATE DEFAULT (CURRENT_DATE) );

CREATE TABLE productos(
id_producto INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR (100) NOT NULL,
categoria VARCHAR(50),
PRECIO DECIMAL (10,2)NOT NULL,
stock INT NOT NULL );

CREATE TABLE ventas(
id_venta INT AUTO_INCREMENT PRIMARY KEY,
id_cliente INT NOT NULL,
fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
total DECIMAL(10,2) NOT NULL,

foreign key (id_cliente)
references clientes(id_cliente)
);

CREATE TABLE detalle_venta(
id_detalle INT AUTO_INCREMENT PRIMARY KEY,
id_venta INT NOT NULL,
id_producto INT NOT NULL,
cantidad INT NOt NULL,
precio_unitario DECIMAL(10,2) NOT NULL,

foreign key(id_venta)
 references ventas(id_venta),
 
 foreign key(id_producto)
  references productos(id_producto));
  
USE sistema_ventas;

INSERT INTO clientes (nombre,telefono,email)
VALUES
('Ana Lopez','7000-1111','ana@gmail.com'),
('Carlos Martinez','7000-2222','carlos@gmail.com'),
('Maria Hernandez','7000-1333','maria@gmail.com'),
('Marcos Gonzales','7000-4444','Marcos@gmail.com'),
('Jose Rivera','7000-5555','jose@gmail.com');

INSERT INTO productos (nombre,categoria,precio,stock)
VALUES
('Camiseta basica','Ropa',12.50,20),
('Pantalon Cargo','Ropa',25.00,15),
('Sudadera','Ropa',30.00,10),
('Gorra','Accesorios',8.50,25),
('Mochila','Accesorio',22.00,12);
  
SELECT*FROM clientes;
SELECT*FROM productos;
SELECT nombre, precio FROM productos ORDER BY precio DESC;