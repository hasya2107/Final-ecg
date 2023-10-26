from flask import Flask, jsonify
import wfdb 
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/ecg-data', methods=["POST"], strict_slashes=False)
@cross_origin(supports_credentials=True)
def ecg_data():
    record = wfdb.rdrecord('mitdb/JS00008',sampto=5000)
    fs=record.fs
    print(fs)
    ecg_data1 =record.p_signal[:,0]
    ecg_data2 = record.p_signal[:,1]
    ecg_data3= record.p_signal[:,2]
    ecg_data4= record.p_signal[:,3]
    ecg_data5= record.p_signal[:,4]
    ecg_data6= record.p_signal[:,5]
    ecg_data7= record.p_signal[:,6]
    ecg_data8= record.p_signal[:,7]
    ecg_data9= record.p_signal[:,8]
    ecg_data10= record.p_signal[:,9]
    ecg_data11=record.p_signal[:,10]
    ecg_data12=record.p_signal[:,11]

    
    # return jsonify({'data1':ecg_data1.tolist(),'data2':ecg_data2.tolist(),'data3':ecg_data3.tolist()})
    return jsonify({'data1':ecg_data1.tolist(),'data2':ecg_data2.tolist(),'data3':ecg_data3.tolist(),'data4':ecg_data4.tolist(),'data5':ecg_data5.tolist(),
                    'data6':ecg_data6.tolist(),'data7':ecg_data7.tolist(),'data8':ecg_data8.tolist(),'data9':ecg_data9.tolist(),
                    'data10':ecg_data10.tolist(),'data11':ecg_data11.tolist(),'data12':ecg_data12.tolist()})

if __name__ == '__main__':
    app.run(debug=True)


