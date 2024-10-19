import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os
import utility

# Ukuran gambar sesuai dengan yang digunakan dalam pelatihan
IMG_HEIGHT = 480
IMG_WIDTH = 640

# Memuat model yang sudah dilatih
model = load_model('best_model/best_model_cnn_minyak_goreng_BAGUS.keras')

# Fungsi prediksi untuk gambar baru
def predict_image(image_path):
    # Memuat gambar dan mengubahnya ke ukuran yang sesuai
    img = image.load_img(image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = image.img_to_array(img)
    
    # Menambahkan dimensi batch dan normalisasi gambar
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    # Melakukan prediksi
    prediction = model.predict(img_array)
    
    # Mendefinisikan nama kelas sesuai dengan label pelatihan
    class_names = ['Curah', 'Kemasan', 'Oplosan']
    
    # Mengambil kelas dengan probabilitas tertinggi
    predicted_class = class_names[np.argmax(prediction)]
    
    return predicted_class

dataName = 'OPLOSAN'
ujiFolderPath = os.path.join('dataset/data_uji',dataName)

predictedList = []
for fileName in os.listdir(ujiFolderPath):
    filePath = os.path.join(ujiFolderPath,fileName)
    predicted_class = predict_image(filePath)
    predictedList.append([fileName, predicted_class])

utility.saveToExcel(predictedList, dataName+' (prediksi)', ujiFolderPath)
utility.cetak(predictedList)
