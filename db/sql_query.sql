--Select database
USE your_database_name;


-- Table structure for table `appointment`
DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(11) NOT NULL,
  `problem` text NOT NULL,
  `appointment_tag` varchar(10) NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` time NOT NULL,
  `assigned` varchar(1) DEFAULT '0',
  `assigned_admin_id` varchar(10),
  PRIMARY KEY (`id`), 
  foreign key(`assigned_admin_id`) references admin_profile(`admin_id`)
);

INSERT INTO `appointment` (`user_id`, `problem`, `appointment_tag`, `appointment_date`, `appointment_time`, `assigned`) VALUES
('10087872', 'Marital Issues','aptag1000','2018-07-23','14:09:14','0' ),
('staff1', 'Marital Issues','aptag1008','2018-07-23','14:09:14','0' ),
('10084947', 'Relatinship Issues','aptag1010','2019-07-24','18:09:18','0');


--Table structure for table `student`
DROP TABLE IF EXISTS `student_profile`;
CREATE TABLE IF NOT EXISTS `student_profile` (
  `student_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `student_email` varchar(255),
  `password` varchar(255) NOT NULL,
  `gender` char(1) NOT NULL,
  `phone_number` text(10) NOT NULL,
  `date_of_birth` date NOT NULL,
  `level` int(3) NOT NULL,
  `optional_email` varchar(255),
  `account_created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `account_modified_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `programme` varchar(255),
  `faculty` varchar(255),
  PRIMARY KEY (`student_id`)
);

INSERT INTO `student_profile` (`student_id`, `first_name`, `last_name`, `student_email`, `password`, `gender`,`phone_number`,`date_of_birth`,`level`,`optional_email`,`programme`,`faculty`) VALUES
(10063460, 'Daniel','Appiah','10063460@upsamail.edu.gh','10063640','M','0554779371','2018-07-23',300,'daniel@gmail.com','IT Management','Information Technology & Communication Studies' ),
(10084947, 'Samuel','Mensah','100849470@upsamail.edu.gh','10084947','M','0554779371','2018-07-23',300,'samuel@gmail.com','IT Management','Information Technology & Communication Studies' ),
(10087872, 'Randy','Duodu','10087872@upsamail.edu.gh','10087872','M','0554779371','2018-07-23',300,'randy@gmail.com','IT Management','Information Technology & Communication Studies' ),
(10084318, 'Ignatius','Osei','10084318@upsamail.edu.gh','10084318','M','0554779371','2018-07-23',300,'ignatius@gmail.com','IT Management','Information Technology & Communication Studies' ),
(10090527, 'Joseph','Sefah','10090527@upsamail.edu.gh','10090527','M','0554779371','2018-07-23',300,'joseph@gmail.com','IT Management','Information Technology & Communication Studies' );


--Table structure for table `admin`
DROP TABLE IF EXISTS `admin_profile`;
CREATE TABLE IF NOT EXISTS `admin_profile` (
  `admin_id` varchar(10) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `school_email` varchar(255),
  `password` varchar(255) NOT NULL,
  `gender` char(1) NOT NULL,
  `phone_number` text(10) NOT NULL,
  `date_of_birth` date NOT NULL,
  `optional_email` varchar(255),
  `account_created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `account_modified_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `faculty_or_office` varchar(255),
  PRIMARY KEY (`admin_id`)
);

INSERT INTO `admin_profile` (`admin_id`, `first_name`, `last_name`, `school_email`, `password`, `gender`,`phone_number`,`date_of_birth`,`optional_email`,`faculty_or_office`) VALUES
('admin1', 'Daniel','Appiah','daniel@upsamail.edu.gh','admin1','M','0554779371','2018-07-23','daniel@gmail.com','Information Technology & Communication Studies' ),
('admin2', 'Samuel','Mensah','samuel@upsamail.edu.gh','admin2','M','0554779371','2018-07-23','samuel@gmail.com','Information Technology & Communication Studies' ),
('admin3', 'Randy','Duodu','randy@upsamail.edu.gh','admin3','M','0554779371','2018-07-23','randy@gmail.com','Information Technology & Communication Studies' ),
('admin4', 'Ignatius','Osei','osei@upsamail.edu.gh','admin4','M','0554779371','2018-07-23','osei@gmail.com','Information Technology & Communication Studies' ),
('admin5', 'Joseph','Sefah','joseph@upsamail.edu.gh','admin5','M','0554779371','2018-07-23','joseph@gmail.com','Information Technology & Communication Studies' );


--Table structure for table `staff`
DROP TABLE IF EXISTS `staff_profile`;
CREATE TABLE IF NOT EXISTS `staff_profile` (
  `staff_id` varchar(10) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `staff_email` varchar(255),
  `password` varchar(255) NOT NULL,
  `gender` char(1) NOT NULL,
  `phone_number` text(10) NOT NULL,
  `date_of_birth` date NOT NULL,
  `optional_email` varchar(255),
  `account_created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `account_modified_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `faculty_or_office` varchar(255),
  PRIMARY KEY (`staff_id`)
);

INSERT INTO `staff_profile` (`staff_id`, `first_name`, `last_name`, `staff_email`, `password`, `gender`,`phone_number`,`date_of_birth`,`optional_email`,`faculty_or_office`) VALUES
('staff1', 'Daniel','Appiah','daniel@upsamail.edu.gh','staff1','M','0554779371','2018-07-23','daniel@gmail.com','Information Technology & Communication Studies' ),
('staff2', 'Samuel','Mensah','samuel@upsamail.edu.gh','staff2','M','0554779371','2018-07-23','samuel@gmail.com','Information Technology & Communication Studies' ),
('staff3', 'Randy','Duodu','randy@upsamail.edu.gh','staff3','M','0554779371','2018-07-23','randy@gmail.com','Information Technology & Communication Studies' ),
('staff4', 'Ignatius','Osei','osei@upsamail.edu.gh','staff4','M','0554779371','2018-07-23','osei@gmail.com','Information Technology & Communication Studies' ),
('staff5', 'Joseph','Sefah','joseph@upsamail.edu.gh','staff5','M','0554779371','2018-07-23','joseph@gmail.com','Information Technology & Communication Studies' );


--Table structure for table `recommendations`
DROP TABLE IF EXISTS `recommendations`;
CREATE TABLE IF NOT EXISTS `recommendations` (
  `recommend_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` varchar(10) NOT NULL,
  `name_of_counsellor` varchar(255) NOT NULL,
  `problem` text NOT NULL,
  `solution` text NOT NULL,
  `appointment_tag` varchar(10) NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` time NOT NULL,
  PRIMARY KEY (`recommend_id`),
  foreign key(`admin_id`) references admin_profile(`admin_id`)
);

INSERT INTO `recommendations` (`admin_id`,`name_of_counsellor`, `problem`, `solution`,`appointment_tag`, `appointment_date`, `appointment_time`) VALUES
('admin1','Daniel Appiah', 'Marital Issues','Note to help you.','aptag1000','2018-07-23','14:09:14'),
('admin2','Samuel Mensah', 'Marital Issues','Note to help you.','aptag1008','2018-07-23','14:09:14'),
('admin5','Joseph Sefah', 'Relationship Issues','Note to help you.','aptag1010','2018-07-23','14:09:14');
