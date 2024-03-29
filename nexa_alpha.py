#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 22, 2018 06:19:27 PM AST  platform: Linux

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

import nexa_alpha_support


#****************IMPORT OTHERS MODULES****************
import transducer
import v_to_i_converter
import set_point
import voltage_divider
import Span_and_Kp
import circuit_config
#***************IMPORT OTHERS MODULES****************

    

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = NEXA (root)
    nexa_alpha_support.init(root, top)
    root.mainloop()

w = None
def create_NEXA(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = NEXA (w)
    nexa_alpha_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_NEXA():
    global w
    w.destroy()
    w = None


class NEXA:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {DejaVu Sans} -size 8 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans} -size 48 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 8 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+389+129")
        top.title("NEXA")
        top.configure(background="#2d3436")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Label1 = Label(top)
        self.Label1.place(relx=0.133, rely=0.289, height=81, width=109)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#2d3436")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#00b894")
        self.Label1.configure(text='''NE''')

        self.Label1_1 = Label(top)
        self.Label1_1.place(relx=0.15, rely=0.444, height=71, width=99)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(background="#2d3436")
        self.Label1_1.configure(font=font11)
        self.Label1_1.configure(foreground="#bfbfbf")
        self.Label1_1.configure(highlightbackground="#d8d8d8")
        self.Label1_1.configure(text='''XA''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.15, rely=0.6, height=21, width=99)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(background="#2d3436")
        self.Label2.configure(foreground="#bfbfbf")
        self.Label2.configure(text='''UNA GRASITA''')

        self.Button_transducer = Button(top, command=lambda:transducer.vp_start_gui())
        self.Button_transducer.place(relx=0.583, rely=0.111, height=49
                , width=199)
        self.Button_transducer.configure(activebackground="#d8d8d8")
        self.Button_transducer.configure(background="#00b894")
        self.Button_transducer.configure(font=font12)
        self.Button_transducer.configure(foreground="#ffffff")
        self.Button_transducer.configure(highlightbackground="#00b894")
        self.Button_transducer.configure(overrelief="flat")
        self.Button_transducer.configure(relief=FLAT)
        self.Button_transducer.configure(text='''Transductor''')

        self.Button1_PID = Button(top, command=lambda:Span_and_Kp.vp_start_gui())
        self.Button1_PID.place(relx=0.583, rely=0.644, height=49, width=199)
        self.Button1_PID.configure(activebackground="#d9d9d9")
        self.Button1_PID.configure(background="#00b894")
        self.Button1_PID.configure(font=font12)
        self.Button1_PID.configure(foreground="#ffffff")
        self.Button1_PID.configure(highlightbackground="#00b894")
        self.Button1_PID.configure(relief=FLAT)
        self.Button1_PID.configure(state=ACTIVE)
        self.Button1_PID.configure(text='''Span Y Kp''')

        self.Button1_V_to_I = Button(top, command=lambda:v_to_i_converter.vp_start_gui())
        self.Button1_V_to_I.place(relx=0.583, rely=0.244, height=49, width=199)
        self.Button1_V_to_I.configure(activebackground="#d9d9d9")
        self.Button1_V_to_I.configure(background="#00b894")
        self.Button1_V_to_I.configure(font=font12)
        self.Button1_V_to_I.configure(foreground="#ffffff")
        self.Button1_V_to_I.configure(highlightbackground="#00b894")
        self.Button1_V_to_I.configure(relief=FLAT)
        self.Button1_V_to_I.configure(text='''Conversor de V a I''')

        self.Button1_Set_Point = Button(top, command=lambda:set_point.vp_start_gui())
        self.Button1_Set_Point.place(relx=0.583, rely=0.378, height=49
                , width=199)
        self.Button1_Set_Point.configure(activebackground="#d9d9d9")
        self.Button1_Set_Point.configure(background="#00b894")
        self.Button1_Set_Point.configure(font=font12)
        self.Button1_Set_Point.configure(foreground="#ffffff")
        self.Button1_Set_Point.configure(highlightbackground="#00b894")
        self.Button1_Set_Point.configure(relief=FLAT)
        self.Button1_Set_Point.configure(text='''Set Point''')

        self.Button1_voltage_divider = Button(top, command=lambda:voltage_divider.vp_start_gui())
        self.Button1_voltage_divider.place(relx=0.583, rely=0.511, height=49
                , width=199)
        self.Button1_voltage_divider.configure(activebackground="#d9d9d9")
        self.Button1_voltage_divider.configure(background="#00b894")
        self.Button1_voltage_divider.configure(font=font12)
        self.Button1_voltage_divider.configure(foreground="#ffffff")
        self.Button1_voltage_divider.configure(highlightbackground="#00b894")
        self.Button1_voltage_divider.configure(relief=FLAT)
        self.Button1_voltage_divider.configure(text='''Divisor de Voltaje''')

        self.Button1_configs = Button(top, command=lambda:circuit_config.vp_start_gui())
        self.Button1_configs.place(relx=0.583, rely=0.778, height=49, width=199)
        self.Button1_configs.configure(activebackground="#d9d9d9")
        self.Button1_configs.configure(background="#00b894")
        self.Button1_configs.configure(font=font12)
        self.Button1_configs.configure(foreground="#ffffff")
        self.Button1_configs.configure(highlightbackground="#00b894")
        self.Button1_configs.configure(relief=FLAT)
        self.Button1_configs.configure(state=ACTIVE)
        self.Button1_configs.configure(text='''Op Amp config''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.45, rely=0.2, relheight=0.6)
        self.TSeparator1.configure(orient="vertical")

        self.Label2_1 = Label(top)
        self.Label2_1.place(relx=0.15, rely=0.644, height=21, width=99)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(background="#2d3436")
        self.Label2_1.configure(font=font9)
        self.Label2_1.configure(foreground="#bfbfbf")
        self.Label2_1.configure(text='''Beta ver 1.01''')

        self.Label2_2 = Label(top)
        self.Label2_2.place(relx=0.308, rely=0.922, height=21, width=159)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(background="#2d3436")
        self.Label2_2.configure(font=font10)
        self.Label2_2.configure(foreground="#bfbfbf")
        self.Label2_2.configure(text='''Developed by @HanSolo''')






if __name__ == '__main__':
    vp_start_gui()



