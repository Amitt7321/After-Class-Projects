CREATE TABLE STUDENT ( 
    Roll_No INT PRIMARY KEY, 
    Name VARCHAR(50), 
    Class VARCHAR(10), 
    Marks INT, 
    City VARCHAR(50) 
); 

INSERT INTO STUDENT (Roll_No, Name, Class, Marks, City) VALUES 
(1, 'Arin sen', '7th', 90, 'West Bengal'), 
(2, 'Amitt Sharma', '7th', 96, 'Haryana'), 
(3, 'Atharva Raj Dubey', '7th', 92, 'Uttar Pradesh'), 
(4, 'Aadarsh Alok Tiwari', '7th', 67, 'Bihar');

SELECT Roll_No, Name, Marks, City 
FROM STUDENT 
WHERE Marks > 80;