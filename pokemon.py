import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

pokemon = input("Que pokemon deseas conocer: ")

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
respuesta = requests.get(url)

try:
    respuesta = requests.get(url, timeout=5)
except requests.Timeout:
    print("Error: El tiempo finalizo")

if respuesta.status_code != 200:
    print("No existe ese pokemon")
    exit()

else :
    print(respuesta)


datos = respuesta.json()
nombre = datos["name"]

print("El pokemon que seleccionaste es: " + nombre)

tipos = datos["types"]
for i in range(int(len(tipos))):
    tipo = tipos[i]["type"]["name"]
    print("El pokemon es de tipo: " + tipo)

habilidades = datos["abilities"]
for i in range(int(len(habilidades))):
    habilidad = habilidades[i]["ability"]["name"]
    print("Sus habilidades son: " + habilidad)

movimientos = datos["moves"]
for i in range(int(len(movimientos))):
    movimiento = movimientos[i]["move"]["name"]
    print("Sus movimientos son: " + movimiento)

try :
    url_imagen = datos["sprites"]["front_default"]
    imagen = Image.open(urlopen(url_imagen))
except:
    print("El pokemon no tiene imagen")
    exit()

plt.title(datos["name"])
imgplot = plt.imshow(imagen)
plt.show()

