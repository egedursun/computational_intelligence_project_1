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
YÖNTEM : MULTILAYER PERCEPTRON
TARİH: 15 NİSAN 2020
"""


#Gerekli kütüphaneler import edilir
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import StratifiedKFold
import mlp_model
import random as r


#batch boyutu, çapraz doğrulama ayrım sayısı ve eğitim nesli sayısı tanımlanır
batch_size = 64
epochs = 10
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


#Modeli tanımlandığı sınıftan edin
model = mlp_model.get_model()


#Model özetini görüntüle
print(model.summary())


#Model eğitimini başlat. (10-Fold Cross Validation aşağıda yapılacak.)
history = model.fit(
        train_images, 
        train_labels, 
        batch_size=batch_size,
        epochs=epochs,
        validation_data=(test_images, test_labels))

#Modeli değerlendir.
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

#Modelin test seti üzerindeki başarısını görüntüle
print('\n\n TEST ACCURACY: %', test_acc*100)


#Modele dayalı tahminlemelerde bulun
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
    
    
predictions = probability_model.predict(test_images)


y_pred = []
for i in range(0, len(predictions)):
    y_pred.append(np.argmax(predictions[i]))
    

#Modele yönelik gerçekleştirilen tahminlerden çıkarılan hata matrisini görüntüle
con_mat = tf.math.confusion_matrix(
        labels = test_labels,
        predictions = y_pred,
        ).numpy()



#Hata matrisini ekrana bastır
print("\n HATA MATRİSİ : \n")
figure = plt.figure(figsize=(8, 8))
sns.heatmap(con_mat, annot=True,cmap=plt.cm.Blues, fmt='g')
plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()


#Eğitim ve test setine bağlı nesile göre değişen accuracy değerleri tarihini ekrana bastır.
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Accuracy History (Training and Validation)')
plt.ylabel('Accuracy Value (%)')
plt.xlabel('Number of Epoch')
plt.show()


#Verilen bir veriye göre tahminlemede bulun
idx = r.randint(0, len(test_images)-1)
data_image = test_images[idx]
data_answer = test_labels[idx]
data_image = np.array([data_image])
result = model.predict(data_image)
result = np.argmax(result)


print("THE IMAGE THAT WILL GET IT'S LABEL PREDICTED: ")
plt.figure()
plt.imshow(data_image[0])
plt.colorbar()
plt.grid(False)
plt.show()

print("THE PREDICTION IS: ", class_names[result])
print("THE REAL CLASS IS: ", class_names[data_answer])





#k-Fold Çapraz doğrulama uygulamadan önce veri setlerini birleştir
inputs = np.concatenate((train_images, test_images))
targets = np.concatenate((train_labels, test_labels))


#10 katlı çapraz doğrulama uygula
cvscores = []
histories = []
y_preds = []
y_trues = []
kfold = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=0)
for train, test in kfold.split(inputs, targets):
  
    print("\n\n TRAINING NEW FOLD... \n\n")
    
    model = mlp_model.get_model()
    
    history = model.fit(inputs[train], 
                        targets[train],
                        batch_size=batch_size,
                        epochs=epochs,
                        validation_data=(inputs[test], targets[test]))
    
    #her katta model performansını ölçümle
    scores = model.evaluate(inputs[test], targets[test], verbose=0)
    print("\n\n TEST ACCURACY : %", scores[1]*100)
    
    cvscores.append(scores[1]*100)
    histories.append(history)
    
    #modele bağlı tahminlemelerde bulun
    probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
    
    
    predictions = probability_model.predict(inputs[test])

    y_pred = []
    for i in range(0, len(predictions)):
        y_pred.append(np.argmax(predictions[i]))
        
    y_preds = np.concatenate((y_preds, y_pred), axis=None)
    y_trues = np.concatenate((y_trues, targets[test]), axis=None)
    


print("AVERAGE ACCURACY : ", np.mean(cvscores))
print("STANDARD DEVIATION (+/-) : ", np.std(cvscores))


#Her kat için accuracy değerinin zamana bağlı değişimini göster (eğitim verisi için)
for i in range(0, len(histories)):
    plt.plot(histories[i].history['accuracy'])
plt.title('Training Accuracy History')
plt.ylabel('Accuracy Value (%)')
plt.xlabel('Number of Epoch')
plt.show()

#Her kat için accuracy değerinin zamana bağlı değişimini göster (test verisi için)
for i in range(0, len(histories)):
    plt.plot(histories[i].history['val_accuracy'])
plt.title('Validation Accuracy History')
plt.ylabel('Accuracy Value (%)')
plt.xlabel('Number of Epoch')
plt.show()


#Her tur için ulaşılan final accuracy skorlarını göster (test verileri için)
for i in range(0, n_splits):
    print("FOLD NO:",(i+1),"  Accuracy : ", cvscores[i])


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


