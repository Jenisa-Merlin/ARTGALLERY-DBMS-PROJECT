# ARTGALLERY-DBMS-PROJECT

PSG COLLEGE OF TECHNOLOGY

DATA BASE MANAGEMENT SYSTEM PACKAGE SUMMARY

Submitted by,
Jenisa Merlin. D (21PW08)
AMCS DEPARTMENT
On,
08.11.2022

TOPIC: Art Gallery Management System
COURSE: DATABASE MANAGEMENT SYSTEM (20XW32)



ABOUT:
Art gallery management system is a platform where there are artists who upload their arts in gallery and the customer can order them which are managed by admin.
First there is a login page which has two options as admin customer.
1)Admin:
He has the control over all the functions.
Then signup page asks username and password once successfully logged in it will go to home page.
In home page you can see the gallery, customers, artists, artworks, orders and logout button.
In gallery, you can see all the artworks of the artists.
In customers, you can see their details, insert details, delete details.
In artists, you can see their details, insert details, delete details.
In artworks, you can see the details, insert artworks, delete artworks.
In orders, you can place orders, delete orders and also view orders.
2)Customer
You can place order by entering the art id of the artwork and can also view all the orders.

IMPLEMENTATION:
FRONT-END: HTML
BACKEND: Python
DATABASE: MySQL

ER DIAGRAM:

 

ARTIST
Artistusername(PK) artistname	artistpassword	artistdob	artistplace	artiststyle	artistmobnum	artistemail

CUSTOMER
Custusername(PK) custname	custaadhaarnum	custmobnum	custemail	custplace

ARTWORKS
Artid(PK) artprice	artistname	arttype	arttitle	artyear

ORDERS
artid(FK)	Ordnum(PK) custname(FK)	orddate	ordpayment






