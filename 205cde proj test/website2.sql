-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2020-04-18 15:21:10
-- 伺服器版本： 10.4.11-MariaDB
-- PHP 版本： 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `website2`
--

-- --------------------------------------------------------

--
-- 資料表結構 `animal`
--

CREATE TABLE `animal` (
  `animal_id` int(11) NOT NULL,
  `animal_name` varchar(10) NOT NULL,
  `years_old` int(3) NOT NULL,
  `disease` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `animal`
--

INSERT INTO `animal` (`animal_id`, `animal_name`, `years_old`, `disease`) VALUES
(1, 'Doe', 9, 'Diabetes'),
(2, 'SoSo', 10, 'Arthritis'),
(3, 'QQ', 3, 'Lymphoma'),
(4, 'Judy', 6, 'Feline Immunodeficiency Virus'),
(5, 'Rex', 6, 'Parvovirus'),
(6, 'GT', 5, 'Leg injury'),
(8, 'Render', 11, 'Unknown'),
(9, 'Don', 12, 'Ringworm');

-- --------------------------------------------------------

--
-- 資料表結構 `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `feed_type` varchar(10) NOT NULL,
  `comment` varchar(1000) NOT NULL,
  `feed_email` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `feedback`
--

INSERT INTO `feedback` (`feedback_id`, `rating`, `feed_type`, `comment`, `feed_email`) VALUES
(1, 8, 'Comments', 'Good', 'soakd5@mediafire.com'),
(2, 6, 'Comments', 'Good attempt.', 'pthorl@feedburner.com'),
(3, 5, 'Questions', 'Can I go  to your store and see the animals?', 'dmurr1@netvibes.com'),
(4, 4, 'Comments', 'Background looks quite bad.', 'fyorston2@zimbio.com'),
(5, 6, 'Comments', 'Hello', 'wfrisdi8@dropbox.com'),
(6, 6, 'Questions', 'Is there any receipt for my payment?', 'mfrangi@hostgator.com'),
(7, 6, 'Comments', 'Good website and carry on.', 'rvettorh@wufoo.com'),
(8, 4, 'Comments', 'Not good', 'bmacalor@sohu.com'),
(9, 5, 'Comments', 'It\'s ok', 'bjestb@csmonitor.com'),
(10, 8, 'Comments', 'Animals are so cute.', 'asyder5@twitpic.com'),
(11, 3, 'Comments', 'hi', 'lscattergo@skype.com'),
(12, 6, 'Comments', 'Good stuff', 'kcastelloj@icq.com'),
(13, 3, 'Comments', 'qwe', 'csarfatt@bloglovin.com'),
(14, 6, 'Comments', 'ok', 'lmechell8@mlb.com'),
(15, 5, 'Questions', 'What is your shop opening hours?', 'gga@gmail.com'),
(16, 6, 'Comments', 'Quite good', 'b@a.cm');

-- --------------------------------------------------------

--
-- 資料表結構 `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `username` varchar(15) DEFAULT NULL,
  `credit_type` varchar(50) DEFAULT NULL,
  `credit_no` varchar(16) DEFAULT NULL,
  `expir_month` int(2) DEFAULT NULL,
  `expir_year` int(4) DEFAULT NULL,
  `cvv` int(3) DEFAULT NULL,
  `money` varchar(50) DEFAULT NULL,
  `animal_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `payment`
--

INSERT INTO `payment` (`payment_id`, `name`, `username`, `credit_type`, `credit_no`, `expir_month`, `expir_year`, `cvv`, `money`, `animal_name`) VALUES
(1, 'Esteban Flecknoe', 'odeamer1', 'visa', '3014336868232669', 1, 2022, 122, '750', 'Doe'),
(2, 'Wilhelmine Punton', 'qrqewr', 'jcb', '3571101280240028', 12, 2020, 289, '2160', 'GT'),
(3, 'Dierdre Capstack', 'jwalcherc', 'master', '6763379027581060', 3, 2021, 365, '2915', 'QQ'),
(4, 'Korella Pavis', 'jdemarco4', 'visa', '9742577174114455', 4, 2021, 422, '1910', 'QQ'),
(5, 'Carroll Moggle', 'ngore', 'visa', '6049359815715891', 5, 2023, 518, '2270', 'SoSo'),
(6, 'Trenton Brimble', 'vmonce7', 'master', '3742832125459339', 6, 2022, 622, '1680', 'Doe'),
(7, 'Alain Di Dello', 'jwalcherc', 'jcb', '5602217298992158', 7, 2024, 643, '1600', 'Rex'),
(8, 'Ray Cao', 'rbourdon9', 'jcb', '3552379639867625', 8, 2022, 854, '6000', 'Judy'),
(9, 'sam', 'abc', 'visa', '2233445566887659', 12, 2020, 233, '227', 'Doe'),
(10, 'sam', 'abc', 'visa', '2233445566887659', 12, 2020, 233, '2200', 'SoSo'),
(11, 'w4e', 'abc', 'visa', '2233445566887659', 12, 2020, 667, '550', 'Judy'),
(12, 'Coe', 'strenam2', 'master', '4354386377880005', 5, 2023, 324, '1500', 'Rex'),
(13, 'Joe', 'gtorou', 'visa', '5544233444455555', 9, 2023, 356, '500', 'Doe');

-- --------------------------------------------------------

--
-- 資料表結構 `website`
--

CREATE TABLE `website` (
  `id` int(11) NOT NULL,
  `username` varchar(15) NOT NULL,
  `email` varchar(25) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `website`
--

INSERT INTO `website` (`id`, `username`, `email`, `password`) VALUES
(1, 'ngore', 'ngore@gmail.com', '12345678'),
(2, 'odeamer1', 'kblaszczyk1@google.pl', 'kbla23'),
(3, 'strenam2', 'ballone2@npr.org', 'bal3'),
(4, 'ckelcey3', 'aable3@huffingtonpost.com', 'VuCLSzl'),
(5, 'jdemarco4', 'mranking4@gmail.com', '2266'),
(18, 'abc', 'abc@yahoo.com', '22333'),
(25, 'gtorou', 'gtorou@gmail.com', '443333'),
(27, 'admin', 'adminan@gmail.com', '11222'),
(30, 'tuutyu', 'tuutyu@trh.com', '45555'),
(31, '55ya', '55ya@gmail.com', '55y5'),
(33, 'rhtr', 'rhtr@gmail.com', '22333'),
(34, 'efweg', 'efweg@abc.com', '7896'),
(35, 'aacc', 'aacc@gmail.com', 'aacc2');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `animal`
--
ALTER TABLE `animal`
  ADD PRIMARY KEY (`animal_id`),
  ADD UNIQUE KEY `animal_id` (`animal_id`);

--
-- 資料表索引 `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- 資料表索引 `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD UNIQUE KEY `payment_id` (`payment_id`);

--
-- 資料表索引 `website`
--
ALTER TABLE `website`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `animal`
--
ALTER TABLE `animal`
  MODIFY `animal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `website`
--
ALTER TABLE `website`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
