/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - skindb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`skindb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `skindb`;

/*Table structure for table `images` */

DROP TABLE IF EXISTS `images`;

CREATE TABLE `images` (
  `name` varchar(2000) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `images` */

insert  into `images`(`name`,`description`) values ('Actinic Keratoses (Solar Keratoses) or intraepithelial Carcinoma (Bowen’s disease)','Actinic Keratoses (Solar Keratoses) or intraepithelial Carcinoma (Bowen’s disease)'),('Basal Cell Carcinoma','Basal Cell Carcinoma'),('Benign Keratosis','Benign Keratosis'),('Dermatofibroma','Dermatofibroma'),('Melanoma','Melanoma'),('Melanocytic Nevi','Melanocytic Nevi'),('Vascular skin lesion','Vascular skin lesion');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`id`,`username`,`password`,`email`,`mobile`,`address`) values (1,'chotu','123','chotu.1000projects@gmail.com','7702177291','hyd'),(2,'moulali','123','moulalicce225@gmail.com','7702177291','15-8-424');

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`id`,`name`,`image`,`username`) values (16,'dfdf','a.jpg','chotu');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
