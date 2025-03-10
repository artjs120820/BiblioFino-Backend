-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: bibliofino
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ciudadano_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ciudadano_id` (`ciudadano_id`),
  CONSTRAINT `administrador_ibfk_1` FOREIGN KEY (`ciudadano_id`) REFERENCES `ciudadano` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
INSERT INTO `administrador` VALUES (1,4);
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudadano`
--

DROP TABLE IF EXISTS `ciudadano`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudadano` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dni` varchar(8) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contrasenia` varchar(255) NOT NULL,
  `email_verificado` tinyint(1) DEFAULT '0',
  `distrito_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dni` (`dni`),
  UNIQUE KEY `correo` (`correo`),
  KEY `distrito_id` (`distrito_id`),
  CONSTRAINT `ciudadano_ibfk_1` FOREIGN KEY (`distrito_id`) REFERENCES `distrito` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudadano`
--

LOCK TABLES `ciudadano` WRITE;
/*!40000 ALTER TABLE `ciudadano` DISABLE KEYS */;
INSERT INTO `ciudadano` VALUES (1,'12345678','Juan','Perez','juan.perez@email.com','hashed_password_1',0,1),(2,'87654321','Maria','Lopez','maria.lopez@email.com','hashed_password_2',0,2),(3,'11223344','Carlos','Gomez','carlos.gomez@email.com','hashed_password_3',0,2),(4,'11223244','Admin','Admin','admin@admin.com','hashed_password_4',1,3);
/*!40000 ALTER TABLE `ciudadano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `copia`
--

DROP TABLE IF EXISTS `copia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `copia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libro_id` int NOT NULL,
  `isbn` varchar(20) NOT NULL,
  `idioma` varchar(50) DEFAULT NULL,
  `editorial` varchar(100) DEFAULT NULL,
  `anio` int DEFAULT NULL,
  `paginas` int DEFAULT NULL,
  `imagen` text,
  `codigo_unico` varchar(50) NOT NULL,
  `disponible` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo_unico` (`codigo_unico`),
  KEY `libro_id` (`libro_id`),
  CONSTRAINT `copia_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `libro` (`id`) ON DELETE CASCADE,
  CONSTRAINT `copia_chk_1` CHECK ((`anio` >= 0)),
  CONSTRAINT `copia_chk_2` CHECK ((`paginas` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copia`
--

LOCK TABLES `copia` WRITE;
/*!40000 ALTER TABLE `copia` DISABLE KEYS */;
INSERT INTO `copia` VALUES (1,1,'9788499890944','Español','Debolsillo',2013,416,'https://example.com/1984_esp.jpg','1984-ESP-001',0),(2,1,'9780451524935','Inglés','Signet Classics',1950,328,'https://example.com/1984_eng.jpg','1984-ENG-001',1),(3,1,'9780141036144','Francés','Penguin Books',2008,352,'https://example.com/1984_fra.jpg','1984-FRA-001',1),(4,2,'9780307474728','Español','Sudamericana',1967,471,'https://example.com/100anos_esp.jpg','100ANOS-ESP-001',0),(5,2,'9780060883287','Inglés','Harper Perennial',2006,417,'https://example.com/100anos_eng.jpg','100ANOS-ENG-001',1),(6,3,'9780743273565','Inglés','Scribner',2004,180,'https://example.com/gatsby_eng.jpg','GATSBY-ENG-001',1),(7,3,'9788420674209','Español','Alianza Editorial',2011,192,'https://example.com/gatsby_esp.jpg','GATSBY-ESP-001',1),(8,4,'9780141439518','Inglés','Penguin Classics',2002,480,'https://example.com/pride_eng.jpg','PYP-ENG-001',1),(9,4,'9788491050681','Español','Penguin Clásicos',2016,448,'https://example.com/pride_esp.jpg','PYP-ESP-001',0),(10,5,'9788420412146','Español','Alfaguara',2005,1056,'https://example.com/donquijote_esp.jpg','DQ-ESP-001',1),(11,5,'9780140449099','Inglés','Penguin Classics',2003,1072,'https://example.com/donquijote_eng.jpg','DQ-ENG-001',1);
/*!40000 ALTER TABLE `copia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distrito`
--

DROP TABLE IF EXISTS `distrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distrito` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distrito`
--

LOCK TABLES `distrito` WRITE;
/*!40000 ALTER TABLE `distrito` DISABLE KEYS */;
INSERT INTO `distrito` VALUES (1,'Ancón'),(2,'Ate'),(3,'Barranco'),(4,'Breña'),(5,'Carabayllo'),(6,'Chaclacayo'),(7,'Chorrillos'),(8,'Cieneguilla'),(9,'Comas'),(10,'El Agustino'),(11,'Independencia'),(12,'Jesús María'),(13,'La Molina'),(14,'La Victoria'),(15,'Lima'),(16,'Lince'),(17,'Los Olivos'),(18,'Lurigancho-Chosica'),(19,'Lurín'),(20,'Magdalena del Mar'),(21,'Miraflores'),(22,'Pachacámac'),(23,'Pucusana'),(24,'Pueblo Libre'),(25,'Puente Piedra'),(26,'Punta Hermosa'),(27,'Punta Negra'),(28,'Rímac'),(29,'San Bartolo'),(30,'San Borja'),(31,'San Isidro'),(32,'San Juan de Lurigancho'),(33,'San Juan de Miraflores'),(34,'San Luis'),(35,'San Martín de Porres'),(36,'San Miguel'),(37,'Santa Anita'),(38,'Santa María del Mar'),(39,'Santa Rosa'),(40,'Santiago de Surco'),(41,'Surquillo'),(42,'Villa El Salvador'),(43,'Villa María del Triunfo');
/*!40000 ALTER TABLE `distrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `autor` varchar(255) NOT NULL,
  `genero` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
INSERT INTO `libro` VALUES (1,'1984','George Orwell','Distopía'),(2,'Cien años de soledad','Gabriel García Márquez','Realismo mágico'),(3,'El gran Gatsby','F. Scott Fitzgerald','Novela clásica'),(4,'Orgullo y prejuicio','Jane Austen','Romance'),(5,'Don Quijote de la Mancha','Miguel de Cervantes','Aventura');
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserva`
--

DROP TABLE IF EXISTS `reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `copia_id` int NOT NULL,
  `fecha_reserva` datetime DEFAULT CURRENT_TIMESTAMP,
  `fecha_vencimiento` datetime NOT NULL,
  `estado` enum('pendiente','entregado','vencido') DEFAULT 'pendiente',
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `copia_id` (`copia_id`),
  CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`) ON DELETE CASCADE,
  CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`copia_id`) REFERENCES `copia` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva`
--

LOCK TABLES `reserva` WRITE;
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
INSERT INTO `reserva` VALUES (1,1,1,'2025-03-01 10:00:00','2025-03-10 23:59:59','pendiente'),(2,2,4,'2025-03-02 15:30:00','2025-03-12 23:59:59','pendiente'),(3,3,6,'2025-03-03 09:45:00','2025-03-13 23:59:59','entregado'),(4,1,9,'2025-02-25 14:20:00','2025-03-05 23:59:59','vencido');
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ciudadano_id` int NOT NULL,
  `token` varchar(500) NOT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_expiracion` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  KEY `ciudadano_id` (`ciudadano_id`),
  CONSTRAINT `token_ibfk_1` FOREIGN KEY (`ciudadano_id`) REFERENCES `ciudadano` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` VALUES (1,1,'token_usuario_juan','2025-03-10 18:17:39','2025-03-17 18:17:39'),(2,2,'token_usuario_maria','2025-03-10 18:17:39','2025-03-17 18:17:39'),(3,3,'token_usuario_carlos','2025-03-10 18:17:39','2025-03-17 18:17:39'),(4,4,'token_admin','2025-03-10 18:17:39','2025-04-09 18:17:39');
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ciudadano_id` int NOT NULL,
  `foto_url` varchar(255) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ciudadano_id` (`ciudadano_id`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`ciudadano_id`) REFERENCES `ciudadano` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,1,'https://example.com/foto1.jpg','Amo la lectura y la tecnología.','2025-03-10 18:17:39'),(2,2,'https://example.com/foto2.jpg','Interesado en novelas históricas.','2025-03-10 18:17:39'),(3,3,'https://example.com/foto3.jpg','Fanático de la ciencia ficción.','2025-03-10 18:17:39');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'bibliofino'
--

--
-- Dumping routines for database 'bibliofino'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-10 13:42:22
