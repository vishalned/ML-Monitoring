import keras
import tensorflow as tf
import matplotlib
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import  MaxPooling2D, Conv2D
from dl_bot import DLBot
from telegram_bot_callback import TelegramBotCallback




token = "5351420165:AAEpaaSsqQiQEltc9JzBn0WRJLY0tj1FS_w"
mlops_demo_bot = DLBot(token = token, user_id=788090772)
tg_bot_cb = TelegramBotCallback(mlops_demo_bot)


#parameters
BATCH_SIZE = 128
NUM_EPOCHS = 100
NUM_CLASSES = 10
INPUT_DIM = (28, 28, 1)

def create_model():
    model = Sequential()
    model.add(Conv2D(16, 3, activation='relu', input_shape = INPUT_DIM))
    model.add(Conv2D(32, 3, activation='relu'))
    model.add(MaxPooling2D((2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(NUM_CLASSES, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


data = mnist.load_data()
(X_train, y_train), (X_test, y_test) = data

n_samples_train = X_train.shape[0]
n_samples_test = X_test.shape[0]
dim = X_train.shape[1]

X_train = (X_train.reshape((n_samples_train, dim, dim, 1)).astype('float32'))/255.
X_test = (X_test.reshape((n_samples_test, dim, dim, 1)).astype('float32'))/255.
y_train = keras.utils.to_categorical(y_train, NUM_CLASSES)
y_test = keras.utils.to_categorical(y_test, NUM_CLASSES)

model = create_model()

model.fit(X_train, y_train, BATCH_SIZE, NUM_EPOCHS, validation_data=(X_test, y_test), callbacks = [tg_bot_cb])









    
