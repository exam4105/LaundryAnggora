from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime
import requests
from bson import ObjectId

app = Flask(__name__)

myclient = MongoClient("mongodb+srv://soys:123@cluster0.iwvcwt0.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["laundry"]
mycol = mydb["pesanan"]


@app.route('/', methods=['GET'])
def home():
    data = mycol.find_one({"_id": ObjectId("60f8d1f5e3a27f0001c9f5e6")})
    return render_template('index.html', data=data)


@app.route('/kiloan', methods=['GET'])
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


@app.route('/order_senin')
def order_senin():
    return render_template('order_senin.html')

@app.route('/order_selasa')
def order_selasa():
    return render_template('order_selasa.html')

@app.route('/order_rabu')
def order_rabu():
    return render_template('order_rabu.html')

@app.route('/order_kamis')
def order_kamis():
    return render_template('order_kamis.html')

@app.route('/order_sabtu')
def order_sabtu():
    return render_template('order_sabtu.html')

@app.route('/order_jumat')
def order_jumat():
    return render_template('order_jumat.html')

@app.route('/order_minggu')
def order_minggu():
    return render_template('order_minggu.html')

@app.route('/service_detail')
def service_detail():
    return render_template('service_detail.html')

@app.route('/completed_order')
def completed_order():
    return render_template('completed_order.html')

@app.route('/', methods=['POST'])
def tambah():
    data = mycol.find_one({"_id": ObjectId("60f8d1f5e3a27f0001c9f5e6")})
    nama=request.form.get('nama')
    jenis_laundry=request.form.get('jenis_laundry')
    whatsapp=request.form.get('whatsapp')
    waktu_jemput=request.form.get('waktu_jemput')
    alamat=request.form.get('alamat')
    pesan=request.form.get('pesan')

    my_dict = {'nama': nama,
               'jenis laundry': jenis_laundry,
               'whatsapp': whatsapp,
               'waktu jemput': waktu_jemput,
               'alamat': alamat,
               'pesan': pesan}

    print(my_dict)
    mycol.insert_one(my_dict)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)