DROP DATABASE estateFinderDB;
CREATE DATABASE IF NOT EXISTS estateFinderDB;

USE estateFinderDB;

CREATE TABLE basicHouse  (
  house_id INT NOT NULL AUTO_INCREMENT,
  address VARCHAR(50) NOT NULL,
  county VARCHAR(40),
  state VARCHAR(2),
  price INT, 
  PRIMARY KEY (house_id),
  INDEX(address)
);

insert into basicHouse (address,county,state,price) values ('6543 East Avenue','Fredericksburg','VA',329000);
insert into basicHouse (address,county,state,price) values ('6545 East Avenue','Fredericksburg','VA',49000);
insert into basicHouse (address,county,state,price) values ('4631 Yamaha Lane','Baltimore','MD',100000);
insert into basicHouse (address,county,state,price) values ('16 Waterloo Street','Fredericksburg','VA',50000);
insert into basicHouse (address,county,state,price) values ('3049 Hawke Street','Fredericksburg','VA',49000);
insert into basicHouse (address,county,state,price) values ('1192 Hill Avenue','Chantilly','VA',100000);
insert into basicHouse (address,county,state,price) values ('2148 Stank Street','Fredericksburg','VA',1000000);
insert into basicHouse (address,county,state,price) values ('19 Gravel Avenue','Fredericksburg','VA',350000);
insert into basicHouse (address,county,state,price) values ('4631 Basalt Circle','baltimore','MD',120000);
insert into basicHouse (address,county,state,price) values ('1111 Hokey Pokey Court','Stafford','VA',50000);
insert into basicHouse (address,county,state,price) values ('942 Stannity Street','Waldorf','MD',49000);
insert into basicHouse (address,county,state,price) values ('2353 Main Street','Baltimore','MD',100000);

CREATE TABLE house_damages (
  house_id INT NOT NULL,
  cost INT NOT NULL,
  type varchar(50),
  FOREIGN KEY (house_id)
  REFERENCES basicHouse (house_id)
);

insert into house_damages (house_id,type,cost) values (1,'water',1000);
insert into house_damages (house_id,type,cost) values (2,'fire',1500);
insert into house_damages (house_id,type,cost) values (3,'neglect',900);
insert into house_damages (house_id,type,cost) values (3,'pests',300);
insert into house_damages (house_id,type,cost) values (3,'plumbing',1200);
insert into house_damages (house_id,type,cost) values (4,'vandalism',500);
insert into house_damages (house_id,type,cost) values (5,'water',1000);
insert into house_damages (house_id,type,cost) values (6,'fire',1500);
insert into house_damages (house_id,type,cost) values (7,'water',900);
insert into house_damages (house_id,type,cost) values (8,'roof',1700);
insert into house_damages (house_id,type,cost) values (9,'fire',1500);
insert into house_damages (house_id,type,cost) values (10,'water',900);
insert into house_damages (house_id,type,cost) values (11,'roof',1700);
insert into house_damages (house_id,type,cost) values (12,'roof',1700);



CREATE TABLE users (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(12) NOT NULL,
  `password` varchar(256) NOT NULL,
  `zipcode` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;