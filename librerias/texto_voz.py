from gtts import gTTS
import os

myTexto="Curso de Python Avanzado"
lenguage="es"

#pasar el texto y el lenguaje al motor , ademas se utiliza paramtros que
#me permitiran controlar los argumentos de la librerias
#El slow reproduce el texto a alta velocidad
myobj = gTTS(text=myTexto,lang=lenguage,slow=False)

#Guardar el audio en un archivo MP3
myobj.save("cursopython.mp3")
#Reproducir el Archivo
os.system("start cursopython.mp3")
