CREATE TABLE ARTADMIN
(
admin_username varchar(20),
admin_email varchar(50),
admin_password varchar(20),
primary key(admin_username)
);

INSERT INTO ARTADMIN (admin_username,admin_email,admin_password) VALUES('Jenisa Merlin','jm@gmail.com','djm1234');
INSERT INTO ARTADMIN (admin_username,admin_email,admin_password) VALUES('Beulah Daniel','db@gmail.com','dbd4321');
INSERT INTO ARTADMIN (admin_username,admin_email,admin_password) VALUES('Jenisa','jm@gmail.com','djm');

SELECT * FROM ARTADMIN;

CREATE TABLE ARTIST
(
artist_name varchar(25),
artist_username varchar(25),
artist_password varchar(20),
artist_dob date,
artist_style varchar(20),
aadhar_num numeric(12),
artist_email varchar(40),
artist_mobNum numeric(10),
artist_place varchar(20),
primary key (artist_username)
);

INSERT INTO ARTIST (artist_name,artist_username,artist_password,artist_dob,artist_style,aadhar_num,artist_email,artist_mobNum,artist_place) VALUES('Leonarda da vinci','davinci','1298','1992-08-02','Renaissance',689754325678,'davinci@gmail.com',9765432167,'Italy');
SELECT * FROM ARTIST;
DROP TABLE ARTIST;
SELECT * FROM CUSTOMER;
CREATE TABLE CUSTOMER
(
cust_name varchar(25),
cust_username varchar(25),
cust_password varchar(20),
cust_aadhar_num numeric(12),
cust_email varchar(40),
cust_mobNum numeric(10),
cust_place varchar(20),
primary key (cust_username)
);

SELECT * FROM CUSTOMER;

INSERT INTO CUSTOMER (cust_name,cust_username,cust_password,cust_aadhar_num,cust_email,cust_mobNum,cust_place)
VALUES('Merlin','merl','1234',34567891234,'merl@gmail.com',9876543213,'chennai');
CREATE TABLE ART
(
art_id varchar(10),
art_title varchar(30),
art_price decimal(8,2),
art_type varchar(20),
art_year date,
primary key(art_id)
);
SELECT * FROM ART;
DROP TABLE ART;
CREATE TABLE ORDERS
(
cust_name varchar(25),
art_id varchar(10),
ord_num numeric(10),
ord_date date,
ord_payment varchar(15),
primary key(ord_num)
);

SELECT * FROM ORDERS;
ALTER TABLE ORDERS ADD FOREIGN KEY(cust_name) REFERENCES CUSTOMER(cust_username);
ALTER TABLE ORDERS ADD FOREIGN KEY(art_id) REFERENCES ART(art_id);

DROP TABLE ORDERS;

SELECT O.cust_name,O.art_id,O.ord_num,O.ord_date,O.ord_payment,A.art_price FROM ORDERS O INNER JOIN ART A WHERE O.art_id = A.art_id where O.ord_num = ;