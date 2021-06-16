import os
import shutil
import time

ruta_descargas = 'tu ruta'
temporizador = 30

ext_vid = ['.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv']
ext_aud = ['.mp3', '.wma', '.wav', '.flac']
ext_img = ['.jpg', '.png', 'jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg']
ext_doc = ['.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf']
ext_com = ['.zip', '.rar', '.rar5', '.7z', '.ace', '.gz']
ext_ins = ['.exe', '.msi']

def motor(archivo, ext):
    for i in ext_doc:
        if ext == i:
            shutil.move(ruta_descargas + archivo + i, ruta_descargas + 'Documentos')

    for i in ext_aud:
        if ext == i:
            shutil.move(ruta_descargas + archivo + i, ruta_descargas + 'Audio')
    
    for i in ext_img:
        if ext == i:
            shutil.move(ruta_descargas + archivo + i, ruta_descargas + 'Imagenes')

    for i in ext_doc:
        if ext == i:
            shutil.move(ruta_descargas + archivo + i, ruta_descargas + 'Documentos')

    for i in ext_ins:
        if ext == i:
            shutil.move(ruta_descargas + archivo + i, ruta_descargas + 'Instaladores')

    for i in ext_com:
        if ext == i:
            shutil.move(ruta_descargas + archivo + i, ruta_descargas + 'Comprimidos')

    if ext != '':
        shutil.move(ruta_descargas + archivo + i, ruta_descargas + 'Otros')

def verificar():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        motor(nombre_archivo, ext)

while(True):
    try:
        time.sleep(temporizador)
        for _ in range(len(os.listdir(ruta_descargas))):
            try:
                verificar()
            except:
                pass
    except KeyboardInterrupt:
        break
