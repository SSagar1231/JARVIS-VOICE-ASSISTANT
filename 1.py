from PIL import Image
import requests
import matplotlib.pyplot as plt
import urllib3

response = requests.get(urllib3, stream=True)
img = Image.open(response.raw)

plt.imshow(img)
plt.show()