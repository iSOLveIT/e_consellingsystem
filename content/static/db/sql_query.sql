--Select database
use app;

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

INSERT INTO `user` (`user_id`, `first_name`, `last_name`, `school_email`, `password`, `gender`,`phone_number`,`date_of_birth`,`level`,`optional_email`,`programme`,`faculty_or_office`, `is_admin`) VALUES
('10063460', 'Daniel','Appiah','10063460@upsamail.edu.gh','$5$rounds=535000$JfsmDYJKixyfI9jc$SFWVpiEmEzOurgW6Cv7pPpOfz0Vjmp7PuBoSfsG7ZOC','M','0554779371','2018-07-23',300,'daniel@gmail.com','IT Management','Information Technology & Communication Studies',false ),
('admin1', 'Samuel','Mensah','samuel@upsamail.edu.gh','$5$rounds=535000$JfsmDYJKixyfI9jc$SFWVpiEmEzOurgW6Cv7pPpOfz0Vjmp7PuBoSfsG7ZOC','M','0554779371','2018-07-23',300,'samuel@gmail.com','IT Management','Information Technology & Communication Studies', true),
('10087872', 'Randy','Duodu','10087872@upsamail.edu.gh','$5$rounds=535000$JfsmDYJKixyfI9jc$SFWVpiEmEzOurgW6Cv7pPpOfz0Vjmp7PuBoSfsG7ZOC','M','0554779371','2018-07-23',300,'randy@gmail.com','IT Management','Information Technology & Communication Studies', false ),
('staff2', 'Ignatius','Osei','osei@upsamail.edu.gh','$5$rounds=535000$JfsmDYJKixyfI9jc$SFWVpiEmEzOurgW6Cv7pPpOfz0Vjmp7PuBoSfsG7ZOC','M','0554779371','2018-07-23',300,'ignatius@gmail.com','IT Management','Information Technology & Communication Studies', false ),
('admin2', 'Joseph','Sefah','10090527@upsamail.edu.gh','$5$rounds=535000$JfsmDYJKixyfI9jc$SFWVpiEmEzOurgW6Cv7pPpOfz0Vjmp7PuBoSfsG7ZOC','M','0554779371','2018-07-23',300,'joseph@gmail.com','IT Management','Information Technology & Communication Studies', true );


#Table structure for table `appointment`
DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(11) NOT NULL,
  `problem` text NOT NULL,
  `appointment_tag` varchar(10) NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` time NOT NULL,
  `recommendation` text,
  `assigned` bit NOT NULL DEFAULT 0,
  `assigned_admin_id` varchar(10),
PRIMARY KEY (`id`)
);

INSERT INTO `appointment` (`user_id`, `problem`, `appointment_tag`, `appointment_date`, `appointment_time`, `assigned`) VALUES
('10087872', 'Marital Issues','aptag1000','2018-07-23','14:09:14',1 ),
('staff1', 'Marital Issues','aptag1008','2018-07-23','14:09:14',0 ),
('10063460', 'Relatinship Issues','aptag1010','2019-07-24','18:09:18',1);

#Table structure for table `recommendations`
DROP TABLE IF EXISTS `recommendations`;
CREATE TABLE IF NOT EXISTS `recommendations` (
  `recommend_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` varchar(10) NOT NULL,
  `name_of_counsellor` varchar(255) NOT NULL,
  `solution` text,
  `appointment_tag` varchar(10) NOT NULL,
  `recommendation_date` date NOT NULL,
  `recommendation_time` time NOT NULL,
  PRIMARY KEY (`recommend_id`));

INSERT INTO `recommendations` (`admin_id`,`name_of_counsellor`, `solution`,`appointment_tag`, `recommendation_date`, `recommendation_time`) VALUES
('admin1','Samuel Mensah', 'Note to help you.','aptag1008','2018-07-23','14:09:14');


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
