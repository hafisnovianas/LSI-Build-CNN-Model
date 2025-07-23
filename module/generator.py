from tensorflow.keras.preprocessing.image import ImageDataGenerator

def data_generator(train_data_path, validation_data_path, IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE):
    train_datagen = ImageDataGenerator(
        rescale=1./255  # Normalisasi
        
        #====Jika butuh augmentasi, silahkan masukkan semua parameter berikut====#
        #rotation_range=20,  # Rotasi gambar acak
        #width_shift_range=0.2,  # Pergeseran horizontal
        #height_shift_range=0.2,  # Pergeseran vertikal
        #shear_range=0.2,  # Shear transform
        #zoom_range=0.2,  # Zoom in/out gambar
        #horizontal_flip=True,  # Membalik gambar secara horizontal
        #fill_mode='nearest',  # Pengisian ulang piksel yang hilang setelah transformasi
    )

    validation_datagen = ImageDataGenerator(
        rescale=1./255
    )

    train_generator = train_datagen.flow_from_directory(
        train_data_path,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    validation_generator = validation_datagen.flow_from_directory(
        validation_data_path,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    return train_generator, validation_generator