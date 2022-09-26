from tkinter import *
import urllib.request
from xml.dom import minidom

# получение курса валюты
def cur(s):
    dict = ['CAD', 'USD', 'EUR', 'CNY', 'JPY']
    f, n = open('exchange.txt'), 1
    for line in f:
        if n == 1 or n == 2:
            n += 1
            continue
        else:
            str = line
            a = str.split("; ")
            if a[3] == dict[s]:
                t = a[4][0:-2]
                t = t.replace(',', '.')
                return float(t)
                break

# вычисление суммы
def sum(s, c1, c2):
    return '%.2f' %(s * c1 / c2)

# очистка данных
def clear_():
    kanada.set(''), russia.set(''), usa.set(''), euro.set(''), china.set(''),
    japan.set('')

#вывод количества валюты по введённой сумме
def callbackFunc():
    inda = [kanada.get(), usa.get(), euro.get(), russia.get(), china.get(),
    japan.get()]
    if inda[0] != '': # kanada
        s = int(inda[0])
        kanada.set(s), russia.set(s * cur(0)), usa.set(sum(s, cur(0),
        cur(1))), euro.set(sum(s, cur(0), cur(2))), china.set(sum(s*10,
        cur(0), cur(3))), japan.set(sum(s*100, cur(0), cur(4)))
    elif inda[1] != '': # usa
        s = int(inda[1])
        kanada.set(sum(s, cur(1), cur(0))), russia.set('%.2f' %(s * cur(1))),
        usa.set(s), euro.set(sum(s, cur(1), cur(2))), china.set(sum(s*10, cur(1),
        cur(3))), japan.set(sum(s*100, cur(1), cur(4)))
    elif inda[2] != '': # euro
        s = int(inda[2])
        kanada.set(sum(s, cur(2), cur(0))), russia.set(s * cur(2)),
        usa.set(sum(s, cur(2), cur(1))), euro.set(s), china.set(sum(s*10, cur(2),
        cur(3))), japan.set(sum(s*100, cur(2), cur(4)))
    elif inda[3] != '': # russia
        s = int(inda[3])
        kanada.set('%.2f' %(s / cur(0))), russia.set(s),
        usa.set('%.2f' %(s / cur(1))), euro.set('%.2f' %(s / cur(2))),
        china.set('%.2f' %(s*10 / cur(3))), japan.set('%.2f' %(s*100 / cur(4)))
    elif inda[4] != '': # china
        s = int(inda[4]) / 10
        kanada.set(sum(s, cur(3), cur(0))), russia.set(s * cur(3)),
        usa.set(sum(s, cur(3), cur(1))), euro.set(sum(s, cur(3), cur(2))),
        china.set(s*10), japan.set(sum(s*100, cur(3), cur(4)))
    elif inda[5] != '': # japan
        s = int(inda[5]) / 100
        kanada.set(sum(s, cur(4), cur(0))), russia.set(s*100 * cur(4)),
        usa.set(sum(s, cur(4), cur(1))), euro.set(sum(s, cur(4), cur(2))),
        china.set(sum(s*10, cur(4), cur(3))), japan.set(s*100)


# графическая оболочка
app = Tk() 
app.geometry('395x100')
app.title('Курс валют ЦБ РФ на сегодня')

# создание файла с курсами валют
# Ежедневные курсы валют ЦБ РФ
url = "http://www.cbr.ru/scripts/XML_daily.asp"

# Чтение URL
webFile = urllib.request.urlopen(url)
data = webFile.read()
	
# Имя файла
UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")

with open(FileName, "wb") as localFile:
    localFile.write(data)

webFile.close()

# Парсинг xml и запись данных в файл
doc = minidom.parse(FileName)

# Извлечение даты
root = doc.getElementsByTagName("ValCurs")[0]
date = "Курс валют ЦБ РФ на {date}г. \n".format(date=root.getAttribute('Date'))

# Заголовок CSV
head = "Идентификатор; Номинал; Название валюты; Сокращение; Курс (руб) \n"

# Извлечение данных по валютам
with open("exchange.txt","w") as out:
    out.write(date)
    out.write(head)
    for rate in doc.getElementsByTagName("Valute"):
        vid = rate.getAttribute("ID")
        charcode = rate.getElementsByTagName("CharCode")[0]
        name = rate.getElementsByTagName("Name")[0]
        value = rate.getElementsByTagName("Value")[0]
        nominal = rate.getElementsByTagName("Nominal")[0]
        str = "{0}; {1}; {2}; {3}; {4} \n".format(vid, nominal.firstChild.data,
        name.firstChild.data, charcode.firstChild.data, value.firstChild.data)
        out.write(str)


# колонки названий стран
# первая колонка
stringkanada = Label(app, text = "Канада")
stringkanada.grid(column=1, row=0, sticky=W)
stringusa = Label(app, text = "США")
stringusa.grid(column=1, row=1, sticky=W)
stringeuro = Label(app, text = "Евросоюз")
stringeuro.grid(column=1, row=2, sticky=W)
# вторая колонка
stringrussia = Label(app, text = "Россия")
stringrussia.grid(column=2, row=0, sticky=W)
stringchina = Label(app, text = "Китай")
stringchina.grid(column=2, row=1, sticky=W)
stringjapan = Label(app, text = "Япония")
stringjapan.grid(column=2, row=2, sticky=W)


# поля ввода
# первая колонка
kanada = StringVar()
usa = StringVar()
euro = StringVar()
# вторая колонка
russia = StringVar()
china = StringVar()
japan = StringVar()

# первая колонка
entrykanada = Entry(app, width=20, textvariable=kanada)
entryusa = Entry(app, width=20, textvariable=usa)
entryeuro = Entry(app, width=20, textvariable=euro)
# вторая колонка
entryrussia = Entry(app, width=20, textvariable=russia)
entrychina = Entry(app, width=20, textvariable=china)
entryjapan = Entry(app, width=20, textvariable=japan)

# первая колонка
entrykanada.grid(column=0, row=0, padx=10)
entryusa.grid(column=0, row=1, padx=10)
entryeuro.grid(column=0, row=2, padx=10)
# вторая колонка
entryrussia.grid(column=3, row=0, padx=10)
entrychina.grid(column=3, row=1, padx=10)
entryjapan.grid(column=3, row=2, padx=10)


# кнопки
resultButton = Button(app, text = 'Рассчитать', command=callbackFunc)
resultButton.grid(column=0, row=3, pady=10, sticky=N)
clear_Button = Button(app, text = 'Очистить', command=clear_)
clear_Button.grid(column=3, row=3, pady=10, sticky=N)

app.mainloop()
