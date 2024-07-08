-- Crear la tabla 'productos'
CREATE TABLE productos (
    codigo VARCHAR(10) PRIMARY KEY,
    descripcion VARCHAR(100),
    categoria VARCHAR(50),
    cantidad INT,
    precio DECIMAL(10, 2),
    proveedor VARCHAR(100)
);

INSERT INTO productos (codigo, descripcion, categoria, cantidad, precio, proveedor) VALUES
('F001', 'Martillo', 'Herramientas Manuales', 50, 9.99, 'Ferretería Central'),
('F002', 'Destornillador Phillips', 'Herramientas Manuales', 75, 4.49, 'Herramientas Express'),
('F003', 'Llave Inglesa', 'Herramientas Manuales', 30, 12.99, 'Proveedora Industrial'),
('F004', 'Sierra de Mano', 'Herramientas Manuales', 20, 15.99, 'Ferretería Central'),
('F005', 'Alicate Universal', 'Herramientas Manuales', 40, 7.99, 'Herramientas Express'),
('F006', 'Nivel de Burbuja', 'Herramientas Manuales', 25, 8.49, 'Proveedora Industrial'),
('F007', 'Cinta Métrica 5m', 'Herramientas Manuales', 60, 3.99, 'Ferretería Central'),
('F008', 'Juego de Llaves Allen', 'Herramientas Manuales', 35, 6.99, 'Herramientas Express'),
('F009', 'Serrucho', 'Herramientas Manuales', 15, 10.99, 'Proveedora Industrial'),
('F010', 'Pistola de Silicona', 'Herramientas Manuales', 45, 5.49, 'Ferretería Central'),
('F011', 'Taladro Eléctrico', 'Herramientas Eléctricas', 20, 49.99, 'Ferretería Total'),
('F012', 'Amoladora Angular', 'Herramientas Eléctricas', 10, 59.99, 'Herramientas y Más'),
('F013', 'Lijadora Eléctrica', 'Herramientas Eléctricas', 15, 39.99, 'Ferretería Total'),
('F014', 'Sierra Circular', 'Herramientas Eléctricas', 8, 69.99, 'Herramientas y Más'),
('F015', 'Pulidora', 'Herramientas Eléctricas', 12, 55.99, 'Ferretería Total'),
('F016', 'Pistola de Calor', 'Herramientas Eléctricas', 18, 29.99, 'Herramientas y Más'),
('F017', 'Cepillo Eléctrico', 'Herramientas Eléctricas', 14, 44.99, 'Ferretería Total'),
('F018', 'Multiherramienta Oscilante', 'Herramientas Eléctricas', 9, 74.99, 'Herramientas y Más'),
('F019', 'Rotomartillo', 'Herramientas Eléctricas', 11, 89.99, 'Ferretería Total'),
('F020', 'Clavadora Eléctrica', 'Herramientas Eléctricas', 7, 99.99, 'Herramientas y Más'),
('F021', 'Tornillo 1/4"', 'Fijaciones', 100, 0.10, 'Fijaciones y Tornillos'),
('F022', 'Tornillo 3/8"', 'Fijaciones', 120, 0.15, 'Fijaciones y Tornillos'),
('F023', 'Clavo 1"', 'Fijaciones', 200, 0.05, 'Fijaciones y Tornillos'),
('F024', 'Clavo 2"', 'Fijaciones', 180, 0.08, 'Fijaciones y Tornillos'),
('F025', 'Taco de Nylon', 'Fijaciones', 150, 0.12, 'Fijaciones y Tornillos'),
('F026', 'Arandela', 'Fijaciones', 300, 0.02, 'Fijaciones y Tornillos'),
('F027', 'Tuerca 1/4"', 'Fijaciones', 250, 0.03, 'Fijaciones y Tornillos'),
('F028', 'Tuerca 3/8"', 'Fijaciones', 220, 0.04, 'Fijaciones y Tornillos'),
('F029', 'Perno 1/4"', 'Fijaciones', 130, 0.20, 'Fijaciones y Tornillos'),
('F030', 'Perno 3/8"', 'Fijaciones', 110, 0.25, 'Fijaciones y Tornillos'),
('F031', 'Cinta Aislante', 'Materiales Eléctricos', 80, 1.99, 'Distribuidora Eléctrica'),
('F032', 'Interruptor', 'Materiales Eléctricos', 90, 2.49, 'Suministros Eléctricos'),
('F033', 'Enchufe', 'Materiales Eléctricos', 70, 1.99, 'Distribuidora Eléctrica'),
('F034', 'Caja de Distribución', 'Materiales Eléctricos', 50, 4.99, 'Suministros Eléctricos'),
('F035', 'Tubo Conduit', 'Materiales Eléctricos', 40, 3.99, 'Distribuidora Eléctrica'),
('F036', 'Regleta', 'Materiales Eléctricos', 60, 2.99, 'Suministros Eléctricos'),
('F037', 'Foco LED 9W', 'Iluminación', 85, 2.99, 'Luz y Brillo'),
('F038', 'Foco LED 12W', 'Iluminación', 70, 3.49, 'Luz y Brillo'),
('F039', 'Tubo Fluorescente', 'Iluminación', 55, 5.99, 'Iluminación Total'),
('F040', 'Lámpara de Techo', 'Iluminación', 25, 19.99, 'Luz y Brillo'),
('F041', 'Aplique de Pared', 'Iluminación', 30, 14.99, 'Iluminación Total'),
('F042', 'Proyector LED', 'Iluminación', 20, 24.99, 'Luz y Brillo'),
('F043', 'Farol Solar', 'Iluminación', 18, 29.99, 'Iluminación Total'),
('F044', 'Cinta de LED', 'Iluminación', 40, 12.99, 'Luz y Brillo'),
('F045', 'Batería 9V', 'Baterías', 100, 1.49, 'Energía Segura'),
('F046', 'Batería AA', 'Baterías', 150, 0.99, 'Energía Segura'),
('F047', 'Batería AAA', 'Baterías', 120, 0.89, 'Energía Segura'),
('F048', 'Batería C', 'Baterías', 80, 1.29, 'Energía Segura'),
('F049', 'Batería D', 'Baterías', 70, 1.49, 'Energía Segura'),
('F050', 'Batería 12V', 'Baterías', 60, 5.99, 'Energía Segura');

-- Crear la tabla 'proveedores'
CREATE TABLE proveedores (
    id_proveedor INT PRIMARY KEY,
    nombre_proveedor VARCHAR(100),
    direccion VARCHAR(150),
    contacto VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO proveedores (id_proveedor, nombre_proveedor, direccion, contacto, email) VALUES
(1, 'Ferretería Central', 'Calle Principal 123, Ciudad', 'Juan Pérez', 'juan.perez@ferreteriacentral.com'),
(2, 'Herramientas Express', 'Avenida Industrial 456, Ciudad', 'Ana López', 'ana.lopez@herramientasexpress.com'),
(3, 'Proveedora Industrial', 'Zona Comercial 789, Ciudad', 'Carlos Gómez', 'carlos.gomez@proveedoraindustrial.com'),
(4, 'Ferretería Total', 'Boulevard de las Ferias 101, Ciudad', 'Marta Ruiz', 'marta.ruiz@ferreteriacentral.com'),
(5, 'Herramientas y Más', 'Plaza de la Tecnología 202, Ciudad', 'Luis Torres', 'luis.torres@herramientasy.com'),
(6, 'Fijaciones y Tornillos', 'Polígono Industrial 303, Ciudad', 'Gloria Ramírez', 'gloria.ramirez@fijacionesytornillos.com'),
(7, 'Distribuidora Eléctrica', 'Parque Empresarial 404, Ciudad', 'Pedro Sánchez', 'pedro.sanchez@distribuidoraelectrica.com'),
(8, 'Suministros Eléctricos', 'Centro Comercial 505, Ciudad', 'Carmen Flores', 'carmen.flores@suministroselectricos.com'),
(9, 'Luz y Brillo', 'Avenida de la Luz 606, Ciudad', 'David Rodríguez', 'david.rodriguez@luzybrillo.com'),
(10, 'Iluminación Total', 'Calle de la Iluminación 707, Ciudad', 'Laura Martínez', 'laura.martinez@iluminaciontotal.com'),
(11, 'Energía Segura', 'Plaza de la Energía 808, Ciudad', 'Fernando Morales', 'fernando.morales@energíasegura.com');

-- Crear la tabla 'categoria'
CREATE TABLE categoria (
    id_categoria INT PRIMARY KEY,
    nombre_categoria VARCHAR(50)
);

INSERT INTO categoria (id_categoria, nombre_categoria) VALUES
(1, 'Herramientas Manuales'),
(2, 'Herramientas Eléctricas'),
(3, 'Fijaciones'),
(4, 'Materiales Eléctricos'),
(5, 'Iluminación'),
(6, 'Baterías');
