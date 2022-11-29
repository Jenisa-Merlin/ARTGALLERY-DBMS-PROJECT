#importing required libraries

from flask import Flask, render_template, request,url_for,session,redirect
import MySQLdb
import MySQLdb.cursors

#flask
app = Flask(__name__)

#database connection
db = MySQLdb.connect("localhost","root","Jeni@3604","artgallery" )
cur = db.cursor()

app.secret_key = 'Jeni@3604'

#starting arrow to inside webpage 
@app.route('/')
def home():
	return render_template('index.html')

#directing to sign up page
@app.route('/front')
def front():
	return render_template('front.html')

#to logout and reach the signup page
@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('password',None)
    session.pop('username',None)
    return redirect(url_for('front'))

#to go back to the home page
@app.route('/Home')
def home_page():
	return render_template('nav-bar.html')

#to view the gallery of artworks
@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

#to display the customer details
@app.route('/customers',methods = ['POST','GET'])
def customers():
	cur.execute("SELECT * FROM CUSTOMER")
	customers_details= cur.fetchall()
	x = len(customers_details)
	return render_template('customers.html',c = customers_details,z = x)

#to enter new customer go to newcustomer.html
@app.route('/gonewcust')
def gonewcust():
	return render_template('newcustomer.html')

#to enter a new customer
@app.route('/newcustomer',methods = ['POST', 'GET'])
def newcustomer():
	try:
		cname = (request.form['cust_name'])
		cid = (request.form['cust_username'])
		cpwd = (request.form['cust_pwd'])
		caadhaar = (request.form['aadhaar_num'])
		cmail = (request.form['cust_email'])
		cmob = (request.form['cust_mobNum'])
		cplace = (request.form['cust_place'])
		sql = """INSERT INTO CUSTOMER (cust_name,cust_username,cust_password,cust_aadhar_num,cust_email,cust_mobNum,cust_place) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
		val = (cname,cid,cpwd,caadhaar,cmail,cmob,cplace,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('newcustomer.html',msg = "Already Exists")
	return render_template('newcustomer.html',msg = "Successfully Registered")

#to delete a customer go to delete.html
@app.route('/godel')
def delecustomer():
	return render_template('del.html')

#to delete a customer
@app.route('/del',methods = ['POST', 'GET'])
def delcustomer():
	try:
		DID = (request.form['CID'])
		sql = "DELETE FROM CUSTOMER WHERE cust_username = %s"
		val = (DID,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('del.html',msg = "Cannot delete")
	return render_template('del.html',msg = "Successfully Deleted")

#to display the artist details
@app.route('/artist',methods = ['POST','GET'])
def artist():
	cur.execute("SELECT * FROM ARTIST")
	artist_details= cur.fetchall()
	x = len(artist_details)
	return render_template('artist.html',c = artist_details,z = x)

#to enter new artist go to newartist.html
@app.route('/gonewartist')
def gonewartist():
	return render_template('newartist.html')

#to enter a new artist
@app.route('/newartist',methods = ['POST', 'GET'])
def newartist():
	try:
		aname = (request.form['artist_name'])
		aid = (request.form['artist_username'])
		apwd = (request.form['artist_pwd'])
		adob = (request.form['artist_dob'])
		astyle = (request.form['artist_style'])
		aaadhaar = (request.form['aadhaar_num'])
		amail = (request.form['artist_email'])
		amob = (request.form['artist_mobNum'])
		aplace = (request.form['artist_place'])
		sql = """INSERT INTO ARTIST (artist_name,artist_username,artist_password,artist_dob,artist_style,aadhar_num,artist_email,artist_mobNum,artist_place) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		val = (aname,aid,apwd,adob,astyle,aaadhaar,amail,amob,aplace,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('newartist.html',msg = "Already Exists")
	return render_template('newartist.html',msg = "Successfully Registered")

#to delete an artist go to delartist.html
@app.route('/godelartist')
def deleartist():
	return render_template('delartist.html')

#to delete an artist
@app.route('/delartist',methods = ['POST', 'GET'])
def delartist():
	try:
		DID = (request.form['AID'])
		sql = "DELETE FROM ARTIST WHERE artist_username = %s"
		val = (DID,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('delartist.html',msg = "Cannot delete")
	return render_template('delartist.html',msg = "Successfully Deleted")

#to display the artworks details
@app.route('/artworks',methods=['POST','GET'])
def artworks():
	cur.execute("SELECT * FROM ART")
	artworks_details= cur.fetchall()
	x = len(artworks_details)
	return render_template('artworks.html',c = artworks_details,z = x)

#to enter new artworks go to newartworks.html
@app.route('/gonewartworks')
def gonewartwork():
	return render_template('newartworks.html')

#to enter a new artwork
@app.route('/newartworks',methods = ['POST', 'GET'])
def newartwork():
	try:
		aid = (request.form['art_id'])
		atitle = (request.form['art_title'])
		aprice = (request.form['art_price'])
		atype = (request.form['art_type'])
		ayear = (request.form['art_year'])
		sql = """INSERT INTO ART (art_id,art_title,art_price,art_type,art_year) VALUES(%s,%s,%s,%s,%s)"""
		val = (aid,atitle,aprice,atype,ayear,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('newartworks.html',msg = "Already Exists")
	return render_template('newartworks.html',msg = "Successfully Registered")

#to delete an artwork go to delartwork.html
@app.route('/godelartworks')
def deleartwork():
	return render_template('delartworks.html')

#to delete an artwork
@app.route('/delartworks',methods = ['POST', 'GET'])
def delartwork():
	try:
		ARTID = (request.form['AID'])
		sql = "DELETE FROM ART WHERE art_id = %s"
		val = (ARTID,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('delartworks.html',msg = "Cannot delete")
	return render_template('delartworks.html',msg = "Successfully Deleted")

#to display the orders details
@app.route('/orders',methods=['POST','GET'])
def orders():
	cur.execute("SELECT * FROM ORDERS")
	orders_details= cur.fetchall()
	x = len(orders_details)
	return render_template('orders.html',c = orders_details,z = x)

#to enter new orders go to neworders.html
@app.route('/goneworders')
def goneworder():
	return render_template('neworders.html')

#to enter a new orders
@app.route('/neworders',methods = ['POST', 'GET'])
def neworder():
	try:
		cname = (request.form['cust_name'])
		aid = (request.form['art_id'])
		onum = (request.form['order_num'])
		odate = (request.form['order_date'])
		opay = (request.form['order_pay'])
		sql = """INSERT INTO ORDERS (cust_name,art_id,ord_num,ord_date,ord_payment) VALUES(%s,%s,%s,%s,%s)"""
		val = (cname,aid,onum,odate,opay,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('neworders.html',msg = "Already Exists")
	return render_template('neworders.html',msg = "Successfully Registered")

#to delete an order go to delorder.html
@app.route('/godelorders')
def deleorder():
	return render_template('delorders.html')

#to delete an order
@app.route('/delorders',methods = ['POST', 'GET'])
def delorder():
	try:
		OID = (request.form['OID'])
		sql = "DELETE FROM ORDERS WHERE ord_num = %s"
		val = (OID,)
		cur.execute(sql,val)
		db.commit()
	except:
		return render_template('delorders.html',msg = "Cannot delete")
	return render_template('delorders.html',msg = "Successfully Deleted")

#if admin it directs to admin signup page and there if username and password is correct it moves to nav-bar page
@app.route('/adminlogin/', methods = ['GET','POST'])
def adminlogin():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		if username == 'Jenisa' and password == 'djm':
			session['loggedin'] = True
			msg = 'Logged in successfully'
			return render_template('nav-bar.html',msg = msg)
		else:
			msg = 'Incorrect username/password'
	return render_template('adminlogin.html',msg = msg)

#to customer login
@app.route('/clogin')
def cust_login():
	return render_template('customerlogin.html')

#customer login for getting AID and confirm the order
@app.route('/customerlogin',methods = ['POST', 'GET'])
def cust():
	try:
		AID = (request.form['AID'])
	except:
		return render_template('customerlogin.html',msg = "Order Can't be Placed")
	return render_template('customerlogin.html',msg = "Successfully Order placed")

#to display the orders combining orders and art
@app.route('/orderdisplay',methods=['POST','GET'])
def ord_disp():
	cur.execute("SELECT O.cust_name,O.art_id,O.ord_num,O.ord_date,O.ord_payment,A.art_price FROM ORDERS O INNER JOIN ART A WHERE O.art_id = A.art_id")
	ord_details= cur.fetchall()
	x = len(ord_details)
	return render_template('orderdisplay.html',c = ord_details,z = x)

#main begins
if __name__ == "__main__":
    app.run(debug = True, port = 8080)