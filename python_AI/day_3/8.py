import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(x_train, y_train, epochs=5, validation_split=0.1)


loss, acc = model.evaluate(x_test, y_test)
print(f"테스트 정확도: {acc:.4f}")


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure(figsize=(8, 4))
for i in range(5):
    image = x_test[i]
    label = y_test[i]
    pred = model.predict(image.reshape(1, 28, 28, 1)).argmax()

    plt.subplot(1, 5, i+1)
    plt.imshow(image.reshape(28, 28), cmap='gray')
    plt.title(f"예측: {class_names[pred]}")
    plt.axis('off')
plt.tight_layout()
plt.show()