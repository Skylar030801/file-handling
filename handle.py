from tkinter import*

root = Tk()
root.title("FILE HANDLING ")
root.geometry("1250x700")
root.configure(background="orange")

def create_file():
        file = open('/home/user/Desktop/weekendactivities.txt', 'w')
        file.write("i went for a drive\n")
        file.write("i went to my brother\n")
        file.write("i drank\n")
        file.write("slept by my sister\n")
        file.write("i moved")
        file.close()
def text_file():
        file = open('/home/user/Desktop/weekendactivities.txt', 'r')
        for each in file:
            TEXT.insert(END,each)
        file.close()

def append():
        file=open('/home/user/Desktop/weekendactivities.txt','a')
        file.writelines(TEXT.get("1.0","end-1c")+"\n")




titleLabel = Label (root, text = "MY WEEKEND ACTIVITIES", font = ("Arial", 20, "bold"), justify = CENTER)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady = 10, padx = 20)


# Create text widget and specify size.
TEXT = Text(root, height = 5, width = 40)
TEXT.grid(row = 3, column = 1, columnspan = 3, pady = 10, padx = 20)


create = Button(root, text = "CREATE TEXTFILE",font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green",activeforeground="blue", command=create_file)
create.grid(row = 5, column = 0, columnspan = 3, pady = 10, padx = 20)

DISPLAY = Button(root, text = "DISPLAY",font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green",activeforeground="blue", command=text_file)
DISPLAY.grid(row = 5, column = 2, columnspan = 3, pady = 10, padx = 20)

APPEND = Button(root, text = "APPEND DATA", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green", activeforeground="blue", command=append)
APPEND.grid(row = 5, column = 4, columnspan = 3, pady = 10, padx = 20)




EXIT = Button(root, text = "Exit", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green",activeforeground="blue",command = root.destroy)
EXIT.grid(row = 5, column = 10, columnspan = 3, pady = 10, padx = 20)

def clear():
    TEXT.delete('1.0', 'end')

clearButton = Button (root, text = "Clear", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = clear)
clearButton.grid(row = 5, column = 7,ipady = 8, ipadx = 12, pady = 5, sticky = NW)




mainloop()
