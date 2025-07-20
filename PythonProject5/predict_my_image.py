import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image  # Импортируем библиотеку Pillow
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Загрузка сохраненной модели ---
print("Загружаем обученную модель...")
try:
    model = load_model('mnist_cnn_model.h5')
    print("Модель успешно загружена.")
except Exception as e:
    print(f"Ошибка при загрузке модели: {e}")
    print("Убедитесь, что файл 'mnist_cnn_model.h5' находится в той же директории, что и этот скрипт.")
    exit()  # Выходим, если модель не загружена

# --- 2. Загрузка и предобработка вашего изображения ---
image_path = 'my_digit.png'  # <--- Укажите путь к вашему файлу изображения
print(f"\nЗагружаем и предобрабатываем изображение: {image_path}")

try:
    # Открываем изображение
    img = Image.open(image_path).convert('L')  # convert('L') - преобразует в оттенки серого

    # Изменяем размер до 28x28 пикселей
    img = img.resize((28, 28))

    # Преобразуем изображение в массив NumPy
    img_array = np.array(img)

    # Проверяем, нужно ли инвертировать цвета (если цифра черная на белом фоне)
    # MNIST имеет белые цифры на черном фоне. Если среднее значение пикселей высокое (белый фон), инвертируем.
    if np.mean(img_array) > 127:  # Если фон светлый, инвертируем
        img_array = 255 - img_array  # Инвертируем цвета
        print("Изображение инвертировано (черный фон, белая цифра).")

    # Нормализация пикселей (от 0-255 к 0-1)
    img_array = img_array.astype('float32') / 255.0

    # Изменение формы для модели (добавляем измерение для батча и канала)
    # (1, 28, 28, 1)
    img_array = img_array.reshape(1, 28, 28, 1)

    print("Изображение успешно предобработано.")

except FileNotFoundError:
    print(f"Ошибка: Файл '{image_path}' не найден. Убедитесь, что путь указан верно.")
    exit()
except Exception as e:
    print(f"Произошла ошибка при обработке изображения: {e}")
    exit()

# --- 3. Делаем предсказание ---
print("\nДелаем предсказание...")
predictions = model.predict(img_array)

# Получаем предсказанный класс (цифру)
predicted_class = np.argmax(predictions[0])
confidence = np.max(predictions[0]) * 100  # Уверенность в процентах

print(f"Модель предсказывает: {predicted_class}")
print(f"Уверенность: {confidence:.2f}%")

# --- 4. Визуализация результата ---
plt.imshow(img_array.reshape(28, 28), cmap='gray')
plt.title(f"Предсказано: {predicted_class} (Уверенность: {confidence:.2f}%)")
plt.axis('off')
plt.show()