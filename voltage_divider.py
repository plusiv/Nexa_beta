#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 22, 2018 12:40:05 AM AST  platform: Linux

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import voltage_divider_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    voltage_divider_support.set_Tk_var()
    top = Divisor_de_voltaje (root)
    voltage_divider_support.init(root, top)
    root.mainloop()

w = None
def create_Divisor_de_voltaje(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    voltage_divider_support.set_Tk_var()
    top = Divisor_de_voltaje (w)
    voltage_divider_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Divisor_de_voltaje():
    global w
    w.destroy()
    w = None

#**********************Edited************************************

#----------------------Ecuations solver function-----------------
    
def calculate(self, R1, V_in, V_out):
    R2 = (V_out*R1)/(V_in - V_out)
    if(R2<0):
        R2 = R2*(-1)
        
    text_result = """
    R2 = {}
    """.format(round(R2,2))
        
    self.Results_label.configure(text=text_result)
        
#************************Edited************************************






class Divisor_de_voltaje:



    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {DejaVu Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("548x477+418+211")
        top.title("Divisor de voltaje")
        top.configure(background="#2d3436")
        top.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.036, rely=0.042, relheight=0.22
                , relwidth=0.912)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="#ffffff")
        self.Labelframe1.configure(text='''Resistencias''')
        self.Labelframe1.configure(background="#2d3436")
        self.Labelframe1.configure(width=500)

        self.r1 = Entry(self.Labelframe1)
        self.r1.place(relx=0.36, rely=0.476, height=23, relwidth=0.252
                , bordermode='ignore')
        self.r1.configure(background="white")
        self.r1.configure(font="TkFixedFont")
        self.r1.configure(relief=FLAT)
        self.r1.configure(selectbackground="#c4c4c4")
        self.r1.configure(textvariable=voltage_divider_support.r1)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.28, rely=0.429, height=31, width=39
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#2d3436")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''R1''')
        self.Label1.configure(width=39)

        self.Labelframe1_1 = LabelFrame(top)
        self.Labelframe1_1.place(relx=0.036, rely=0.294, relheight=0.178
                , relwidth=0.912)
        self.Labelframe1_1.configure(relief=GROOVE)
        self.Labelframe1_1.configure(foreground="#ffffff")
        self.Labelframe1_1.configure(text='''Voltajes''')
        self.Labelframe1_1.configure(background="#2d3436")
        self.Labelframe1_1.configure(width=500)

        self.V_out = Entry(self.Labelframe1_1)
        self.V_out.place(relx=0.6, rely=0.471, height=23, relwidth=0.172
                , bordermode='ignore')
        self.V_out.configure(background="white")
        self.V_out.configure(font="TkFixedFont")
        self.V_out.configure(selectbackground="#c4c4c4")
        self.V_out.configure(textvariable=voltage_divider_support.v_out)

        self.V_in = Entry(self.Labelframe1_1)
        self.V_in.place(relx=0.24, rely=0.471, height=23, relwidth=0.172
                , bordermode='ignore')
        self.V_in.configure(background="white")
        self.V_in.configure(font="TkFixedFont")
        self.V_in.configure(selectbackground="#c4c4c4")
        self.V_in.configure(textvariable=voltage_divider_support.v_in)

        self.Label2 = Label(self.Labelframe1_1)
        self.Label2.place(relx=0.16, rely=0.471, height=21, width=25
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(background="#2d3436")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Vin''')

        self.Label3 = Label(self.Labelframe1_1)
        self.Label3.place(relx=0.48, rely=0.471, height=21, width=49
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(background="#2d3436")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Vout''')
        self.Label3.configure(width=49)

        self.Labelframe1_2 = LabelFrame(top)
        self.Labelframe1_2.place(relx=0.036, rely=0.503, relheight=0.325
                , relwidth=0.912)
        self.Labelframe1_2.configure(relief=GROOVE)
        self.Labelframe1_2.configure(foreground="#ffffff")
        self.Labelframe1_2.configure(text='''Resultados''')
        self.Labelframe1_2.configure(background="#2d3436")
        self.Labelframe1_2.configure(width=500)

        self.Results_label = Label(self.Labelframe1_2)
        self.Results_label.place(relx=0.02, rely=0.194, height=111, width=479
                , bordermode='ignore')
        self.Results_label.configure(activebackground="#f9f9f9")
        self.Results_label.configure(background="#2d3436")
        self.Results_label.configure(foreground="#ffffff")
        self.Results_label.configure(text='''Los resultados aparecerán aqui''')

        self.Calculate = Button(top, command=lambda:calculate(self,
                                                                   voltage_divider_support.r1.get(),
                                                                   voltage_divider_support.v_in.get(),
                                                                   voltage_divider_support.v_out.get()
                                                                   ))
        self.Calculate.place(relx=0.036, rely=0.86, height=39, width=499)
        self.Calculate.configure(activebackground="#d9d9d9")
        self.Calculate.configure(background="#00b894")
        self.Calculate.configure(font=font9)
        self.Calculate.configure(highlightbackground="#00b894")
        self.Calculate.configure(relief=FLAT)
        self.Calculate.configure(text='''Calcular''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()



