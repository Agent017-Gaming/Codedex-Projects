import os
import numpy as np
import imageio.v3 as iio
from PIL import Image

filenames = ['first.png',
    'second.png',
    'third.png',
    'forth.png',
    'fifth.png',
    'sixth.png',
    'seventh.png']

with Image.open(filenames[0]) as im:
    target_size = im.size
images = [ ]

for fname in filenames:
  with Image.open(fname) as im:
        im_resized = im.resize(target_size)  # resize to match first image
        images.append(np.array(im_resized))

images = np.array(images)

# Each frame 0.5s → fps=2
iio.imwrite("team.gif", images, fps=2, loop=0)
