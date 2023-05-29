def prog():
    from PIL import Image
    name = "2.3.jpg"
    with Image.open(name) as img:
        img.load()
    img_crop=img.crop((100, 100, 1300, 1000))
    img_crop.save('crop.jpg', quality=95)
def prog2():
    from PIL import Image
    ivents= {1:"Хэллоуин.jpg", 2:"ДеньСвятВален.jgp", 3:"СДнёмРожденья.jgp"}
    print()

    a=int(input("Мероприятие: \n"
                "1.Хэллоуин\n"
                "2.День святого валентина\n"
                "3.СДнёмРожденья\n"))
    name = ivents[a]
    with Image.open(name) as img:
        img.load()
    img.show()

def prog3():
    from PIL import Image, ImageDraw, ImageFont
    a = input('Введите имя того, кого хатите поздравить')
    image = Image.open("СДнёмРожденья.jpg")
    cons= a + ", Поздравляю"
    font = ImageFont.truetype("arial.ttf", 60)
    drawer = ImageDraw.Draw(image)
    drawer.text((800, 600), cons , font=font, fill="grey")
    image.save('new_img.jpg')
    image.show()
prog3()