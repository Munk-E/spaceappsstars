import tkinter as tk
from tkinter import ttk
from tkinter import *
#def main ():

def starChoose(root):
    def makeSomething(value):
        global goodFile
        #root.after(0,lambda:root.destroy())
        goodFile = value
        sliderBoy(root)
    Button(root, text='Cygnus 2',command=lambda *args: makeSomething('Cyg2.txt')).grid()
    Button(root, text='Orion 1',command=lambda *args: makeSomething('Orion1.txt')).grid()
    Button(root, text='Saggitarius 4',command=lambda *args: makeSomething('Sag4.txt')).grid()
#...etc

def sliderBoy(root):
    count = 0
    with open(goodFile) as fp:
        for line in fp:
            if line.strip():
                count += 1

    print('number of non-blank lines', count)

    # root window
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('Luminosity over time')


    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)


    # slider current value

    current_value = tk.IntVar()


    def get_current_value():
        file = open(goodFile)
  
    # read the content of the file opened
        content = file.readlines()
        return content[current_value.get()]
    #return '{: .0f}'.format(current_value.get())


    def slider_changed(event):
        value_label.configure(text=get_current_value())


# label for the slider
    slider_label = ttk.Label(root,text='Slider:')
    slider_label.grid(column=0,row=0,sticky='w')

#  slider
    slider = ttk.Scale(root,from_=0,to=count-1,orient='horizontal',command=slider_changed,variable=current_value)

    slider.grid(column=1,row=0,sticky='we')

# current value label
    current_value_label = ttk.Label(root,text='Current Value:')

    current_value_label.grid(row=1,columnspan=2,sticky='n',ipadx=10,ipady=10)

    # value label
    value_label = ttk.Label(root,text=get_current_value())
    value_label.grid(row=2,columnspan=2,sticky='n')

def main():
    root = tk.Tk()
    app = starChoose(root)
    root.mainloop()

main()
