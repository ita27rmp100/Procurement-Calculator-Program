# السلام عليكم و رحمة الله تعال و بركاته ـ، معكم المبرمج عبد الرحيم في فيديو جديد ، في هذا الفيديو سنعرض لكم برنامج حاسبة المشتريات بعد تطويره ( إضافة بعض التعديلات عليه )
from tkinter import *
from tkinter import ttk
from database_facture import *
t = Tk()
g = Tk()
t.title("Add purchases")
g.title("Purchase invoice")
t.iconbitmap(r"C:\Users\SeVeN\Downloads\تجارة.ico")
g.iconbitmap(r"C:\Users\SeVeN\Downloads\تجارة (1).ico")
t.iconwindow()
t.geometry("170x80")
g.geometry("270x230")
t.resizable(0,0)
g.resizable(0,0)
mountej = StringVar()
su=[]
price_of_veg = {}
def nt () : #لإضافة  البيانات المدخلة في نافذة حاسبة المشتريات إلى نافذة الفاتورة و بالضبط في الليست بوكس
    txt = f"{float(e2.get())* float(price(mountej.get()))}             {price(mountej.get())}         {e2.get()}       {mountej.get()}"
    txt = f"{mountej.get()}       {e2.get()}         {price(mountej.get())}             {float(e2.get())* float(price(mountej.get()))}"
    lb.insert(END,txt)
    su.append(float(e2.get())* float(price(mountej.get())))
    mountej.set("")
    l4 = Label(g,text=str(sum(su)),width=15).place(x=150,y=200)
def clear() : #لحذف جميع العناصر الموجودة في الليستبوكس
    x = lb.size()
    lb.delete(0,x)
    su.clear()
    l4 = Label(g,text=str(sum(su)),width=15).place(x=150,y=200)
def clear1() : #لحذف آخر عنصر في ا ليست بوكس 
    xd = lb.size() - 1
    lb.delete(xd)
    su.pop()
    #"Onions"
    l4 = Label(g,text=str(sum(su)),width=15).place(x=150,y=200)
def key(event) : #نفس عمل الدالة الثانية و الأخيرة و لكن تقوم بذلك عند الضغط على زر معين الكيبورد
    if event.keysym == "F1": #عند الضغط على الزر أف1 يقوم  في الكيبورد يقوم بنفس مهام الدالة كلير
        x = lb.size()
        lb.delete(0,x)
        su.clear()
        l4 = Label(g,text=str(sum(su)),width=15).place(x=150,y=300)
    if event.keysym == "F2": #عند الضغط على زر أف2 يقوم بنفس مهام الدالة كلير1
        xd = lb.size() - 1
        lb.delete(xd)
        su.pop()
        l4 = Label(g,text=str(sum(su)),width=15).place(x=150,y=300)

l1 = Label(t,text="product name :",width=11,bd=0)
l1.place(x=15,y=0)
l2 = Label(t,text="Quantity :",width=10,bd=0)
l2.place(x=100,y=0)
e1 = ttk.Combobox(t,textvariable=mountej,width=7)
e1.place(x=15,y=20)
e1["values"]= lp("l")
e2 = Spinbox(t,width=5,from_=1,to=5)
e2.place(x=112,y=20)
b1 = Button(t,text="Add to bill",command=nt,bg="green",fg="white",width=12)
b1.place(x=40,y=48)
ls = Label(g,text="p.n          Q       p           t.p",font=("arial",10))
ls.place(x=40,y=0)
lb = Label(g,text="The total purchase price :").place(x=10,y=200)
lb = Listbox(g,width=30,fg="black")
#يستخدم السطرين التاليين لاستقبال ضغطات الكيبورد و هي تابعة للدالة كاي اللي فوق 
lb.bind("<Key>",key)
lb.focus_set()
lb.place(x=40,y=30)
my_menu = Menu(g)
g.configure(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="Scan options",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Total scan                  F1",command=clear)
file_menu.add_command(label="Clear the last item    F2",command=clear1)
g.mainloop()
t.mainloop()
