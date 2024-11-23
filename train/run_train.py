from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import generator

IMG_HEIGHT = 480
IMG_WIDTH = 640
BATCH_SIZE = 32
EPOCHS = 1
train_data_path = 'dataset/data_latih/'

train_generator, validation_generator = generator.data_generator(train_data_path, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE)

# Membuat model CNN dengan menggunakan Input
model = Sequential([
    Input(shape=(IMG_HEIGHT, IMG_WIDTH, 3)),  # Input yang dianjurkan di layer pertama
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')  # 3 kelas: oplosan, curah, kemasan
])

# Kompilasi model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Callback untuk menyimpan model terbaik dan Early Stopping
checkpoint = ModelCheckpoint('best_model/best_model_cnn_minyak_goreng.keras', 
                             monitor='val_accuracy', 
                             save_best_only=True, 
                             mode='max')

early_stopping = EarlyStopping(monitor='val_loss', 
                               patience=3,  # Menghentikan jika tidak ada perbaikan selama 3 epoch
                               restore_best_weights=True)

# Melatih model dengan callback checkpoint dan early stopping
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator,
    callbacks=[checkpoint, early_stopping]
)

# Menyimpan model akhir (jika ingin tetap menyimpan model terakhir meskipun bukan yang terbaik)
model.save('best_model/final_model_cnn_minyak_goreng.keras')