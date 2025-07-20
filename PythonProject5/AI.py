import tensorflow as tf
from tensorflow.keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

# 1. Загрузка датасета MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("Исходные размеры данных:")
print(f"Обучающие изображения: {X_train.shape}") # (60000, 28, 28)
print(f"Обучающие метки: {y_train.shape}")     # (60000,)
print(f"Тестовые изображения: {X_test.shape}")  # (10000, 28, 28)
print(f"Тестовые метки: {y_test.shape}")      # (10000,)

# 2. Предобработка изображений (X_train, X_test)

# 2.1. Нормализация пикселей: приведение значений от 0-255 к 0-1
# Делим каждое значение пикселя на 255.0 (чтобы получить float)
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# 2.2. Изменение формы (Reshaping) для сверточных слоев
# Добавляем измерение для канала (1, так как изображения черно-белые)
# Теперь форма будет (количество_изображений, высота, ширина, 1)
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

print("\nРазмеры данных после предобработки изображений:")
print(f"Обучающие изображения: {X_train.shape}") # (60000, 28, 28, 1)
print(f"Тестовые изображения: {X_test.shape}")  # (10000, 28, 28, 1)

# 3. Предобработка меток (y_train, y_test)

# Преобразование меток в one-hot encoding
# Например, цифра 7 станет [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# Это необходимо для функции потерь categorical_crossentropy, которую мы будем использовать
num_classes = 10 # Цифры от 0 до 9
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)

print("\nРазмеры данных после предобработки меток (one-hot encoding):")
print(f"Обучающие метки: {y_train.shape}") # (60000, 10)
print(f"Тестовые метки: {y_test.shape}")  # (10000, 10)

# Проверим, как выглядит одно изображение после нормализации
plt.imshow(X_train[0].reshape(28, 28), cmap='gray') # Нужно убрать измерение канала для отображения
plt.title(f"Метка (one-hot): {y_train[0]}")
plt.show()

# --- Импорт всех необходимых библиотек в начале ---
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Загрузка и предобработка данных MNIST ---
print("Загрузка и предобработка данных...")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Нормализация
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Изменение формы
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

# One-hot encoding
num_classes = 10
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)
print("Данные предобработаны.")

# --- 2. Построение архитектуры CNN ---
print("\nПостроение архитектуры CNN...")
input_shape = X_train.shape[1:]

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.summary()
print("Архитектура CNN создана.")

# --- Следующие шаги (компиляция, обучение, оценка) будут добавлены сюда ---
# ...

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Загрузка и предобработка данных MNIST ---
print("Загрузка и предобработка данных...")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Нормализация
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Изменение формы
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

# One-hot encoding
num_classes = 10
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)
print("Данные предобработаны.")

# --- 2. Построение архитектуры CNN ---
print("\nПостроение архитектуры CNN...")
input_shape = X_train.shape[1:]

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])
model.summary()
print("Архитектура CNN создана.")

# --- 3. Компиляция модели ---
print("\nКомпиляция модели...")
model.compile(optimizer='adam',         # Оптимизатор Adam
              loss='categorical_crossentropy', # Функция потерь для многоклассовой классификации
              metrics=['accuracy'])      # Метрика для отслеживания (точность)
print("Модель скомпилирована.")

# --- 4. Обучение модели ---
print("\nНачинается обучение модели...")
# model.fit() - это метод для обучения модели
history = model.fit(X_train, y_train,   # Обучающие данные и метки
                    batch_size=128,     # Размер пакета (количество примеров, обрабатываемых за один раз)
                    epochs=10,          # Количество эпох (полных проходов по всему обучающему набору)
                    verbose=1,          # Отображать прогресс обучения
                    validation_data=(X_test, y_test)) # Данные для валидации (тестирования на каждом шаге)
print("Обучение завершено.")

# --- 5. Оценка модели ---
print("\nОценка модели на тестовых данных...")
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Потери на тестовых данных: {loss:.4f}")
print(f"Точность на тестовых данных: {accuracy:.4f}")

# --- Визуализация результатов обучения (опционально) ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Точность на обучении')
plt.plot(history.history['val_accuracy'], label='Точность на валидации')
plt.title('Точность модели')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Потери на обучении')
plt.plot(history.history['val_loss'], label='Потери на валидации')
plt.title('Потери модели')
plt.xlabel('Эпоха')
plt.ylabel('Потери')
plt.legend()

plt.show()

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Загрузка и предобработка данных MNIST ---
# Этот блок кода должен быть выполнен первым, чтобы X_train, y_train, X_test, y_test были доступны
print("Загрузка и предобработка данных...")
(X_train, y_train_raw), (X_test, y_test_raw) = mnist.load_data() # y_test_raw для отображения исходных меток

# Нормализация
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Изменение формы
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

# One-hot encoding для обучения (y_train, y_test)
num_classes = 10
y_train = tf.keras.utils.to_categorical(y_train_raw, num_classes)
y_test = tf.keras.utils.to_categorical(y_test_raw, num_classes)
print("Данные предобработаны.")

# --- 2. Построение архитектуры CNN ---
print("\nПостроение архитектуры CNN...")
input_shape = X_train.shape[1:]

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])
# model.summary() # Можно закомментировать, если уже видели

# --- 3. Компиляция модели ---
print("\nКомпиляция модели...")
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print("Модель скомпилирована.")

# --- 4. Обучение модели ---
print("\nНачинается обучение модели...")
history = model.fit(X_train, y_train,
                    batch_size=128,
                    epochs=10,
                    verbose=1,
                    validation_data=(X_test, y_test))
print("Обучение завершено.")

# --- НОВЫЙ БЛОК: Сохранение модели ---
print("\nСохраняем модель...")
model.save('mnist_cnn_model.h5') # Сохраняем модель в файл 'mnist_cnn_model.h5'
print("Модель сохранена как 'mnist_cnn_model.h5'")

# --- 5. Оценка модели ---
print("\nОценка модели на тестовых данных...")
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Потери на тестовых данных: {loss:.4f}")
print(f"Точность на тестовых данных: {accuracy:.4f}")

# --- Визуализация результатов обучения (опционально) ---
# ... (код для графиков, если хотите его снова отобразить) ...
# plt.show()


# --- НОВЫЙ БЛОК: Использование модели для предсказаний ---
print("\nДелаем предсказания на случайных тестовых изображениях...")

# Выбираем несколько случайных индексов из тестовой выборки
num_predictions = 5
random_indices = np.random.choice(len(X_test), num_predictions, replace=False)

plt.figure(figsize=(12, 4))
for i, idx in enumerate(random_indices):
    image_to_predict = X_test[idx] # Изображение для предсказания (уже предобработанное)
    true_label = y_test_raw[idx]   # Истинная метка (из сырых данных)

    # Модель ожидает батч, даже если это одно изображение,
    # поэтому добавляем еще одно измерение в начале
    # (1, 28, 28, 1) вместо (28, 28, 1)
    prediction_input = np.expand_dims(image_to_predict, axis=0)

    # Делаем предсказание
    predictions = model.predict(prediction_input)

    # predictions - это массив вероятностей (например, [0.01, 0.00, ..., 0.98, ...])
    # Наибольшая вероятность указывает на предсказанный класс
    predicted_class = np.argmax(predictions[0]) # predictions[0] потому что предсказание для одного изображения

    # Визуализация
    plt.subplot(1, num_predictions, i + 1)
    plt.imshow(image_to_predict.reshape(28, 28), cmap='gray') # Отображаем изображение
    plt.title(f"Истина: {true_label}\nПредсказано: {predicted_class}")
    plt.axis('off')

plt.suptitle("Предсказания модели на тестовых данных", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make room for suptitle
plt.show()