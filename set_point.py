#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 21, 2018 11:59:51 PM AST  platform: Linux

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

import set_point_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Toplevel()
    set_point_support.set_Tk_var()
    top = Set_Point (root)
    set_point_support.init(root, top)
    root.mainloop()

w = None
def create_Set_Point(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    set_point_support.set_Tk_var()
    top = Set_Point (w)
    set_point_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Set_Point():
    global w
    w.destroy()
    w = None

#**********************Edited************************************

#----------------------Ecuations solver function-----------------
    
def calculate(self, Pot, V_in, V_out_min, V_out_max):
    I = (V_out_max - V_out_min)/Pot
    R1 = (V_in - V_out_max)/I
    R2 = V_out_min/I
        
    text_result = """
    R1 = {}
    R2 = {}
    """.format(round(R1, 2), round(R2,2))
        
    self.Results_label.configure(text=text_result)
        
#************************Edited************************************





class Set_Point:


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
        top.title("Set Point")
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

        self.I_max = Entry(self.Labelframe1)
        self.I_max.place(relx=0.4, rely=0.571, height=23, relwidth=0.252
                , bordermode='ignore')
        self.I_max.configure(background="white")
        self.I_max.configure(font="TkFixedFont")
        self.I_max.configure(relief=FLAT)
        self.I_max.configure(selectbackground="#c4c4c4")
        self.I_max.configure(textvariable=set_point_support.pot)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.4, rely=0.286, height=21, width=119
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#2d3436")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Potenciometro''')
        self.Label1.configure(width=119)

        self.Labelframe1_1 = LabelFrame(top)
        self.Labelframe1_1.place(relx=0.036, rely=0.294, relheight=0.178
                , relwidth=0.912)
        self.Labelframe1_1.configure(relief=GROOVE)
        self.Labelframe1_1.configure(foreground="#ffffff")
        self.Labelframe1_1.configure(text='''Voltajes''')
        self.Labelframe1_1.configure(background="#2d3436")
        self.Labelframe1_1.configure(width=500)

        self.V_in_min = Entry(self.Labelframe1_1)
        self.V_in_min.place(relx=0.46, rely=0.588, height=23, relwidth=0.172
                , bordermode='ignore')
        self.V_in_min.configure(background="white")
        self.V_in_min.configure(font="TkFixedFont")
        self.V_in_min.configure(selectbackground="#c4c4c4")
        self.V_in_min.configure(textvariable=set_point_support.v_out_min)

        self.V_sat = Entry(self.Labelframe1_1)
        self.V_sat.place(relx=0.2, rely=0.588, height=23, relwidth=0.172
                , bordermode='ignore')
        self.V_sat.configure(background="white")
        self.V_sat.configure(font="TkFixedFont")
        self.V_sat.configure(selectbackground="#c4c4c4")
        self.V_sat.configure(textvariable=set_point_support.v_in)

        self.V_in_max = Entry(self.Labelframe1_1)
        self.V_in_max.place(relx=0.68, rely=0.588, height=23, relwidth=0.172
                , bordermode='ignore')
        self.V_in_max.configure(background="white")
        self.V_in_max.configure(font="TkFixedFont")
        self.V_in_max.configure(selectbackground="#c4c4c4")
        self.V_in_max.configure(textvariable=set_point_support.v_out_max)
        self.V_in_max.configure(width=86)

        self.Label2 = Label(self.Labelframe1_1)
        self.Label2.place(relx=0.26, rely=0.235, height=21, width=25
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(background="#2d3436")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Vin''')

        self.Label3 = Label(self.Labelframe1_1)
        self.Label3.place(relx=0.42, rely=0.235, height=21, width=229
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(background="#2d3436")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Rango de operacion (min - max)''')

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

        #----------------------------EDITED-----------------------------------------------
        self.Calculate = Button(top, command=lambda:calculate(self,
                                                                   set_point_support.pot.get(),
                                                                   set_point_support.v_in.get(),
                                                                   set_point_support.v_out_min.get(),
                                                                   set_point_support.v_out_max.get()
                                                                   ))

        #----------------------------EDITED-------------------------------------------------
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



