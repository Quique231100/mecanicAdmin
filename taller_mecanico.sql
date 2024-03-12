-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-03-2024 a las 20:33:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `taller_mecanico`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `ID_CLIENTE` int(10) NOT NULL,
  `NOMBRE_CLIENTE` varchar(255) NOT NULL,
  `APELLIDOP_CLIENTE` varchar(255) NOT NULL,
  `APELLIDOM_CLIENTE` varchar(255) NOT NULL,
  `ID_Usuario` int(10) DEFAULT NULL,
  `Imagen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`ID_CLIENTE`, `NOMBRE_CLIENTE`, `APELLIDOP_CLIENTE`, `APELLIDOM_CLIENTE`, `ID_Usuario`, `Imagen`) VALUES
(1, 'Ramiro', 'Lupercio', 'Coronel', 2, 'Clientes/17004.png'),
(10, 'Raudel', 'c', 'c', 2, 'Clientes/hola.png'),
(11, '2', '1', '1', 2, 'Clientes/hola.png'),
(12, '2', '2', '2', 2, 'Clientes/hola.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `piezas`
--

CREATE TABLE `piezas` (
  `ID_Pieza` int(10) NOT NULL,
  `Descripcion_Pieza` longtext NOT NULL,
  `Stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `piezas`
--

INSERT INTO `piezas` (`ID_Pieza`, `Descripcion_Pieza`, `Stock`) VALUES
(1, 'Tornillo M6x201', 112),
(2, 'Espejos', 5),
(3, 'Aceite de motor 1L', 45),
(4, 'Anticongelante', 18),
(5, 'Tornillo M6x201', 112),
(6, 'Tornillo M6x201', 112),
(7, 'Tornillo M6x201', 112),
(8, 'Tornillo M6x201', 112),
(9, 'Tornillo M6x201', 112),
(10, 'Tornillo M6x201', 112),
(11, 'Tornillo M6x201', 112);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reparaciones`
--

CREATE TABLE `reparaciones` (
  `ID_REPARACION` int(10) NOT NULL,
  `ID_Pieza` int(10) NOT NULL,
  `FECHA_ENTRADA` varchar(255) NOT NULL,
  `FECHA_SALIDA` varchar(255) NOT NULL,
  `FALLA` text NOT NULL,
  `CANT_PIEZAS` int(100) NOT NULL,
  `ID_VEHICULO` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `reparaciones`
--

INSERT INTO `reparaciones` (`ID_REPARACION`, `ID_Pieza`, `FECHA_ENTRADA`, `FECHA_SALIDA`, `FALLA`, `CANT_PIEZAS`, `ID_VEHICULO`) VALUES
(1, 1, '2023-01-10', '2023-01-15', 'Problema en el motor', 2, 6),
(2, 2, '2023-02-05', '2023-02-10', 'Frenos desgastados', 4, 7),
(3, 3, '2023-03-15', '2023-03-20', 'Problema de transmisión', 1, 8),
(4, 4, '2023-04-20', '2023-04-25', 'Requiere cambio de aceite', 3, 9),
(5, 6, '10/10/23', '15/10/23', 'Balatas desgastadas', 9, 2),
(6, 4, '10-10-23', '17-10-23', 'Frenos desgastados', 2, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `ID_Usuario` int(10) NOT NULL,
  `Nombre_Usuario` varchar(255) NOT NULL,
  `Apellido_P_Usuario` varchar(255) NOT NULL,
  `Apellido_M_Usuario` varchar(255) NOT NULL,
  `Telefono_Usuario` varchar(255) NOT NULL,
  `UserName_Usuario` varchar(255) NOT NULL,
  `Perfil_Usuario` varchar(255) NOT NULL,
  `Direccion_Usuario` varchar(255) NOT NULL,
  `Password_Usuario` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`ID_Usuario`, `Nombre_Usuario`, `Apellido_P_Usuario`, `Apellido_M_Usuario`, `Telefono_Usuario`, `UserName_Usuario`, `Perfil_Usuario`, `Direccion_Usuario`, `Password_Usuario`) VALUES
(1, 'admin', 'admin', 'admin', 'admin', 'admin', 'Admin', 'admin', 'admin'),
(2, 'Enrique', 'Aguilar', 'Garcia', '3310432860', 'Quique2311', 'Admin', 'Elias Villalpando 692', '1234'),
(3, 'Fabian', 'Rivera', 'Sanchez', '3216549876', 'FabianRag', 'Gerente', 'Ocampo 27', '1234'),
(4, 'Alexa', 'Gomez', 'Sanchez', '4567891235', 'Alexa75', 'Admin', 'Revolucion 45', '1234'),
(5, 'Maria', 'Salmeron', 'Bañuelos', 'asdas', 'MariaFer', 'Secretaria', 'Elias Villalpando 692', '1234'),
(6, 'Maria', 'Jimenez', 'Hola', '3344558899', 'Maria14', 'Secretaria', 'Revolucion', '1234'),
(7, 'Jimena', 'Galvez', 'Adios', '33556688', 'Jimena11', 'Secretaria', 'Hola 74', '1234'),
(8, 'Felipe', 'Jimenez', 'aksd', '3355664488', 'Felipe15', 'Mecanico', 'Hola 75', '1234');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `ID_VEHICULO` int(10) NOT NULL,
  `MATRICULA` varchar(10) NOT NULL,
  `MARCA` varchar(255) NOT NULL,
  `MODELO` varchar(255) NOT NULL,
  `FECHA` varchar(255) NOT NULL,
  `ID_CLIENTE` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`ID_VEHICULO`, `MATRICULA`, `MARCA`, `MODELO`, `FECHA`, `ID_CLIENTE`) VALUES
(1, 'ABC123', 'Toyota', 'Camry', '01/15/2023', 1),
(2, 'XYZ789', 'Ford', 'F-150', '11/20/2022', 1),
(3, 'Honda', 'DEF456', 'Civic', '05/10/2022', 2),
(4, 'GHI789', 'Chevrolet', 'Silverado', '02/10/2023', 2),
(5, 'JKL012', 'Nissan', 'Altima', '10/08/2022', 3),
(6, 'MNO345', 'Hyundai', 'Elantra', '03/25/2023', 3),
(7, 'PQR678', 'Mazda', 'CX-5', '09/15/2022', 4),
(8, 'STU901', 'Subaru', 'Outback', '04/12/2023', 4),
(9, 'VWX234', 'Jeep', 'Wrangler', '11/30/2022', 5),
(10, 'YZA567', 'Kia', 'Sorento', '01/22/2023', 5),
(11, 'BCD890', 'Volkswagen', 'Jetta', '12/18/2022', 6),
(12, 'EFG123', 'Audi', 'A4', '02/28/2023', 6),
(13, 'HIJ456', 'BMW', 'X5', '10/05/2022', 7),
(14, 'QRS345', 'Infiniti', 'Q50', '04/05/2023', 8),
(17, '954WEF', 'Ford', 'Raptor', '12/14/2022', 9);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ID_CLIENTE`),
  ADD KEY `ID_Usuario` (`ID_Usuario`);

--
-- Indices de la tabla `piezas`
--
ALTER TABLE `piezas`
  ADD PRIMARY KEY (`ID_Pieza`);

--
-- Indices de la tabla `reparaciones`
--
ALTER TABLE `reparaciones`
  ADD PRIMARY KEY (`ID_REPARACION`),
  ADD KEY `ID_Pieza` (`ID_Pieza`),
  ADD KEY `ID_VEHICULO` (`ID_VEHICULO`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`ID_Usuario`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`ID_VEHICULO`),
  ADD KEY `ID_CLIENTE` (`ID_CLIENTE`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `ID_CLIENTE` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `piezas`
--
ALTER TABLE `piezas`
  MODIFY `ID_Pieza` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `reparaciones`
--
ALTER TABLE `reparaciones`
  MODIFY `ID_REPARACION` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `ID_Usuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  MODIFY `ID_VEHICULO` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
