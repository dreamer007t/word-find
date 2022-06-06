# Name:  Rabsun Shrestha    
# Student Number:  10494870


from tkinter import *# Used to create the GUI.
from tkinter import messagebox
import tkinter.messagebox # Used to show pop-up information windows.
import json # Used to convert between JSON-formatted text and Python variables.

class ProgramGUI:
    def __init__(self):
        self.main=tkinter.Tk()

        self.main.title('Word Find Log Viewer')
        try:
            with open('logs.txt','r') as f:
                self.logs=json.load(f)
        except:
            messagebox.showwarning('missing','file not found')
            self.main.destroy()
        self.current_log=0
        # 4 frames for 4 rows
        self.frame1=tkinter.Frame(self.main,padx='5',pady='5')
        self.frame2=tkinter.Frame(self.main,padx='5')
        self.frame3=tkinter.Frame(self.main,padx='5')
        self.frame4=tkinter.Frame(self.main,padx='5')
        # label/data for frame 1
        self.label1=tkinter.Label(self.frame1,justify='left',text='Letters:')
        self.label11=tkinter.Label(self.frame1)
        # label/data for frame 2
        self.label2=tkinter.Label(self.frame2,justify='right',text='Words:')
        self.label22=tkinter.Label(self.frame2)
        # label/data for frame 3
        self.label3=tkinter.Label(self.frame3,text='Score:')
        self.label33=tkinter.Label(self.frame3)
        # label/button for frame 1
        self.button1=tkinter.Button(self.frame4,text='Prev',command=self.previous_log)
        self.label4=tkinter.Label(self.frame4,justify='left')
        self.button2=tkinter.Button(self.frame4,text='Next',command=self.next_log)
        #label and button packing
        self.label1.pack(side='left',)
        self.label11.pack(side='left')
        self.label2.pack(side='left')
        self.label22.pack(side='left')
        self.label3.pack(side='left')
        self.label33.pack(side='left')        
        self.button1.pack(side='left')
        self.label4.pack(side='left')
        self.button2.pack(side='left')
        # frame packing     
        self.frame1.pack(fill=X,side='top')
        self.frame2.pack(fill=X)
        self.frame3.pack(fill=X)
        self.frame4.pack(fill=X)
        # show_log function call
        self.show_log()
        # to separate data in dictionaries
        self.s=','
        tkinter.mainloop()
        
    # This method displays the current log
    def show_log(self):
        s=','
        self.page=((self.current_log+1),'/',len(self.logs))
    
        current=self.logs[self.current_log]
        self.label11.configure(text=s.join(current['letters']))
        self.label22.configure(text=s.join(current['words']))
        self.label33.configure(text=(current['score']))
        self.label4.configure(text=(self.page))
            
         

# This method is called when the user clicks the "Previous" button.     
    def previous_log(self):
        # checking the edge of the log
        if self.current_log==0:
            messagebox.showwarning("Warning","No Previous Log.")
        else:
            self.current_log=self.current_log-1
            self.page=((self.current_log+1),'/',len(self.logs))
            current=self.logs[self.current_log]
            self.label11.configure(text=self.s.join(current['letters']))
            self.label22.configure(text=self.s.join(current['words']))
            self.label33.configure(text=(current['score']))
            self.label4.configure(text=(self.page))

# This method is called when the user clicks the "Next" button.
    def next_log(self):
        # checking the edge of the log
        if self.current_log==len(self.logs)-1:
            messagebox.showwarning("Warning","No Next Log.")
        else:
            
            self.current_log=self.current_log+1
            self.page=((self.current_log+1),'/',len(self.logs))
            
            current=self.logs[self.current_log]
            self.label11.configure(text=self.s.join(current['letters']))
            self.label22.configure(text=self.s.join(current['words']))
            self.label33.configure(text=(current['score']))
            self.label4.configure(text=(self.page))


gui = ProgramGUI()
