--Add a new customer Query 
INSERt into Customer(CustId, Name, Phone)
SELECT MAX(CustId)+1, 'Robin', '(768)-786-8976'
FROM Customer;


Task 1 : 


# Query 1: #


alter table rental
add Returned int; 

update rental
set returned = 1
where PaymentDate = 'NULL';
select * from rental;

#Query 2: #


-- Task2
#Query 3: 

--For Free Vehicle 

select Vehicle.VehicleId, Vehicle.Type, Vehicle.Category
from Vehicle left join Rental on Vehicle.VehicleId = Rental.VehicleId
where Rental.VehicleID is NULL AND Category=1, Type = 6;

-- FoR Free Vehicle with User Input

select Vehicle.VehicleId
from Vehicle left join Rental on Vehicle.VehicleId = Rental.VehicleId
where Rental.VehicleID is NULL AND Category=?;
