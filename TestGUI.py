import tkinter
class MyGUI:
  def __init__(self):
 #Create the main window widget
    self.main_window = tkinter.Tk()
 ## ADD CODE HERE
 #create frame here
    self.frame_left = tkinter.Frame(self.main_window)
    self.frame_right = tkinter.Frame(self.main_window)
 #add components
    self.my_label1 = tkinter.Label(self.frame_left,text='Label One')
    self.my_label1.pack()
    self.my_label2 = tkinter.Label(self.frame_left,text='Label Two')
    self.my_label2.pack()
    self.my_label3 = tkinter.Label(self.frame_left,text='Label Three')
    self.my_label3.pack()
    self.my_label4 = tkinter.Label(self.frame_right,text='Label One')
    self.my_label4.pack(side='left')
    self.my_label5 = tkinter.Label(self.frame_right,text='Label Two')
    self.my_label5.pack(side='left')
    self.my_label6 = tkinter.Label(self.frame_right,text='Label Three')
    self.my_label6.pack(side='left')
 #pack frames after you add everything to them
    self.frame_left.pack(side='left')
    self.frame_right.pack(side='right')

 #enter loop
    tkinter.mainloop()
my_gui = MyGUI()