CREATE DATABASE  IF NOT EXISTS `mmh` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `mmh`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: mmh
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `id` varchar(200) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES ('ChIJ-ZogKrvMj4ARKrML-5D1a88','Alum Rock Park',NULL,NULL),('ChIJ41IqMUH6loARzXdWQwR2YIY','Yosemite National Park',NULL,NULL),('ChIJ4egP629-j4ARHEBOhfGLwGU','Billy Goat Hill Park',NULL,NULL),('ChIJ79wUZGoUkFQRdN-YP4SnvZ0','Island Center Forest',NULL,NULL),('ChIJ9bv3LrFqkFQRotc0wVEyvuA','Pinnacle Peak',NULL,NULL),('ChIJAwaRsA9xkFQRYP2uR9cF8yA','Soaring Eagle Regional Park',NULL,NULL),('ChIJefPVfDnyloARf_Bi2Am4V34','Yosemite Valley',NULL,NULL),('ChIJO30s5HQyjoAR1km_IFPiyII','Hellyer County Park',NULL,NULL),('ChIJP9-SDpjIj4ARgXa4S8VffAI','Penitencia Creek',NULL,NULL),('ChIJx4k2vnwrjoAR69PynJxw_DQ','Joseph D. Grant County Park',NULL,NULL),('ChIJxf8hxP9vkFQRWyyK_MWk_J8','Taylor Mountain Forest',NULL,NULL),('ChIJz_zKsizEj4ARGklZQxfB4Pw','Mission Peak Regional Preserve',NULL,NULL),('EiAzMTkgQmVybmFsIFJkLCBFZGVudmFsZSwgQ0EsIFVTQQ','Rocky Ridge Trail',NULL,NULL),('Eio5ODAgSmFja3BpbmUgU3QsIFRhaG9lIENpdHksIENBIDk2MTQ1LCBVU0E','Tahoe Rim Trail',NULL,NULL),('EjgxNTE4NC0xNTE4NiBQZW5pdGVuY2lhIENyZWVrIFJkLCBTYW4gSm9zZSwgQ0EgOTUxMzIsIFVTQQ','Alum Rock Park',NULL,'2016-07-28 14:45:58');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-29 23:57:23
