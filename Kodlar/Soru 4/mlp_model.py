#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EGE DOĞAN DURSUN - 05170000006
CEM ÇORBACIOĞLU - 05130000242
EGE ÜNİVERSİTESİ
MÜHENDİSLİK FAKÜLTESİ
BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
2019 - 2020 BAHAR DÖNEMİ
İŞLEMSEL ZEKA VE DERİN ÖĞRENME DERSİ
PROJE 1 - SORU 4 - MAKİNE ÖĞRENMESİ / SINIFLANDIRICI - NO:1
TARİH: 15 NİSAN 2020
"""

import tensorflow as tf
from tensorflow import keras

#Multilayer perceptron modelinin tanımı.
# FLATTEN -> DENSE -> DROPOUT -> DENSE -> DROPOUT -> DENSE -> DENSE
def get_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dropout(0.1),
        keras.layers.Dense(256, activation="relu"),
        keras.layers.Dropout(0.1),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dense(10),
        ])
    
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=["accuracy"])
    
    return model