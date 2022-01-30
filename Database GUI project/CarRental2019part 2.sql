CREATE TABLE CUSTOMER
(
  CustId INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  Phone VARCHAR(100),
  PRIMARY KEY(CustId)
);

CREATE TABLE RATE
(
  Type INT NOT NULL,
  Category	INT(1) ,
  Weekly	INT,
  Daily	INT,
  PRIMARY KEY (Type, Category)
);

CREATE TABLE VEHICLE
(
  VehicleID	INT	NOT NULL,
  Description	VARCHAR(25)	NOT NULL,
  Year VARCHAR(4)	NOT NULL,
  Type	INT,
  Category	INT,
  PRIMARY KEY(VehicleID),
  FOREIGN KEY (Type, Category) REFERENCES rate (Type, Category) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RENTAL
(
    CustId	INT	NOT NULL,
    VehicleId	INT	NOT NULL,
    StartDate	DATE	,
    OrderDate	DATE ,
    RentalType	INT	DEFAULT '1',
    Qty	INT	DEFAULT '1',
    ReturnDate DATE,
    TotalAmount INT,
    PaymentDate DATE,
    
    FOREIGN KEY(VehicleId) REFERENCES VEHICLE(VehicleId),
	FOREIGN KEY(CustId) REFERENCES CUSTOMER(CUSTId)
);
--Import tables from CSV files

--CUSTOMER

.mode CSV
.import --csv --skip 1 customer.csv Customer


--Rate
.mode CSV
.import --csv --skip 1 rate.csv Rate

--Vehcile 

.mode CSV
.import --csv --skip 1 vehicle.csv Vehicle

--Rental 
.mode CSV
.import --csv --skip 1 rental.csv Rental


