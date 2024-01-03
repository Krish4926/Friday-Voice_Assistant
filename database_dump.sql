-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: friday_allusers
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `friday_config`
--

DROP TABLE IF EXISTS `friday_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `friday_config` (
  `id` int NOT NULL AUTO_INCREMENT,
  `default_speech_rate` float DEFAULT NULL,
  `default_email` varchar(255) DEFAULT NULL,
  `default_password` varchar(255) DEFAULT NULL,
  `default_volume` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friday_config`
--

LOCK TABLES `friday_config` WRITE;
/*!40000 ALTER TABLE `friday_config` DISABLE KEYS */;
INSERT INTO `friday_config` VALUES (1,130,'fridayaibykrish@gmail.com','fridayaibykrish',1);
/*!40000 ALTER TABLE `friday_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `krish4926_history`
--

DROP TABLE IF EXISTS `krish4926_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `krish4926_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_input` text,
  `friday_output` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `krish4926_history`
--

LOCK TABLES `krish4926_history` WRITE;
/*!40000 ALTER TABLE `krish4926_history` DISABLE KEYS */;
INSERT INTO `krish4926_history` VALUES (1,'open youtube for me','Opening websites: youtube','2023-12-26 06:47:15');
/*!40000 ALTER TABLE `krish4926_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testuser1_history`
--

DROP TABLE IF EXISTS `testuser1_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testuser1_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_input` text,
  `friday_output` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testuser1_history`
--

LOCK TABLES `testuser1_history` WRITE;
/*!40000 ALTER TABLE `testuser1_history` DISABLE KEYS */;
INSERT INTO `testuser1_history` VALUES (1,'open instagram for me','Opening websites: instagram','2023-12-26 06:55:35');
/*!40000 ALTER TABLE `testuser1_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testuser3_history`
--

DROP TABLE IF EXISTS `testuser3_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testuser3_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_input` text,
  `friday_output` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testuser3_history`
--

LOCK TABLES `testuser3_history` WRITE;
/*!40000 ALTER TABLE `testuser3_history` DISABLE KEYS */;
INSERT INTO `testuser3_history` VALUES (1,'open youtube','Opening websites: youtube','2023-12-26 13:25:27'),(2,'it\'s a good evening yaar i would like to listen some songs','Playing Song: play destiny','2023-12-26 13:31:23'),(3,'it\'s a good evening let\'s play some songs','Playing Song: destiny','2023-12-26 13:32:59'),(4,'create to do list','To-do created.','2023-12-26 13:45:16'),(5,'create to do list','To-do created.','2023-12-26 13:46:58'),(6,'create to do','To-do created.','2023-12-26 13:49:22'),(7,'create to do','To-do created.','2023-12-26 14:03:08'),(8,'create to do list','To-do created.','2023-12-26 14:04:56'),(9,'what is the time','Sir, the time is 07:44 PM.','2023-12-26 14:14:34'),(10,'can you tell me the time now','Sir, the time is 07:44 PM.','2023-12-26 14:14:48');
/*!40000 ALTER TABLE `testuser3_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todos`
--

DROP TABLE IF EXISTS `todos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `todos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `todo_text` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `completed` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todos`
--

LOCK TABLES `todos` WRITE;
/*!40000 ALTER TABLE `todos` DISABLE KEYS */;
INSERT INTO `todos` VALUES (1,'testuser3','write chemistry journal','2023-12-26 13:45:12',0),(2,'testuser3','complete cs project','2023-12-26 13:46:54',0),(3,'testuser3','complete physics homework','2023-12-26 13:49:18',0),(4,'testuser3','coffee time','2023-12-26 14:03:04',0),(5,'testuser3','coffee break','2023-12-26 14:04:52',0);
/*!40000 ALTER TABLE `todos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usage_reg`
--

DROP TABLE IF EXISTS `usage_reg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usage_reg` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `log_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usage_reg`
--

LOCK TABLES `usage_reg` WRITE;
/*!40000 ALTER TABLE `usage_reg` DISABLE KEYS */;
INSERT INTO `usage_reg` VALUES (1,'testuser1','TestUser1','2023-12-26 04:11:24'),(2,'testuser2','TestUser2','2023-12-26 05:19:24'),(13,'testuser1','TestUser1','2023-12-26 06:37:44'),(15,'Krish4926','Krish Brahmbhatt','2023-12-26 06:46:11'),(16,'testuser1','TestUser1','2023-12-26 12:22:27'),(17,'testuser1','TestUser1','2023-12-26 18:45:21'),(18,'Krish4926','Krish Brahmbhatt','2023-12-26 18:50:45'),(19,'testuser3','TestUser3','2023-12-26 18:52:27'),(20,'testuser3','TestUser3','2023-12-26 18:55:13'),(21,'testuser3','TestUser3','2023-12-26 19:00:30'),(22,'testuser3','TestUser3','2023-12-26 19:02:01');
/*!40000 ALTER TABLE `usage_reg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(50) NOT NULL,
  `email_id` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mobile_no` varchar(10) DEFAULT NULL,
  `role` varchar(50) DEFAULT 'guest',
  PRIMARY KEY (`username`),
  UNIQUE KEY `email_id` (`email_id`),
  UNIQUE KEY `mobile_no` (`mobile_no`),
  CONSTRAINT `users_chk_1` CHECK ((length(`mobile_no`) = 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Krish4926','krishbrahmbhatt4926@gmail.com','Krish Brahmbhatt','krish4926','8780930655','admin'),('testuser1','testuser1@gmail.com','TestUser1','testuser1','1234567890','guest'),('testuser2','testuser2@gmail.com','TestUser2','testuser2','0987654321','guest'),('testuser3','testuser3@gmail.com','TestUser3','testuser3','1212121212','guest');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `websites`
--

DROP TABLE IF EXISTS `websites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `websites` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `websites`
--

LOCK TABLES `websites` WRITE;
/*!40000 ALTER TABLE `websites` DISABLE KEYS */;
INSERT INTO `websites` VALUES (1,'Google','https://www.google.com'),(2,'YouTube','https://www.youtube.com'),(3,'Facebook','https://www.facebook.com'),(4,'WhatsApp','https://www.whatsapp.com'),(5,'Amazon','https://www.amazon.in'),(6,'Flipkart','https://www.flipkart.com'),(7,'Instagram','https://www.instagram.com'),(8,'Twitter','https://www.twitter.com'),(9,'LinkedIn','https://www.linkedin.com'),(10,'Yahoo','https://in.yahoo.com'),(11,'Netflix','https://www.netflix.com'),(12,'Hotstar','https://www.hotstar.com'),(13,'Paytm','https://www.paytm.com'),(14,'Snapdeal','https://www.snapdeal.com'),(15,'Indiatimes','https://www.indiatimes.com'),(16,'IRCTC','https://www.irctc.co.in'),(17,'Zomato','https://www.zomato.com'),(18,'Swiggy','https://www.swiggy.com'),(19,'OLX','https://www.olx.in'),(20,'Quora','https://www.quora.com'),(21,'BookMyShow','https://www.bookmyshow.com'),(22,'Cricbuzz','https://www.cricbuzz.com'),(23,'JioSaavn','https://www.jiosaavn.com'),(24,'MakeMyTrip','https://www.makemytrip.com'),(25,'Myntra','https://www.myntra.com'),(26,'Ajio','https://www.ajio.com'),(27,'Hindustan Times','https://www.hindustantimes.com'),(28,'NDTV','https://www.ndtv.com'),(29,'ICICI Bank','https://www.icicibank.com'),(30,'State Bank of India','https://www.sbi.co.in'),(31,'HDFC Bank','https://www.hdfcbank.com'),(32,'Axis Bank','https://www.axisbank.com'),(33,'Cricinfo','https://www.espncricinfo.com'),(34,'Gaana','https://www.gaana.com'),(35,'BigBasket','https://www.bigbasket.com'),(36,'Rediff','https://www.rediff.com'),(37,'Economic Times','https://economictimes.indiatimes.com'),(38,'Jabong','https://www.jabong.com'),(39,'Shopclues','https://www.shopclues.com'),(40,'Lenskart','https://www.lenskart.com'),(41,'Zee News','https://zeenews.india.com'),(42,'Yatra','https://www.yatra.com'),(43,'India Today','https://www.indiatoday.in'),(44,'Firstpost','https://www.firstpost.com'),(45,'Moneycontrol','https://www.moneycontrol.com'),(46,'Inshorts','https://www.inshorts.com'),(47,'Cleartrip','https://www.cleartrip.com'),(48,'Justdial','https://www.justdial.com'),(49,'Magicbricks','https://www.magicbricks.com'),(50,'Naukri.com','https://www.naukri.com'),(51,'Shine.com','https://www.shine.com'),(52,'Bewakoof','https://www.bewakoof.com'),(53,'Medlife','https://www.medlife.com'),(54,'Koimoi','https://www.koimoi.com'),(55,'CarDekho','https://www.cardekho.com'),(56,'99acres','https://www.99acres.com'),(57,'IndiaMart','https://www.indiamart.com'),(58,'Voot','https://www.voot.com'),(59,'Udemy','https://www.udemy.com'),(60,'Coursera','https://www.coursera.org'),(61,'Hike','https://www.hike.in'),(62,'Jio','https://www.jio.com'),(63,'Practo','https://www.practo.com'),(64,'Croma','https://www.croma.com'),(65,'Zomato','https://www.zomato.com'),(66,'Bigg Boss','https://www.voot.com/bigg-boss'),(67,'Hotels.com','https://www.hotels.com'),(68,'UrbanClap','https://www.urbanclap.com'),(69,'Indigo','https://www.goindigo.in'),(70,'Snapfish','https://www.snapfish.in'),(71,'PolicyBazaar','https://www.policybazaar.com'),(72,'Dineout','https://www.dineout.co.in'),(73,'Sulekha','https://www.sulekha.com'),(74,'Jagran','https://www.jagran.com'),(75,'JioCinema','https://www.jiocinema.com'),(76,'Shaadi.com','https://www.shaadi.com'),(77,'Team-BHP','https://www.team-bhp.com'),(78,'Zivame','https://www.zivame.com'),(79,'SpiceJet','https://www.spicejet.com'),(80,'Zopper','https://www.zopper.com'),(81,'BloombergQuint','https://www.bloombergquint.com'),(82,'Swirlr','https://www.swirlr.com'),(83,'PVR Cinemas','https://www.pvrcinemas.com'),(84,'LensCrafters','https://www.lenscrafters.com'),(85,'Furlenco','https://www.furlenco.com'),(86,'FreshToHome','https://www.freshtohome.com'),(87,'Saregama','https://www.saregama.com'),(88,'ClickIndia','https://www.clickindia.com'),(89,'Tata Sky','https://www.tatasky.com'),(90,'Ola Cabs','https://www.olacabs.com'),(91,'Pepperfry','https://www.pepperfry.com'),(92,'Koovs','https://www.koovs.com'),(93,'ClearTax','https://www.cleartax.in'),(94,'MakeMyTrip','https://www.makemytrip.com'),(95,'Reliance Digital','https://www.reliancedigital.in'),(96,'Droom','https://www.droom.in'),(97,'Nykaa','https://www.nykaa.com'),(98,'Deliveroo','https://www.deliveroo.in'),(99,'Shoppers Stop','https://www.shoppersstop.com'),(100,'Wynk Music','https://www.wynk.in');
/*!40000 ALTER TABLE `websites` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-28  2:59:31
