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

CREATE TABLE damages (
  damage_id INT NOT NULL AUTO_INCREMENT,
  type varchar(50),
  PRIMARY KEY (damage_id)
 );
 
insert into damages (type) values ('water damage');
insert into damages (type) values ('fire damage');
insert into damages (type) values ('vandalism');
insert into damages (type) values ('roof damage');
insert into damages (type) values ('pests');
 
CREATE TABLE house_damages (
  house_id INT NOT NULL,
  damage_id INT NOT NULL,
  cost INT NOT NULL,
  FOREIGN KEY (house_id)
  REFERENCES basicHouse (house_id),
  FOREIGN KEY (damage_id)
  REFERENCES damages (damage_id)
  
);

insert into house_damages (house_id,damage_id,cost) values (1,1,1000);
insert into house_damages (house_id,damage_id,cost) values (2,3,1500);
insert into house_damages (house_id,damage_id,cost) values (2,1,900);
insert into house_damages (house_id,damage_id,cost) values (3,3,500);