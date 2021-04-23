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
PROJE 1 - SORU 4 - MAKİNE ÖĞRENMESİ / SINIFLANDIRICI - NO:2
YÖNTEM : RANDOM FOREST
TARİH: 15 NİSAN 2020
"""


#Gerekli kütüphaneler import edilir
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import StratifiedKFold
from tensorflow import keras
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import random as r
import tensorflow as tf


#Çapraz doğrulama fold sayısı belirlenir
n_splits = 10


#Veri seti yüklenir, gerekli eğitim ve test verilerine ayrıştırılır.
fashion_mnist  = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


#Veride mevcut olan sınıf isimlerini ifade eden bir liste tanımlanır.
class_names = ["T-shirt",
               "Trouser",
               "Pullover",
               "Dress",
               "Coat",
               "Sandal",
               "Shirt",
               "Sneaker",
               "Bag",
               "Ankle Boot"]


#Eğitim ve test verilerinin ve labellarının shape'leri kontrol edilir.
print("TRAIN DATA SHAPE : ", train_images.shape)
print("TRAIN LABELS LENGTH : ", len(train_labels))

print("TEST DATA SHAPE : ", test_images.shape)
print("TEST LABELS LENGTH : ", len(test_labels))


#Örnek birkaç veri görüntülenir
print("\n\n EXAMPLE DATA SAMPLES: \n")
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure()
plt.imshow(train_images[10])
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure()
plt.imshow(train_images[105])
plt.colorbar()
plt.grid(False)
plt.show()


#Daha verimli bir eğitim için eğitim ve test verilerine normalizasyon uygulanır.
#Resimlerimiz siyah beyaz olduğu için ve siyah beyaz değerler 0 ve 255 arasında tanımlandığı için 255.0'e böldük.
train_images = train_images / 255.0
test_images = test_images / 255.0


#Çeşitli sınıflara ait verilere örnekler
print("\n EXAMPLES FROM VARIOUS CLASSES : \n")
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


#Eğitim ve test verisini düzleştir.
train_pixels = []
test_pixels = []
for i in range(0, len(train_images)):
    train_pixels.append(train_images[i].flatten().reshape(28*28))
for i in range(0, len(test_images)):
    test_pixels.append(test_images[i].flatten().reshape(28*28))


#Random Forest modelini eğit.
rf_model = RandomForestClassifier().fit(train_pixels, train_labels)


#Eğitim verileri için tahminlemeler üret
predictions = rf_model.predict(train_pixels)


#Eğitim verileri için confusion matrix oluştur
con_matrix = confusion_matrix(predictions, train_labels)


#Eğitim verileri için oluşturulan confusion matrixi görüntüle
print("\n EĞİTİM VERİLERİ HATA MATRİSİ : \n")
figure = plt.figure(figsize=(8, 8))
sns.heatmap(con_matrix, annot=True,cmap=plt.cm.Blues, fmt='g')
plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()


#Eğitim verileri için accuracy oranını görüntüle
rf_train_accuracy = (predictions == train_labels).mean()
print("\n\n TRANINING ACCURACY :", rf_train_accuracy, "\n\n")


#Test verileri için tahminlemeler üret
predictions = rf_model.predict(test_pixels)


#Test verileri için confusion matrix oluştur
con_matrix = confusion_matrix(predictions, test_labels)


#Test verileri için oluşturulan confusion matrixi görüntüle
print("\n TEST VERİLERİ HATA MATRİSİ : \n")
figure = plt.figure(figsize=(8, 8))
sns.heatmap(con_matrix, annot=True,cmap=plt.cm.Blues, fmt='g')
plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()


#Test verileri için accuracy oranını görüntüle
rf_test_accuracy = (predictions == test_labels).mean()
print("\n\n TEST ACCURACY : ", rf_test_accuracy , "\n\n")



#Verilen bir veriye göre tahminlemede bulun
idx = r.randint(0, len(test_images)-1)
data_image = test_images[idx]
data_pixels = data_image.flatten().reshape(28*28)
data_answer = test_labels[idx]
data_pixels = np.array([data_pixels])
result = rf_model.predict(data_pixels)


print("THE IMAGE THAT WILL GET IT'S LABEL PREDICTED: ")
plt.figure()
plt.imshow(data_image)
plt.colorbar()
plt.grid(False)
plt.show()

print("THE PREDICTION IS: ", class_names[result[0]])
print("THE REAL CLASS IS: ", class_names[data_answer])



#k-Fold Çapraz doğrulama uygulamadan önce veri setlerini birleştir
inputs = np.concatenate((train_images, test_images))
input_pixels = np.concatenate((train_pixels, test_pixels))
targets = np.concatenate((train_labels, test_labels))


#10 katlı çapraz doğrulama uygula
cvscores = []
y_preds = []
y_trues = []
kfold = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=0)
for train, test in kfold.split(inputs, targets):
    
    print("\n\n TRAINING NEW FOLD... \n\n")
    
    rf_model = RandomForestClassifier().fit(input_pixels[train], targets[train])
    
    train_predictions = rf_model.predict(input_pixels[test])
    test_predictions = rf_model.predict(input_pixels[test])
    
    #her katta model performansını ölçümle
    rf_train_accuracy = (train_predictions == targets[test]).mean()
    print("\n TRANINING ACCURACY :", rf_train_accuracy, "\n")
    rf_test_accuracy = (test_predictions == targets[test]).mean()
    print("\n TEST ACCURACY : ", rf_test_accuracy , "\n")
    
    cvscores.append(rf_test_accuracy*100)
    
    y_pred = []
    for i in range(0, len(test_predictions)):
        y_pred.append(test_predictions[i])
        
    y_preds = np.concatenate((y_preds, y_pred), axis=None)
    y_trues = np.concatenate((y_trues, targets[test]), axis=None)


print("AVERAGE ACCURACY : ", np.mean(cvscores))
print("STANDARD DEVIATION (+/-) : ", np.std(cvscores))


#Her tur için ulaşılan final accuracy skorlarını göster (test verileri için)
for i in range(0, n_splits):
    print("FOLD NO:",(i+1),"  Accuracy : ", cvscores[i])
    
    
len(y_trues)
len(y_preds)
#Tüm toplam tahminlemeler için hata matrisini görüntüle
con_mat = tf.math.confusion_matrix(
        labels = y_trues,
        predictions = y_preds,
        ).numpy()


#Hata matrisini ekrana bastır
print("\n HATA MATRİSİ : \n")
figure = plt.figure(figsize=(8, 8))
sns.heatmap(con_mat, annot=True,cmap=plt.cm.Blues, fmt='g')
plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
    
    
    
    
    

