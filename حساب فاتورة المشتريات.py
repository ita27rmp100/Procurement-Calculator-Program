from tkinter import *
from tkinter import ttk
from database_facture import price
t = Tk()
g = Tk()
t.title("إضافة المشتريات")
g.title("الفاتورة")
t.geometry("170x80")
g.geometry("270x240")
t.resizable(0,0)
g.resizable(0,0)
mountej = StringVar()
su=[]
def nt () : #لإضافة  البيانات المدخلة في نافذة حاسبة المشتريات إلى نافذة الفاتورة و بالضبط في الليست بوكس
    txt = f"{float(e2.get())* float(price(mountej.get()))}             {price(mountej.get())}         {e2.get()}       {mountej.get()}"
    txt = f"{mountej.get()}       {e2.get()}         {price(mountej.get())}             {float(e2.get())* float(price(mountej.get()))}"
    lb.insert(END,txt)
    su.append(float(e2.get())* float(price(mountej.get())))
    mountej.set("")
    l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=200)
def clear() : #لحذف جميع العناصر الموجودة في الليستبوكس
    x = lb.size()
    lb.delete(0,x)
    su.clear()
    l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=200)
def clear1() : #لحذف آخر عنصر في ا ليست بوكس 
    xd = lb.size() - 1
    lb.delete(xd)
    su.pop()
    #"Onions"
    l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=200)
def key(event) : #نفس عمل الدالة الثانية و الأخيرة و لكن تقوم بذلك عند الضغط على زر معين الكيبورد
    if event.keysym == "F1": #عند الضغط على الزر أف1 يقوم  في الكيبورد يقوم بنفس مهام الدالة كلير
        x = lb.size()
        lb.delete(0,x)
        su.clear()
        l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=300)
    if event.keysym == "F2": #عند الضغط على زر أف2 يقوم بنفس مهام الدالة كلير1
        xd = lb.size() - 1
        lb.delete(xd)
        su.pop()
        l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=300)

l1 = Label(t,text="product name :",width=11,bd=0)
l1.place(x=15,y=0)
l2 = Label(t,text="Quantity :",width=10,bd=0)
l2.place(x=100,y=0)
e1 = ttk.Combobox(t,textvariable=mountej,width=7)
e1.place(x=15,y=20)
e1["values"]=['Potatos', 'Onions', 'Tomatoes', 'Garlic', 'Leeks', 'Caroots', 'Fennel']
e2 = Spinbox(t,width=5,from_=1,to=5)
e2.place(x=112,y=20)
b = Button(t,text="Add to bill",command=nt,bg="green",fg="white")
b.place(x=60,y=43)
ls = Label(g,text="p.n          Q       p           t.p",font=("arial",10))
ls.place(x=40,y=0)
lb = Label(g,text="إجمالي ثمن الشراء").place(x=120,y=200)
lb = Listbox(g,width=30,fg="black")
#يستخدم السطرين التاليين لاستقبال ضغطات الكيبورد و هي تابعة للدالة كاي اللي فوق 
lb.bind("<Key>",key)
lb.focus_set()
lb.place(x=40,y=30)
my_menu = Menu(g)
g.configure(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="خيارات المسح",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="F1               مسح كلي",command=clear)
file_menu.add_command(label="F2          مسح آخر عنصر",command=clear1)
g.mainloop()
t.mainloop()
