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

CREATE TABLE damages (
  damage_id INT NOT NULL AUTO_INCREMENT,
  type varchar(50),
  PRIMARY KEY (damage_id)
 );
 
CREATE TABLE house_damages (
  house_id INT NOT NULL,
  damage_id INT NOT NULL,
  cost INT NOT NULL,
  FOREIGN KEY (house_id)
  REFERENCES basicHouse (house_id),
  FOREIGN KEY (damage_id)
  REFERENCES damages (damage_id)
  
);

