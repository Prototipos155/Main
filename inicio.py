from conexion import Conexion

cx=Conexion('irrepetible',1,'DB2.sql')
#cx=Conexion()

print(cx.detectar_Instruccion('use irrepetible'))

print(cx.detectar_Instruccion('create schema irrepetible'))