import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import datetime
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import os
from keras.models import model_from_json
from keras import backend as K 

import cv2
import pandas as pd

import os
 
 
 

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="skinsdb")
    c = _conn.cursor()

    return c, _conn

# -------------------------------register-----------------------------------------------------------------
def user_reg(id,username, password, email, mobile, address,):
    try:
        c, conn = db_connect()
        print(id,username, password, email,
               mobile, address)
        j = c.execute("insert into register (id,username,password,email,mobile,address) values ('"+id+"','"+username +
                      "','"+password+"','"+email+"','"+mobile+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
    
def doc_reg(id,username, password, email, location, specialist,exp):
    try:
        c, conn = db_connect()
        print(id,username, password, email, location, specialist,exp)
        j = c.execute("insert into doctor (id,username,password,email,location, specialist,exp) values ('"+id+"','"+username +
                      "','"+password+"','"+email+"','"+location+"','"+specialist+"','"+exp+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def book_act(id,doctor, patient, disease):
    try:
        c, conn = db_connect()
        print(id,doctor, patient, disease)
        status = "pending"
        j = c.execute("insert into book (id,doctor, patient, disease,status) values ('"+id+"','"+doctor +
                      "','"+patient+"','"+disease+"','"+status+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
# -------------------------------------Login --------------------------------------
def user_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from register where username='" +
                      username+"' and password='"+password+"'")
        data = c.fetchall()
        print(data)
        for a in data:
           session['username'] = a[1]
           session['address'] = a[5]
       
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
    
def doc_act(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from doctor where username='" +
                      username+"' and password='"+password+"'")
        data = c.fetchall()
        print(data)
        for a in data:
           session['username'] = a[1]
       
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
#-------------------------------------Upload Image------------------------------------------
def user_upload(id,name, image):
    try:
        c, conn = db_connect()
        print(name,image)
        username = session['username']
        j = c.execute("insert into upload (id,name,image,username) values ('"+id+"','"+name+"','"+image +"','"+username +"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))



def accept_req(doctor,patient):
    try:
        c, conn = db_connect()
        j = c.execute("update book set status='accepted' where doctor='"+doctor+"' and patient='"+patient+"' ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

#---------------------------------------View Images---------------------------------------
def user_viewimages(username):
    c, conn = db_connect()
    c.execute("select * from upload where  username='"+username +"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result



def view_d(address):
    c, conn = db_connect()
    c.execute("select * from doctor where  location='"+address +"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def view_status(username):
    c, conn = db_connect()
    c.execute("select * from book where  patient='"+username +"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def view_r(username):
    c, conn = db_connect()
    c.execute("select * from book where  doctor='"+username +"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
#------------------------------------Track----------------------------------------------------
def v_image(name):
    c, conn = db_connect()
    c.execute("Select * From images where name='"+name+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
# ----------------------------------------------Update Items------------------------------------------

def image_info(path):
    SKIN_CLASSES = {
    0: 'Actinic Keratoses (Solar Keratoses) or intraepithelial Carcinoma (Bowens disease)',
    1: 'Basal Cell Carcinoma',
    2: 'Benign Keratosis',
    3: 'Dermatofibroma',
    4: 'Melanoma',
    5: 'Melanocytic Nevi',
    6: 'Vascular skin lesion'

    }    
    j_file = open('modelnew.json', 'r')
    loaded_json_model = j_file.read()
    j_file.close()
    model = model_from_json(loaded_json_model)
    model.load_weights('modelnew.h5')
    img1 = image.load_img(path, target_size=(224,224))
    img1 = np.array(img1)
    img1 = img1.reshape((1,224,224,3))
    img1 = img1/255
    prediction = model.predict(img1)
    pred = np.argmax(prediction)
    disease = SKIN_CLASSES[pred]
    accuracy = prediction[0][pred]
    K.clear_session()

    
      
    
    return disease

if __name__ == "__main__":
    print(db_connect())
