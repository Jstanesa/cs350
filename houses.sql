DROP DATABASE estateFinderDB;
CREATE DATABASE IF NOT EXISTS estateFinderDB;
GRANT ALL PRIVILEGES ON estateFinderDB.* to 'estate'@'localhost';
identified by 'blogPassword';
USE estateFinderDB;


CREATE TABLE basicHouse 
(
  address VARCHAR(50) NOT NULL,
  dateListed DATE,
  county VARCHAR(40),
  state VARCHAR(2),
  price INT(5)
);

INSERT INTO basicHouse VALUES ('20659 Frazier Way', '08-12-27', 'Mechanicsville', 'MD', 156459);
INSERT INTO basicHouse VALUES ('306 Applegate Drive', '12-8-13', 'Stafford', 'VA', 205650);
INSERT INTO basicHouse VALUES ('3058 Dinger Drive', '14-01-10', 'Fredericksburg', 'VA', 300000);
INSERT INTO basicHouse VALUES ('2090 Colgate Way', '06-05-27', 'Spotsylvania', 'VA', 450000);
INSERT INTO basicHouse VALUES ('709 Billard Circle', '12-03-05', 'Fredericksburg', 'VA', 315000);
INSERT INTO basicHouse VALUES ('101 Leonard Court', '12-07-19', 'Fredericksburg', 'VA', 175000);
INSERT INTO basicHouse VALUES ('908 Granite Drive', '13-09-16', 'Stafford', 'VA', 379000);
INSERT INTO basicHouse VALUES ('203 Dingleberry Drive', '08-01-10', 'Fredericksburg', 'VA', 50000);

/*CREATE TABLE houseChars (      
  houseAdd VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES basicHouse(address),
  color VARCHAR(15),
  garage VARCHAR(40),
  bedrooms VARCHAR(2),
  bathrooms DECIMAL(5,1),
  size INT                    
);*/