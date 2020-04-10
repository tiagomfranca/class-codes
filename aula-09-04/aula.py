import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


st.title('Aula do dia 09/04')


image = Image.open('monte_fuji.jpg')

imagem_color_arr = np.array(image)

img_gray = np.mean(imagem_color_arr, axis=2)

st.text(img_gray.shape)

tons = st.slider('Tons', 1, 25, 4)

st.text(tons)

img_gray = np.mean(imagem_color_arr, axis=2)

incremento = int(255/tons)
limite_inferior = 0
limite_superior = incremento

for parte in range(0, int(255/tons)):
    img_gray[np.logical_and(limite_inferior < img_gray, img_gray < limite_superior)]  = limite_inferior
    limite_inferior = limite_superior
    limite_superior += incremento

#img_gray[np.logical_and(0 < img_gray, img_gray < 64)]  = 0
#img_gray[np.logical_and(64 < img_gray, img_gray < 128)]  = 64
#img_gray[np.logical_and(128 < img_gray, img_gray < 192)]  = 128
#img_gray[img_gray > 192]  = 192

new_image = Image.fromarray(img_gray)

plt.axis('off')
plt.imshow(new_image)
plt.show()
st.pyplot()

# new_image = Image.fromarray(imagem_color_arr)

# st.image(new_image, caption='Sunrise by the mountains', use_column_width=True)