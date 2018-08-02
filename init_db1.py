from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)
DATABASE = 'myapp.db'

def init_db():
   db = sqlite3.connect(DATABASE)
   with app.open_resource('db1.sql', mode='r') as f:
   	   sql = f.read()
   print(sql)
   db.cursor()
   db.execute(sql)
   db.commit()
   db.close()
   
if __name__=='__main__':
   init_db()