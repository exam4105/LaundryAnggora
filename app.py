from flask import Flask, render_template, jsonify, request, session, redirect, url_for, request
from functools import wraps
from pymongo import MongoClient
from datetime import datetime
import time
import hashlib
import requests
from bson import ObjectId

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

myclient = MongoClient("mongodb+srv://soys:123@cluster0.iwvcwt0.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient.laundry
mycol = mydb.pesanan
newcol = mydb.admin

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/kiloan')
def kiloan():
    return render_template('kiloan.html')

@app.route('/sepatu')
def sepatu():
    return render_template('sepatu.html')

@app.route('/springbed')
def springbed():
    return render_template('springbed.html')

@app.route('/karpet')
def karpet():
    return render_template('karpet.html')

@app.route('/tas')
def tas():
    return render_template('tas.html')

@app.route('/stroller')
def stroller():
    return render_template('stroller.html')
#END OF CUSTOMER PAGE

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.before_request
def before_request():
    if 'logged_in' in session and 'last_activity' in session:
        if time.time() - session['last_activity'] > 5:
            session.pop('logged_in', None)
            return redirect(url_for('login'))
        else:
            session['last_activity'] = time.time()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve the username and password from the database
        user = newcol.find_one({'username': request.form['username']})

        if user and user['password'] == request.form['password']:
            session['logged_in'] = True
            session['last_activity'] = time.time()
            return redirect(url_for('order_list'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('last_activity', None)
    return redirect(url_for('login'))

@app.route('/order_list')
@login_required
def order_list():
    data = mydb.pesanan.find({})
    
    return render_template('order_list.html',data=data)

@app.route('/delete', methods=['GET'])
def delete():
    id=request.args.get('_id')
    mycol.delete_one({'_id':ObjectId(id)})
    data=list(mydb.pesanan.find({}))
    return render_template('order_list.html',data=data)

@app.route('/service_detail')
@login_required
def service_detail():
    return render_template('service_detail.html')

@app.route('/', methods=['POST','GET'])
def tambah():
    if request.method== 'POST':
       my_dict = ({'nama':request.form['name'], 'jenis_laundry':request.form['laundry'], 'whatsapp':request.form['Whatsapp'], 'waktu_jemput':request.form['pickup'], 'alamat':request.form['address'], 'pesan':request.form['massage']})
       mycol.insert_one(my_dict)

    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)