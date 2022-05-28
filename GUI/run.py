from flask import Flask, render_template, request, url_for, redirect
from tensorflow import keras
import numpy as np


# import copy


# import matplotlib.pyplot as plt
import h5py
import scipy
# from PIL import Image
# from scipy import ndimage

from tensorflow import keras
import tensorflow as tf



app = Flask(__name__)

@app.route("/" , methods= ['GET','POST'])
def cap():
    # return "<p>Hello, World!</p>"
    str3 = ''
    str1 = ''
    str2 = ''
    i = 0
    l = ['ins_cap.h5' , 'nfle_cap.h5', 'narco_cap.h5', 'rbd_cap.h5', 'plm_cap.h5']
    if request.method =='POST':
        x_bal = request.files['myfile']
        x_bal = np.loadtxt(x_bal,  delimiter=',')
        print(np.shape(x_bal))
        x_bal = x_bal.reshape((1,1024))
        print(np.shape(x_bal))

        model3 = keras.models.load_model("healthy_cap.h5")
        pred3 = model3.predict(x_bal)
        if pred3[0][0] < 0.5:
            str3 = 'CAP phase detected : B '
        else:
            str3 = 'CAP phase detected : A '
        model1 = keras.models.load_model("model_v4.h5")
        pred1 = model1.predict(x_bal)
        print(str1)
        
        if pred1[0][0] > 0.5:
            str1 = 'Health Report : Positve'
            model2 = keras.models.load_model("model_skip_D70.h5")
            pred2 = model2.predict(x_bal)
            print(type(pred2))
            disease = ['INS', 'NFLE','NARCO','RBD','PLM']
            print(pred2)
            i = (pred2.argmax())
            print(i)
            str2 = disease[i]
            print(str1)
            s = l[i]
            print(s)
            model3 = keras.models.load_model(s)
            pred3 = model3.predict(x_bal)
            if pred3[0][0] < 0.5:
                str3 = 'CAP phase detected : B '
            else:
                str3 = 'CAP phase detected : A '
            model1 = keras.models.load_model("model_v4.h5")
            pred1 = model1.predict(x_bal)
        else:
            str1 = 'Health Report : Negative'
            model3 = keras.models.load_model("healthy_cap.h5")
            pred3 = model3.predict(x_bal)
            if pred3[0][0] < 0.5:
                str3 = 'CAP phase detected : B '
            else:
                str3 = 'CAP phase detected : A '
            model1 = keras.models.load_model("model_v4.h5")
            pred1 = model1.predict(x_bal)
        return render_template('form.html' , str1 = str1, str2 = str2, str3 = str3)
    return render_template('form.html' , str1 = str1 , str2 = str2, str3 = str3)

if __name__ == '__main__':
    app.run(debug=True, port=3232)