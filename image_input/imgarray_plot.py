import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from PIL import Image
from numpy import asarray, uint8, empty
from random import randint

# CONSTANTS
UZERO = uint8(0)
U255 = uint8(255)
RED = [U255,UZERO,UZERO,U255]
GREEN = [UZERO,U255,UZERO,U255]
BLUE = [UZERO,UZERO,U255,U255]
WHITE = [U255,U255,U255,U255]
BLACK = [UZERO,UZERO,UZERO,U255]
COLORS = (RED,GREEN,BLUE)


# FUNCTIONS
# crea un array vuoto del colore desiderato
def empty_colored_img(pixel_height, pixel_width, color):
    img = empty( (pixel_height, pixel_width , 4), dtype=uint8 ) 
    for j in range(pixel_height):
        for k in range(pixel_width):
            for i in range(len(color)):
                img[j][k][i] = color[i]
    return img

# toglie la prima riga dell'array e la mette alla fine
def scroll_img(img_array):
    img = empty_colored_img(64,64,GREEN)
    for i in range(64):
        if i == 63:
            img[i] = img_array[0]
        else:
            img[i] = img_array[i+1]
    return img


###----------------acquisizione immagine-----------------###
image = Image.open('risorsepy\\image_input\\rainbow_32px.png')
dataraw = image.convert()
data = asarray(dataraw)

# crea un array vuoto BLACK per pulire l'input
img2 = empty_colored_img(64,64,BLACK)

# raddoppia la grandezza dell'immagine importata e la copia nella nera
for i32 in range(32):
    for l32 in range(32):
        if data[i32][l32][3] == UZERO:
            for i in range(4):
                img2[i32*2][l32*2][i] =img2[i32*2][l32*2+1][i] = BLACK[i]
                img2[i32*2+1][l32*2][i] = img2[i32*2+1][l32*2+1][i] = BLACK[i]    
        else: # se no copia cosi' com'e'
            for i in range(4):
                img2[i32*2][l32*2][i] = img2[i32*2][l32*2+1][i] = data[i32][l32][i]
                img2[i32*2+1][l32*2][i] = img2[i32*2+1][l32*2+1][i] = data[i32][l32][i]

#importa il serpente
image = Image.open('risorsepy\\image_input\\snake.png')
dataraw = image.convert()
img_snake = asarray(dataraw)

###------------ inizio a creare il grafico da renderizzare ---------###

# crea 2 figure con origine in comune
fig_plot, temp_plot = plt.subplots()

#crea il film senza fotogrammi
film = []
#crea un frame di colore casuale tra R G B, poi uno con l'immagine e li aggiunge
#al film come frame
random_img = empty_colored_img(64,64,COLORS[randint(0,2)])
random_frame = temp_plot.imshow(random_img, animated=True)
im = temp_plot.imshow(img2, animated=True)
film.append([im])
film .append([random_frame])

#fa cio' che ho descritto sopra per tutte le righe dell'immagine
for i in range(63):
    img2 = scroll_img(img2)
    im = temp_plot.imshow(img2, animated=True)
    random_img = empty_colored_img(64,64,COLORS[randint(0,2)])
    random_frame = temp_plot.imshow(random_img, animated=True)
    film.append([im])
    film.append([random_frame])

#randomizza 2 fotogrammi di serpente nel film
y = [temp_plot.imshow(img_snake, animated=True)]
for i in range(2):
    r = randint(0, len(film)-1)
    for j in range(2):
        film.insert(r, y)

#crea l'animazione vera e propria
animated = animation.ArtistAnimation(fig_plot, film, interval=30, blit=True,
                                repeat_delay=0)

#mostra la prodezza
print(len(film))
plt.show()