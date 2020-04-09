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

limiar = st.slider('Limiar?', 0, 255, 25)

st.text(limiar)

img_gray = np.mean(imagem_color_arr, axis=2)

# img_gray[img_gray != limiar] = 255
img_gray[0 < img_gray and img_gray < 64]  = 0
img_gray[64 < img_gray and img_gray < 128]  = 64
img_gray[128 < img_gray and img_gray < 192]  = 128
img_gray[img_gray > 192]  = 192
# img_gray[img_gray < limiar] = 191
# img_gray[img_gray > limiar] = 127
# img_gray[img_gray > limiar] = 64
# img_gray[img_gray < limiar] = 0

new_image = Image.fromarray(img_gray)

plt.axis('off')
plt.imshow(new_image)
plt.show()
st.pyplot()

# new_image = Image.fromarray(imagem_color_arr)

# st.image(new_image, caption='Sunrise by the mountains', use_column_width=True)