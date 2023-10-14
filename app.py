from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime
import requests
from bson import ObjectId

app = Flask(__name__)

myclient = MongoClient("mongodb+srv://soys:123@cluster0.iwvcwt0.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient.laundry
mycol = mydb.pesanan


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


@app.route('/order_list')
def list_order():
    data = mydb.pesanan.find({})
    
    return render_template('order_list.html',data=data)

@app.route('/delete', methods=['GET'])
def delete():
    id=request.args.get('_id')
    mycol.delete_one({'_id':ObjectId(id)})
    data=list(mydb.pesanan.find({}))
    return render_template('order_list.html',data=data)

@app.route('/service_detail')
def service_detail():
    return render_template('service_detail.html')

@app.route('/', methods=['POST'])
def tambah():
    nama=request.form.get('nama')
    jenis_laundry=request.form.get('jenis_laundry')
    whatsapp=request.form.get('whatsapp')
    waktu_jemput=request.form.get('waktu_jemput')
    alamat=request.form.get('alamat')
    pesan=request.form.get('pesan')

    my_dict = {'nama': nama,
               'jenis_laundry': jenis_laundry,
               'whatsapp': whatsapp,
               'waktu_jemput': waktu_jemput,
               'alamat': alamat,
               'pesan': pesan}

    print(my_dict)
    mycol.insert_one(my_dict)

    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)