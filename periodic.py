from tkinter import *
import mysql.connector
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.geometry("1422x812+300+500")
root.wm_title('Periodic Table')
entry1 = ttk.Entry(root, textvariable = "input_text", justify = CENTER,
                                     font = ('courier', 15, 'bold'))
canvas = Canvas(root,width= 1422,height = 812)
image = ImageTk.PhotoImage(Image.open("Screen Shot 2020-06-02 at 04.17.29.jpeg"))
canvas.create_image(0,0,anchor= NW, image=image)
canvas.pack()
mylabel2 = Label(root, text = "enter the atomic number").place(x =4450,y= 280)

def myclick():
    mylabel = Label(root,text = "Please click for see all data!")
    mylabel.pack()
def enter():
    mylb = Label(root,text = e.get())
    mylb.pack()
e = Entry(root,width = 50,bg = "gray",fg="white",borderwidth = 6)
e.place(x=440, y = 270)
entry = e.get()

config = {
'user':'root',
'password':'74536600',
'host':'localhost',
'database' : 'mydb',
'port' : '3306'

}
cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
query = ("SELECT * FROM Basic_Properties ")
for i in cursor:
    print(i)

print(entry)
def call_groupandheat():
    root3 = Tk()
    root3.wm_title('Periodic Table')
    text2 = Text(root3)
    cursor.execute('''
    SELECT *
    FROM Name; ;''')
    elementsData2 = cursor.fetchall()
    text2.insert(INSERT, "Atomic Number ")
    text2.insert(INSERT, "        ")
    text2.insert(INSERT," Discovery ")
    text2.insert(INSERT, "        ")
    text2.insert(INSERT,"Naming    \n ")
    text2.insert(INSERT, "          ")


    for alldata2 in elementsData2:
        text2.insert(INSERT,(alldata2[0]))
        text2.insert(INSERT,"          ")
        text2.insert(INSERT, (alldata2[1]))
        text2.insert(INSERT,"          ")
        text2.insert(INSERT, (alldata2[3]))


        text2.insert(END,"\n" )
    text2.pack()

def call_find_all_sp():
    root2 = Tk()
    root2.wm_title('Periodic Table')
    text = Text(root2)

    cursor.execute('''
   SELECT * FROM Basic_Properties 
	''',(entry))
    elementsData= cursor.fetchall()
    # text1 = Tk.text(root2,height = 10, width = 20)
    # text1.config(state = "normal")

    text.insert(INSERT, "Atomic Number  ")
    text.insert(INSERT, "      ")
    text.insert(INSERT, "Phase   ")
    text.insert(INSERT, "       ")
    #text.insert(INSERT, "Density   ")
    #text.insert(INSERT, "       ")
    text.insert(INSERT, "Period   ")
    text.insert(INSERT, "      ")
    text.insert(INSERT,  "Name      \n ")


    #text.insert(INSERT, (alldata[0], "\t", alldata[1], "\t", alldata[2], "\t", alldata[3], "\t", alldata[4], "\n"))
    for alldata in elementsData:
        text.insert(INSERT,(alldata[0]))
        text.insert(INSERT,"         ")
        text.insert(INSERT, (alldata[1]))
        text.insert(INSERT,"          ")
        #text.insert(INSERT, (alldata[2]))
        #text.insert(INSERT,"          ")
        text.insert(INSERT,(alldata[3]))
        text.insert(INSERT,"          ")
        text.insert(INSERT, (alldata[4]))

        text.insert(END,"\n" )
    text.pack()

myButton = Button(root, text ="Get Name data ",  padx=5,pady = 5,command = call_groupandheat, fg = "blue", bg ="red").place(x=430,y=310)

enterBUtton = Button(root, text ="Basic Properties",  padx=5,pady = 5,command =call_find_all_sp, fg = "blue", bg ="red").place(x=550,y=310)

button_quit = Button(root, text = "Exit", padx=10,pady = 5,command = root.quit,fg = "red").place(x=850,y=310)
root.mainloop()
