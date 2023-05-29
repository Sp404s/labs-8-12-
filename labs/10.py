def prog1():
    import json
    with open("1.json", encoding='utf-8' ) as f:
        data = json.load(f)
    prod=data['products']
    for i in prod:
        print('Название: '+ i["name"])
        print('Цена: ' + str(i["price"]))
        print('Вес: ' + str(i["weight"]))
        if i['available']==True:
            print('В наличии', "\n")
        else:
            print('Нет в наличии', "\n")
def prog2():
    import json
    name=input("Название: ")
    price=input("Цена: ")
    aval= input("Есть в наличии: ")
    weight=input("Вес: ")
    def change(data):
        with open("2.json","r+",encoding='utf-8') as file:
            file_data = json.load(file)
            file_data['products'].append(data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    if aval == "Да":
        aval=True
    else:
        aval=False
    y = {
        "name": name,
        "price": price,
        "available": aval,
        "weight": weight
        }
    change(y)
    with open("2.json", encoding='utf-8') as f:
        data = json.load(f)
    prod = data['products']
    for i in prod:
        print('Название: ' + i["name"])
        print('Цена: ' + str(i["price"]))
        print('Вес: ' + str(i["weight"]))
        if i['available'] == True:
            print('В наличии', "\n")
        else:
            print('Нет в наличии', "\n")
def prog3():
    with open('en-ru.txt', 'r') as f:
        ru_en = {}
        for line in f.readlines():
            words = line.strip().split(" - ")
            if len(words) == 2:
                ru_words = words[1].split(", ")
                for ru_word in ru_words:
                    if ru_word not in ru_en:
                        ru_en[ru_word] = []
                    ru_en[ru_word].append(words[0])
        with open('ru-en.txt', 'w') as out_f:
            for ru_word in sorted(ru_en.keys()):
                en_words = ", ".join(sorted(ru_en[ru_word]))
                out_f.write(f"{ru_word} - {en_words}\n")
prog3()