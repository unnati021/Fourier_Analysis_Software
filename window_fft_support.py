#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 16, 2018 01:14:50 PM


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
def set_Tk_var():
    global che46
    che46 = StringVar()
    global che47
    che47 = StringVar()
    global che48
    che48 = StringVar()
    global che49
    che49 = StringVar()
    global che50
    che50 = StringVar()
    global che52
    che52 = StringVar()
    global che61
    che61 = StringVar()
    global che62
    che62 = StringVar()
    global che65
    che65 = StringVar()
    global che67
    che67 = StringVar()
    global che66
    che66 = StringVar()
    global che68
    che68 = StringVar()
    global che69
    che69 = StringVar()
    global che70
    che70 = StringVar()

    global che71
    che71 = StringVar()
    global che72
    che72 = StringVar()
    global che73
    che73 = StringVar()
    global che74
    che74 = StringVar()
    global che75
    che75 = StringVar()
    global che76
    che76 = StringVar()
    global che77
    che77 = StringVar()
    global che78
    che78 = StringVar()
    global che79
    che79 = StringVar()
    global che80
    che80 = StringVar()
    global che81
    che81 = StringVar()
    global che82
    che82 = StringVar()
    global che83
    che83 = StringVar()
    






def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import window_fft
    window_fft.vp_start_gui()

