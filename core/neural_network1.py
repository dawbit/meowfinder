import numpy as np
import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import settings as s


tf.reset_default_graph()
print(tf.test.gpu_device_name())

# def get_data(train_data, test_data):
#    train = train_data[:-25000]
#    test = test_data[-12500:]
#    return train, test


def network1(train, test, train_amount):
    train_amount = int(train_amount*2/3)
    global model
    tflearn.init_graph(num_cores=12, gpu_memory_fraction=1, soft_placement=True)

    X_train = np.array([i[0] for i in train[:train_amount]]).reshape(-1, s.IMG_SIZE, s.IMG_SIZE, 1)  #oryginalna wersja#
    #X_train = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE)#
    y_train = [i[1] for i in train[:train_amount]]

    # validation_set (y_test powinno byc wymiaru 2D)
    # X_test = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)#oryginalna wersja#
    X_validation = np.array([i[0] for i in train[train_amount:]]).reshape(-1, s.IMG_SIZE, s.IMG_SIZE, 1)#oryginalna wersja#
    #X_test = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE)#
    y_validation = [i[1] for i in train[train_amount:]]

    tf.reset_default_graph()

    convnet = input_data(shape=[None, s.IMG_SIZE, s.IMG_SIZE, 1], name='input')

    convnet = conv_2d(convnet, 32, 5, activation='relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 64, 5, activation='relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = fully_connected(convnet, 1024, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 2, activation='softmax')
    convnet = regression(convnet, optimizer='adam', learning_rate=s.LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet, tensorboard_dir='log', tensorboard_verbose=0)

    # model.fit({'input': X_train}, {'targets': y_train}, n_epoch=10,
    #           validation_set=({'input': X_test}, {'targets': y_test}),
    #          snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
    model.fit({'input': X_train}, {'targets': y_train}, n_epoch=10,
              validation_set=({'input': X_validation}, {'targets': y_validation}),
              snapshot_step=500, show_metric=True, run_id=s.MODEL_NAME)

    tf.reset_default_graph()

    convnet = input_data(shape=[None, s.IMG_SIZE, s.IMG_SIZE, 1], name='input')

    convnet = conv_2d(convnet, 32, 5, activation='relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 64, 5, activation='relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 128, 5, activation='relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 64, 5, activation='relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 32, 5, activation='relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = fully_connected(convnet, 1024, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 2, activation='softmax')
    convnet = regression(convnet, optimizer='adam', learning_rate=s.LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet, tensorboard_dir='log', tensorboard_verbose=0)

    # model.fit({'input': X_train}, {'targets': y_train}, n_epoch=10,
    #           validation_set=({'input': X_test}, {'targets': y_test}),
    #           snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

    model.fit({'input': X_train}, {'targets': y_train}, n_epoch=10,
              validation_set=({'input': X_validation}, {'targets': y_validation}),
              snapshot_step=500, show_metric=True, run_id=s.MODEL_NAME)

    #------ tej linijki na dole nie miales w pliku, ale byla w notatniku z jupitera------#
    model.save(s.MODEL_NAME)

    return model