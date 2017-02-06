#/usr/bin python
#!-*- coding:utf-8 -*-

import Tkinter

top = Tkinter.Tk()

quit = Tkinter.Button( top,text='exit!',command=top.quit )
quit.pack()

Tkinter.mainloop()