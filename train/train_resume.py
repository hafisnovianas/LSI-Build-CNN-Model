from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import train.generator as generator

# Parameter gambar dan pelatihan
IMG_HEIGHT = 480
IMG_WIDTH = 640
BATCH_SIZE = 32
EPOCHS = 20
train_data_path = 'dataset/data_latih/'

train_generator, validation_generator = generator.data_generator(train_data_path, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE)

# Memuat model dari checkpoint
model = load_model('best_model/best_model_cnn_minyak_goreng_BAGUS.keras')

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
