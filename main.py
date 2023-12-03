import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO


def get_cat_image():
    # Получаем URL случайной картинки кота
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        json_response = response.json()
        image_url = json_response[0]['url']
        return image_url
    else:
        print("Ошибка при получении картинки:", response.status_code)
        return None


def show_cat_image():
    image_url = get_cat_image()
    if image_url:
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            # Отображаем картинку в Tkinter
            image_data = Image.open(BytesIO(image_response.content))
            image_data.thumbnail((300, 300))  # Изменено здесь
            img = ImageTk.PhotoImage(image_data)

            label.config(image=img)
            label.image = img  # Сохраняем ссылку на изображение
        else:
            print("Ошибка при загрузке картинки:", image_response.status_code)


# Создаем главное окно
root = tk.Tk()
root.title("Картинки котиков")

# Добавляем метку для отображения картинки
label = tk.Label(root)
label.pack()

# Добавляем кнопку для загрузки новой картинки
button = tk.Button(root, text="Загрузить новую картинку", command=show_cat_image)
button.pack()

# Загружаем первую картинку
show_cat_image()

# Запускаем приложение
root.mainloop()
