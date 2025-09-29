import imageio.v3 as iio

filenames = ['gif_final_python_project/first.png',
    'gif_final_python_project/second.png',
    'gif_final_python_project/third.png',
    'gif_final_python_project/forth.png',
    'gif_final_python_project/fifth.png',
    'gif_final_python_project/sixth.png',
    'gif_final_python_project/seventh.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)