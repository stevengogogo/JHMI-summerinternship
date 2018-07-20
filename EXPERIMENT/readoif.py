# Read oif files. Use oiffile.py
# oiffile.py from https://www.lfd.uci.edu/~gohlke/code/oiffile.py.html
#%% READ IMAGE
import oiffile as oif
import matplotlib.pyplot as plt

img = oif.imread("mitochr2/B 1040nm 9%.oif")

#%% PRINT IMAGE SIZE
print(img.shape)

#%% PLOT IMAGE
plt.figure()
for i in range(0,img.shape[0]):
    plt.imshow(img[i,:,:])
plt.show()

#%%
with oif.OifFile('mitochr2/chr transfected 940nm 3% A4 scanned 2sec at 25%.oif') as oif:
    image = oif.asarray()
image

#%%
image.shape
