DROP DATABASE estateFinderDB;
CREATE DATABASE IF NOT EXISTS estateFinderDB;

USE estateFinderDB;

CREATE TABLE basicHouse  (
  house_id INT NOT NULL AUTO_INCREMENT,
  address VARCHAR(50) NOT NULL,
  county VARCHAR(40),
  state VARCHAR(2),
  price INT, 
  PRIMARY KEY (house_id)
);

insert into basicHouse (address,county,state,price) values ('6543 east ave','fred','va',50000);
insert into basicHouse (address,county,state,price) values ('6545 east ave','fred','va',49000);
insert into basicHouse (address,county,state,price) values ('4631 yamaha ln','baltimore','md',100000);
 
CREATE TABLE house_damages (
  house_id INT NOT NULL,
  cost INT NOT NULL,
  type varchar(50),
  FOREIGN KEY (house_id)
  REFERENCES basicHouse (house_id)
);

insert into house_damages (house_id,type,cost) values (1,'water damage',1000);
insert into house_damages (house_id,type,cost) values (2,'fire damage',1500);
insert into house_damages (house_id,type,cost) values (2,'sabotage',900);
insert into house_damages (house_id,type,cost) values (3,'plumbing',500);