from tkinter import * 
t = Tk()
g = Tk()
t.title("إضافة المشتريات")
g.title("الفاتورة")
t.geometry("228x100")
g.geometry("300x330")
mountej = StringVar()
thamen = IntVar()
su=[]
def nt () : #لإضافة  البيانات المدخلة في نافذة حاسبة المشتريات إلى نافذة الفاتورة و بالضبط في الليست بوكس
    txt = f"{thamen.get()* float(e2.get())}             {thamen.get()}         {e2.get()}       {mountej.get()}"
    lb.insert(END,txt)
    su.append(thamen.get()*float(e2.get()))
    thamen.set(0)
    mountej.set("")
    l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=300)
def clear() : #لحذف جميع العناصر الموجودة في الليستبوكس
    x = lb.size()
    lb.delete(0,x)
    su.clear()
    l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=300)
def clear1() : #لحذف آخر عنصر في ا ليست بوكس 
    xd = lb.size() - 1
    lb.delete(xd)
    su.pop()
    l4 = Label(g,text=str(sum(su)),width=15).place(x=10,y=300)
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

l1 = Label(t,text="الثمن للواحدة",width=10,bd=0)
l1.grid(row=1,column=3)
l2 = Label(t,text="الكمية",width=10,bd=0)
l2.grid(row=1,column=5)
l3 = Label(t,text="إسم المنتج",width=10,bd=0)
l3.grid(row=1,column=7)
e1 = Entry(t,textvariable=thamen,width=5,bd=0)
e1.grid(row=2,column=3)
e2 = Spinbox(t,width=5,bd=0,from_=1,to = 10)
e2.grid(row=2,column=5)
e3 = Entry(t,textvariable=mountej,width=5,bd=0)
e3.grid(row=2,column=7)
b = Button(t,text="إضافة إلى الفاتورة",command=nt)
b.grid(row=3,column=5)
ls = Label(g,text="إسم المنتوج    الكمية    الثمن للواحدة       المجموع")
ls.place(x=40,y=0)
lb = Label(g,text="إجمالي ثمن الشراء").place(x=120,y=300)
lb = Listbox(g,width=30)
#يستخدم السطرين التاليين لاستقبال ضغطات الكيبورد و هي تابعة للدالة كاي اللي فوق 
lb.bind("<Key>",key)
lb.focus_set()
lb.place(x=40,y=30)
my_menu = Menu(g)
g.configure(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="خيارات المسح",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="مسح كلي",command=clear)
file_menu.add_command(label="مسح آخر عنصر",command=clear1)
g.mainloop()
t.mainloop()


    
