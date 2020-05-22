import sys
import tkinter
from tkinter import messagebox
from tkinter import ttk

def window_manage():

    window = tkinter.Tk()
    window.geometry("300x300")
    window.title("TMSG")
    window.grid_columnconfigure(0,weight = 1)
    window.iconbitmap("icon.ico")
    class game_count():
        def __init__(self,number,name,time=0):
            self.default_time = time
            self.flag = 1
            self.frame_gamename = tkinter.Frame(master = window,width = 200,bg = "#ffc000",bd = 4)
            self.label_gamename = tkinter.Label(master = self.frame_gamename,text = name,bg = "#ffc000",fg = "#fff",font = ("Arial",15,"bold"))
            self.frame_time = tkinter.Frame(master = window,width = 200,bg = "#4472c4")
            self.label_time = tkinter.Label(master = self.frame_time,text = 0,width = 200,bg = "#4472c4",fg = "#fff",font = ("Arial",15,"bold"))
            self.button_frame = tkinter.Frame(master = window,width = 300,height = 300)
            self.timer_button = tkinter.Button(master = self.button_frame,height = 3,width = 7,bd = 0,bg = "#ed7231",fg = "#fff",activebackground = "#ed320d",activeforeground = "#fff",command = self.reset_time)
            self.frame_gamename.grid(row = number*2,column = 0,columnspan = 3,sticky = "we")
            self.label_gamename.pack(anchor = "center",expand = 1)
            self.frame_time.grid(row = number*2+1,column = 0,sticky = "wens")
            self.label_time.pack()
            self.button_frame.grid(row = number*2+1,column = 2)
            self.timer_button.pack()
        def count_down(self):
            if int(self.label_time["text"]) > 0:
                i = int(self.label_time["text"])-1
                self.label_time["text"] = i
            elif self.flag == 0 and self.label_time["text"] == 0:
                self.flag = 1
        def reset_time(self):
            self.label_time["text"] = self.default_time
            self.flag = 0

    configfile_path = open("time_manage.txt",encoding = "utf-8")
    configfile_meta = configfile_path.readlines()
    create_gadgets = int(len(configfile_meta)/2)
    count_up = 1
    game_panel = [game_count(0,configfile_meta[0],configfile_meta[1])]

    while count_up < create_gadgets:
        game_panel.append(game_count(count_up,configfile_meta[count_up*2],configfile_meta[count_up*2+1]))
        count_up += 1
    def count_down():
        c = 0
        f = 0
        for f in game_panel:
            game_panel[c].count_down()
            c = c+1
        window.after(1000,count_down)
    count_down()
    window.mainloop()
window_manage()