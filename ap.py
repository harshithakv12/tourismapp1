from flask import Flask, render_template, request,redirect,url_for
import sqlite3

app=Flask(__name__)

DATABASE = 'myapp.db'

def connect_db():
   return sqlite3.connect(DATABASE)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/places')
def places():
   return render_template('places.html')

@app.route('/packages')
def packages():
   return render_template('packages.html')

@app.route('/pack')
def pack():
   return render_template('pack.html')

@app.route('/pack2')
def pack2():
   return render_template('pack2.html')

@app.route('/pack3')
def pack3():
   return render_template('pack3.html')

@app.route('/pack4')
def pack4():
   return render_template('pack4.html')

@app.route('/karnataka')
def karnataka():
   return render_template('karnataka.html')

@app.route('/kerala')
def kerala():
   return render_template('kerala.html')

@app.route('/andhrapradhesh')
def andhrapradhesh():
   return render_template('andhrapradhesh.html')

@app.route('/Tamilnadu')
def Tamilnadu():
   return render_template('Tamilnadu.html')

@app.route('/login',methods=['GET','POST'])
def login():
   error = None
   if request.method == 'POST':
      if request.form['username'] != 'username' or request.form['password'] != 'username':
         error = 'Invalid credentials. Please try again.'
      else:
         return redirect(url_for)
   return render_template('login.html',error=error)

@app.route('/booking')
def booking():
   return render_template('booking.html')

@app.route('/myProfile',methods=['POST','GET'])
def showmyprofile():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      email = request.form['email']
      db = connect_db()
      sql = "insert into login112 (username,password,email) values (?,?,?)"
      db.execute(sql, [username,password,email])
      db.commit()
      db.close()
      return render_template('myProfile.html',html_page_name=username)   

@app.route('/bookinglist')
def bookinglist():
   db = connect_db()
   cur = db.execute("select username,password,email from login112")
   entries = [dict(username=row[0],password=row[1],email=row[2]) for row in cur.fetchall()]
   print(entries)
   db.close()
   return render_template('users.html',entries=entries)  

@app.route('/booking2')
def booking1():
   return render_template('booking2.html')

@app.route('/myProfile2',methods=['GET','POST'])
def showmyprofile1():
   if request.method == 'POST':
      username = request.form['username']
      email = request.form['email']
      phonenumber = request.form['phonenumber']
      password = request.form['password']
      confirmpassword = request.form['confirmpassword']
      db = connect_db()
      sql = "insert into cpass (username,email,phonenumber,password,confirmpassword) values (?,?,?,?,?)"
      db.execute(sql, [username,email,phonenumber,password,confirmpassword])
      db.commit()
      db.close()
      return render_template('myprofile2.html',html_page_name=username)   

@app.route('/cpasslist1')
def bookinglist1():
   db = connect_db()
   cur = db.execute("select username,email,phonenumber,password,confirmpassword from cpass")
   entries1 = [dict(username=row[0],email=row[1],phonenumber=row[2],password=row[3], confirmpassword=row[4]) for row in cur.fetchall()]
   print(entries1)
   db.close()
   return render_template('user1.html',entries1=entries1)  

@app.route('/booking3')
def booking3():
   return render_template('booking3.html')

@app.route('/myProfile3',methods=['GET','POST'])
def showmyprofile3():
   if request.method == 'POST':
      username = request.form['username']
      email = request.form['email']
      password = request.form['password']
      reenterpassword = request.form['reenterpassword']
      db = connect_db()
      sql = "insert into pass (username,email,password,reenterpassword) values (?,?,?,?)"
      db.execute(sql, [username,email,password,reenterpassword])
      db.commit()
      db.close()
      return render_template('myprofile3.html',html_page_name=username)   

@app.route('/cpasslist3')
def bookinglist3():
   db = connect_db()
   cur = db.execute("select username,email,password,reenterpassword from pass")
   entries2 = [dict(username=row[0],email=row[1],password=row[2],reenterpassword=row[3]) for row in cur.fetchall()]
   print(entries2)
   db.close()
   return render_template('user2.html',entries2=entries2)  

if __name__=='__main__':
    app.run(debug=True)
