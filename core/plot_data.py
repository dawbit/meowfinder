import matplotlib.pyplot as plt
import numpy as np
import neural_network1


#-------IMPORTOWANIE TEGO NIE DZIALA, HGW--------#
from neural_network1 import test_data


TRAIN_DIR = 'train'
TEST_DIR = 'test'
IMG_SIZE = 125
LR = 1e-3
MODEL_NAME = 'meowfinder-{}-{}'.format(LR, 'basic')


#-------IMPORTOWANIE TEGO NIE DZIALA, HGW--------#


def plt_dat():
    model = neural_network1.network1.model
    d = test_data[0]
    img_data, img_num = d

    data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
    prediction = model.predict([data])[0]


    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.imshow(img_data, cmap="gray")
    print(f"cat: {prediction[0]}, dog: {prediction[1]}")

    fig = plt.figure(figsize=(16, 12))

    for num, data in enumerate(test_data[:16]):

        img_num = data[1]
        img_data = data[0]

        y = fig.add_subplot(4, 4, num + 1)
        orig = img_data
        data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
        model_out = model.predict([data])[0]

        if np.argmax(model_out) == 1:
            str_label = 'Dog'
        else:
            str_label = 'Cat'

        y.imshow(orig, cmap='gray')
        plt.title(str_label)
        y.axes.get_xaxis().set_visible(False)
        y.axes.get_yaxis().set_visible(False)
    plt.show()