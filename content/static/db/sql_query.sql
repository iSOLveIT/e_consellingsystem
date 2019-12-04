

#Changes


# Table for users
DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `user_id` varchar(10) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `school_email` varchar(255),
  `password` varchar(255) NOT NULL,
  `gender` char(1) NOT NULL,
  `phone_number` text(10) NOT NULL,
  `date_of_birth` date NOT NULL,
  `level` int(3),
  `optional_email` varchar(255),
  `account_created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `account_modified_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `programme` varchar(255),
  `faculty_or_office` varchar(255),
  `is_admin` boolean NOT NULL,
  PRIMARY KEY (`user_id`)
);



#Table structure for table `appointment`
DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(11) NOT NULL,
  `problem` text NOT NULL,
  `appointment_tag` varchar(10) NOT NULL,
  `appointDate_Time` datetime NOT NULL,
  `recommendation` text,
  `assigned` bit NOT NULL DEFAULT 0,
  `assigned_admin_id` varchar(10),
  `terms` bit NOT NULL DEFAULT 1,
PRIMARY KEY (`id`)
);



#Table structure for table `recommendations`
DROP TABLE IF EXISTS `recommendations`;
CREATE TABLE IF NOT EXISTS `recommendations` (
  `recommend_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` varchar(10) NOT NULL,
  `name_of_counsellor` varchar(255) NOT NULL,
  `solution` text,
  `appointment_tag` varchar(10) NOT NULL,
  `recommendation_date_time` datetime NOT NULL,
  PRIMARY KEY (`recommend_id`));

INSERT INTO `recommendations` (`admin_id`,`name_of_counsellor`, `solution`,`appointment_tag`, `recommendation_date_time`) VALUES
('admin1','Samuel Mensah', 'Note to help you.','aptag1008','2018-07-23 14:09:14');


#Table structure for table `email_database`
DROP TABLE IF EXISTS `email_database`;
CREATE TABLE IF NOT EXISTS `email_database` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_name` varchar(255) NOT NULL,
  `sender_email` varchar(255) NOT NULL,
  `subject` varchar(255) ,
  `body` text NOT NULL,
  `check_policy` boolean not null default 0,
  `email_sent_on` datetime NOT NULL,
PRIMARY KEY (`id`)
);
