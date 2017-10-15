-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 15, 2017 at 06:28 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment`
--

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `qnum` int(2) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `ques` varchar(80) DEFAULT NULL,
  `op1` varchar(85) DEFAULT NULL,
  `op2` varchar(85) DEFAULT NULL,
  `op3` varchar(85) DEFAULT NULL,
  `op4` varchar(85) DEFAULT NULL,
  `corA` varchar(85) DEFAULT NULL,
  `qid` int(5) DEFAULT NULL,
  `_cour` varchar(45) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`qnum`, `type`, `ques`, `op1`, `op2`, `op3`, `op4`, `corA`, `qid`, `_cour`) VALUES
(1, 'MCQ', 'WHAT IS 2-5?', '+3', '-3', '+2', '-2', '2', 123, 'ADVANCED PROGRAMMING'),
(2, 'T/F', '3<-3?', 'TRUE', 'FALSE', NULL, NULL, '2', 123, 'ADVANCED PRROGRAMMING'),
(3, 'NUMERIC', 'WHO IS SHAHID AFRIDI?', NULL, NULL, NULL, NULL, 'Cricketer', 123, 'ADVANCED PROGRAMMINE'),
(4, 'T/F', 'adaf', 'adafd', 'adfa', NULL, NULL, 'a', 132, 'adfadf'),
(1, 'MCQ', 'adf', 'adf', 'adf', 'ada', 'dsasd', 'asdad', 122, 'Advanced PRogramming'),
(1, 'T/F', 'asdf', 'asdf', 'asdfa', NULL, NULL, 'adfasd', 123, 'asdvanadf'),
(4, 'MCQ', '', '', 'adsf', 'asd', '', 's', 23, 'adf'),
(4, 'MCQ', '', '', 'adsf', 'asd', '', 's', 23, 'adf'),
(4, 'MCQ', '', 'asdfad', 'adsf', 'asd', '', 's', 23, 'adf'),
(5, 'NUMERIC', 'ADFA', NULL, NULL, NULL, NULL, 'ADFAD', 33, 'ADFAS'),
(1, 'T/F', 'ADFAD', 'ASDA', 'ADSFAD', NULL, NULL, 'ADSFA', 22, 'ADFASD'),
(3, 'MCQ', 'a', '', '', 'sdfa', 'dfadfadadsf', 'asd', 33, 'asdfad'),
(3, 'MCQ', 'fadfa', 'asdfads', 'sdfasdf', 'adfa', 'dfadf', 'adfadf', 322, 'asdfasd'),
(6, 'MCQ', '', 'adfadf', '', 'adf', '', '', 33, 'adf'),
(2, 'NUMERIC', 'asdfs', NULL, NULL, NULL, NULL, 'adsfd', 33, 'dsasd'),
(3, 'T/F', '', 'asdfa', 'dasfd', NULL, NULL, '', 3333, 'asdfad'),
(1, 'MCQ', 'asdf', 'adfadsfads', 'fadsf', 'fadfad', 'adsfadfad', 'fad', 676, 'Advanced');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `_name` varchar(25) DEFAULT NULL,
  `reg` int(6) DEFAULT NULL,
  `quNum` int(5) DEFAULT NULL,
  `marks` varchar(5) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`_name`, `reg`, `quNum`, `marks`) VALUES
('Hazal Kaya', 1, 1, '1'),
('Hazal Kaya', 1, 1, '0'),
('Hazal Kaya', 1, 1, '1'),
('Student', 120168, 1, '0');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`, `password`) VALUES
(124494, 'Tayyab Salman', 'tayyab'),
(158842, 'Beren Saat', 'beren'),
(758846, 'Hazal Kaya', 'hazal'),
(595586, 'Daenerys Targaryen', 'daenerys');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=758847;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
