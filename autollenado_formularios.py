from tkinter import *
from tkinter import messagebox
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("C:/Users/NICO/Desktop/git/autollenado_formulario/carga_form.html")
time.sleep(3)


#----------------------Funciones-----------------------------------

def creacionBBDD():
	miConexion=sqlite3.connect("Registro")
	miCursor= miConexion.cursor()

	miCursor.execute('''
			CREATE TABLE REGISTRO_USUARIOS (
			NOMBRE_USUARIO VARCHAR (50),
			APELLIDO_USUARIO VARCHAR(10),
			EMAIL_USUARIO VARCHAR(50),
			TELEFONO_USUARIO INTEGER )

		''')
		

def cargar_registro():
	
	miConexion=sqlite3.connect("Registro")
	miCursor=miConexion.cursor()

	datos=nombre, apellido, email, telefono
	miCursor.execute("INSERT INTO REGISTRO_USUARIOS VALUES(?,?,?,?)", (datos))
	miConexion.commit()
		
#---------------Creación de BDD sólo para la prueba automatizada----------------------

bbdd= creacionBBDD()

#---------------Inicio del ciclo de auto llenado--------------------------------------


with open('data.txt') as file:
	 for i, line in enumerate(file):
	 		usuario = (line)
	 		sep = ","
	 		dividir = usuario.split(sep)
	 		try:
	 			gotdata = dividir[3]
	 			nombre = dividir[0]
	 			apellido = dividir[1]
	 			email = dividir[2]
	 			telefono = dividir[3]
	 		except IndexError:
	 			gotdata = 'null'
	 		
	 		
	 		driver.find_element_by_id("nomb").send_keys(nombre)
	 		time.sleep(2)
	 		driver.find_element_by_id("ape").send_keys(apellido)
	 		time.sleep(2)
	 		driver.find_element_by_id("mail").send_keys(email)
	 		time.sleep(2)
	 		driver.find_element_by_id("fono").send_keys(telefono)
	 		time.sleep(2)
	 		driver.find_element_by_id("carga").click()
	 		carga=cargar_registro()
	 		time.sleep(2)

file.close()
driver.close()