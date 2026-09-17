# Sistema de Gestión de Ventas

Sistema de gestión de ventas desarrollado en Python y MySQL para administrar clientes, productos, inventario, ventas y reportes.

## 📋 Descripción

Este proyecto permite gestionar las operaciones básicas de un pequeño negocio desde una aplicación ejecutada en consola.

El sistema utiliza Python para la lógica de la aplicación y MySQL como sistema de gestión de base de datos.

## 🎯 Objetivo

Crear una solución sencilla para llevar el control de:

- Clientes
- Productos
- Inventario
- Ventas
- Detalle de ventas
- Reportes

El proyecto fue desarrollado como parte de mi portafolio para demostrar conocimientos de programación, bases de datos y desarrollo de aplicaciones.

## 🚀 Funcionalidades

### 👥 Gestión de clientes

- Registrar clientes.
- Consultar clientes registrados.
- Mostrar información de contacto.

### 📦 Gestión de productos

- Registrar productos.
- Consultar productos.
- Actualizar productos.
- Eliminar productos.
- Controlar precios.
- Controlar existencias.

### 🛒 Gestión de ventas

- Registrar ventas.
- Seleccionar un cliente.
- Agregar uno o varios productos a una venta.
- Calcular subtotales.
- Calcular el total de la venta.
- Registrar el detalle de cada producto vendido.
- Actualizar automáticamente el stock.

### 📊 Reportes

- Reporte de ventas.
- Reporte de inventario.
- Consulta del total vendido.

## 🛠️ Tecnologías utilizadas

- Python 3
- MySQL
- MySQL Connector/Python
- python-dotenv
- Git
- GitHub
- Visual Studio Code

## 🗂️ Estructura del proyecto

```text
Sistema-Gestion-venta/
│
├── src/
│   ├── clientes.py
│   ├── database.py
│   ├── main.py
│   ├── productos.py
│   ├── reportes.py
│   └── ventas.py
│
├── screenshots/
│   ├── Clientes.png
│   ├── Gestion.png
│   ├── Productos.png
│   ├── Ventas.png
│   └── Reportes.png
│
├── .env
├── .gitignore
├── BD_ventas.sql
└── README.md
