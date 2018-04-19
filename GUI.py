from Tkinter import *
import main


top = Tk()

Input_Label = Label(top, text = 'Starting address')
Input_Label.pack()

Input_Value = Variable()
Value = Entry(top, textvariable=Input_Value)
Value.pack()

def PressButton():
    x = Input_Value.get()
    CRC32Main2.main2(x)

GenerateButton = Button(top, text='Generate', command=PressButton)
GenerateButton.pack()

mainloop()
