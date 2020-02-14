#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from subprocess import call
import subprocess
import subprocess as sub
import webbrowser

call('sudo apt-get install speedtest-cli', shell=True)
call('sudo apt-get install python3', shell=True)
call('sudo apt-get install python3-tk', shell=True)


def inicio1():

	botonBienvenido=Frame(v_home)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=405, y=70)
	Button(botonBienvenido, image=rayo_logo, cursor="heart", justify="center", bd=0,
	highlightbackground="black",
    background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


	boton_offshell_menu3=Frame(v_home)
	boton_offshell_menu3.pack(fill=BOTH, expand=YES)
	boton_offshell_menu3.place(x=297, y=10)
	Button(boton_offshell_menu3, highlightbackground="black", command=lambda:[], 
		text="Controlador de Velocidad de Bajada/Subida",   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 23)).pack()


	boton_empezar=Frame(v_home)
	boton_empezar.pack(fill=BOTH, expand=YES)
	boton_empezar.place(x=475, y=380)
	Button(boton_empezar, highlightbackground="black", command=lambda:[procesador(), boton_empezar.destroy(),
		botonBienvenido.destroy()], 
		image=go_boton,   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 23)).pack()

	pass



def procesador():


	p = sub.Popen(["speedtest-cli"],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	
	text = tk.Text(v_home, width=75, height=11, highlightbackground="black", background="black", 
		foreground='orange', bd=0, font=("URW Chancery L", 16))

	text.pack()
	text.place(x=300, y=150)
	text.insert(tk.END, output)


	boton_repetir=Frame(v_home, width=50, height=100)
	boton_repetir.place(x=700, y=410)
	Button(boton_repetir, 
		command=lambda:[procesador(), text.destroy(), botonVolver.destroy(), boton_repetir.destroy(), 
		boton_img1.destroy()], 
		highlightbackground="red", text="Repetir Análisis", cursor="heart", justify="center", 
		bd=0, relief="raised", overrelief="sunken", background="black", activebackground='black', 
		activeforeground='Red', foreground='darkred', font=("URW Chancery L", 20)).pack()

	boton_img1=Frame(v_home)
	boton_img1.pack(fill=BOTH, expand=YES)
	boton_img1.place(x=10, y=150)
	Button(boton_img1, image=nube_logo, cursor="heart", justify="center", bd=0,
	highlightbackground="black",
    background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


	botonVolver=Frame(v_home, width=50, height=100)
	botonVolver.place(x=890, y=410)
	Button(botonVolver, command=lambda:[inicio1(), text.destroy(), botonVolver.destroy(), 
		boton_repetir.destroy(), boton_img1.destroy()], 
		highlightbackground="red", text="Cerrar", cursor="heart", justify="center", bd=0, relief="raised", 
		overrelief="sunken", background="black", activebackground='black', 
		activeforeground='Red', foreground='darkred', font=("URW Chancery L", 20)).pack()


	pass




v_home = Tk()


v_home.title("OffShell System Community Software")
v_home.geometry("1124x650+75+50")
v_home.resizable(width=False, height=False)
v_home.config(bg="black", bd=0)
v_home.tk.call('wm', 'iconphoto', v_home._w, tk.PhotoImage(file='primate.gif'))

#Definición Imágenes:
fondo_circulo=PhotoImage(file="red_circle.gif")
primate_logo=PhotoImage(file="primate.gif")
debian_fondo=PhotoImage(file=("debian_fondo.gif"))
meco_logo=PhotoImage(file=("meco.gif"))
go_boton=PhotoImage(file=("go.gif"))
rayo_logo=PhotoImage(file=("rayo.gif"))
nube_logo=PhotoImage(file=("nube.gif"))
aokla_logo=PhotoImage(file=("aokla.gif"))
off_logo=PhotoImage(file=("off_logo.gif"))



botonBienvenido=Frame(v_home)
botonBienvenido.pack(fill=BOTH, expand=YES)
botonBienvenido.place(x=405, y=70)
Button(botonBienvenido, image=rayo_logo, cursor="heart", justify="center", bd=0,
	highlightbackground="black",
    background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()


boton_offshell_menu3=Frame(v_home)
boton_offshell_menu3.pack(fill=BOTH, expand=YES)
boton_offshell_menu3.place(x=297, y=10)
Button(boton_offshell_menu3, highlightbackground="black", command=lambda:[], 
		text="Controlador de Velocidad de Bajada/Subida",   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 23)).pack()


boton_empezar=Frame(v_home)
boton_empezar.pack(fill=BOTH, expand=YES)
boton_empezar.place(x=472, y=370)
Button(boton_empezar, highlightbackground="black", command=lambda:[procesador(), boton_empezar.destroy(),
	botonBienvenido.destroy()], 
		image=go_boton,   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 23)).pack()


boton_powered=Frame(v_home)
boton_powered.pack(fill=BOTH, expand=YES)
boton_powered.place(x=123, y=490)
Button(boton_powered, highlightbackground="black", 
		command=lambda:[webbrowser.open_new_tab("https://www.speedtest.net/es/about")], 
		text="Powered by\nSpeedTest.net",   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

boton_aokla=Frame(v_home)
boton_aokla.pack(fill=BOTH, expand=YES)
boton_aokla.place(x=130, y=550)
Button(boton_aokla, highlightbackground="black", 
		command=lambda:[webbrowser.open_new_tab("https://www.speedtest.net/es/about")], 
		image=aokla_logo,   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 23)).pack()


boton_off=Frame(v_home)
boton_off.pack(fill=BOTH, expand=YES)
boton_off.place(x=830, y=470)
Button(boton_off, highlightbackground="black", 
		command=lambda:[webbrowser.open_new_tab("https://www.offshellsystem.tk/p/offshell-system.html")], 
		text="Software\nOffShell System",   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 14)).pack()

boton_offlogo=Frame(v_home)
boton_offlogo.pack(fill=BOTH, expand=YES)
boton_offlogo.place(x=845, y=530)
Button(boton_offlogo, highlightbackground="black", 
		command=lambda:[webbrowser.open_new_tab("https://www.offshellsystem.tk/p/offshell-system.html")], 
		image=off_logo,   
        foreground='red', activeforeground='red',cursor="heart", bd=0,
        justify="center", relief="groove", background="black", activebackground="black", 
        font=("URW Chancery L", 23)).pack()




v_home.mainloop()