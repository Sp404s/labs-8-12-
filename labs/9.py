def prog1():
    import os
    from PIL import Image, ImageFilter
    print("Методы обработки изоб: \n"
          "1.Детализировать\n"
          "2.Улучшить резкость\n"
          "3.Найти контуры\n"
          "4.Метод теснение")
    a = int(input())
    directory = os.listdir(os.getcwd()+"\Изображения для обработки")
    print(directory)
    eff = [ImageFilter.DETAIL, ImageFilter.SHARPEN, ImageFilter.CONTOUR, ImageFilter.EMBOSS]
    for file in directory:
        os.chdir(r"C:\Users\Alex\PycharmProjects\pythonProject3\labs\Изображения для обработки")
        with Image.open(file) as img:
            os.chdir(r"C:\Users\Alex\PycharmProjects\pythonProject3\labs\Обработанные картинки")
            img.load()
            new_img = img.filter(eff[a - 1])
            new_img.save(file)
def prog2():
    import os
    from PIL import Image, ImageFilter
    print("Методы обработки изоб: \n"
          "1.Детализировать\n"
          "2.Улучшить резкость\n"
          "3.Найти контуры\n"
          "4.Метод теснение")
    a = int(input())
    directory = os.listdir(os.getcwd() + "\Изображения для обработки")
    eff = [ImageFilter.DETAIL, ImageFilter.SHARPEN, ImageFilter.CONTOUR, ImageFilter.EMBOSS]
    for file in directory:
         os.chdir(r"C:\Users\Alex\PycharmProjects\pythonProject3\labs\Изображения для обработки")
         with Image.open(file) as img:
            if img.format == "JPEG" or "PNG":
                os.chdir(r"C:\Users\Alex\PycharmProjects\pythonProject3\labs\Обработанные картинки")
                img.load()
                new_img = img.filter(eff[a - 1])
                new_img.save(file)

def prog3():
    import csv
    a=0
    with open("Списк.csv", newline='') as file:
        r = csv.DictReader(file,delimiter=";")
        print("Нужно купить:")
        for i in r:
            a+=int(i["Количество"])* int(i["Цена"])
            print(i["Продукт"]+ " -", i["Количество"]+" шт.", i["Цена"]+" руб.")
        print("Итоговая сумма:", a, "руб")
prog3()