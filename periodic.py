from tkinter import *
import mysql.connector

from PIL import ImageTk, Image

root = Tk()
root.geometry("1422x812+300+500")
root.wm_title('Periodic Table')
canvas = Canvas(root,width= 1422,height = 812)
image = ImageTk.PhotoImage(Image.open("background.jpeg"))
canvas.create_image(0,0,anchor= NW, image=image)
canvas.pack()
mylabel2 = Label(root, text = "Enter the atomic number", fg = "blue", bg ="white").place(x =440,y= 280)


def enter():
    mylb = Label(root,text = e.get())
    mylb.pack()
e = Entry(root,width = 50,bg = "gray",fg="white",borderwidth = 6)
e.place(x=440, y = 300)


def delete():
    integer = e.get()
    print(integer)
    args = (integer,)

cursor.callproc('Delete_Element', args)



config = {
'user':'root',
'password':'psswd',
'host':'localhost',
'database' : 'mydb',
'port' : '3306'

}
cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()



def call_naming():
    root3 = Tk()
    root3.wm_title('Name')
    text2 = Text(root3)
    cursor.execute('''
    SELECT *
    FROM Name ;''')
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
    text.insert(INSERT, "Period   ")
    text.insert(INSERT, "      ")
    text.insert(INSERT,  "Name      \n ")


    #text.insert(INSERT, (alldata[0], "\t", alldata[1], "\t", alldata[2], "\t", alldata[3], "\t", alldata[4], "\n"))
    for alldata in elementsData:
        text.insert(INSERT,(alldata[0]))
        text.insert(INSERT,"         ")
        text.insert(INSERT, (alldata[1]))
        text.insert(INSERT,"          ")
        text.insert(INSERT,(alldata[3]))
        text.insert(INSERT,"          ")
        text.insert(INSERT, (alldata[4]))
        text.insert(END,"\n" )
    text.pack()

myButton = Button(root, text ="Get Name data ",  padx=5,pady = 5,command = call_naming, fg = "blue", bg ="red").place(x=443,y=339)

deleteBUtton = Button(root, text ="Delete the element",  padx=5,pady = 5,command =delete, fg = "blue", bg ="red").place(x=780,y=339)

#button_quit = Button(root, text = "Exit", padx=10,pady = 5,command = root.quit,fg = "red").place(x=850,y=310)
root.mainloop()
