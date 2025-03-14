def price (name_of_veg) :
    price_of_veg = {}
    from tkinter import messagebox
    import csv
    with open(r"D:\Clas2.csv","r") as f :
        readf = csv.reader(f,delimiter=",")
        data = list(readf)
        for i in range(len(data)) :
            x = data[i]
            y = x[0]
            price_of_veg[y[0:y.index(";")]]=y[y.index(";")+1:len(y)]
        try :
            return  price_of_veg[name_of_veg]
        except :
            messagebox.showerror("خطأ","المنتج غير موجود ، يمكنك إضافته الآن")
def lp(mode) : #دالة لاستخراج العناصر الموجودة من ملف الاكسل
    price_of_veg = {}
    from tkinter import messagebox
    import csv
    with open(r"D:\Clas2.csv", "r") as f:
        readf = csv.reader(f, delimiter=",")
        data = list(readf)
        for i in range(len(data)):
            x = data[i]
            y = x[0]
            price_of_veg[y[0:y.index(";")]] = y[y.index(";") + 1:len(y)]
        if mode == "d" :
            return price_of_veg
        if mode == "l" :
            x = list(price_of_veg.keys())
            return x
