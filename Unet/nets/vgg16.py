from tensorflow.keras import layers
from tensorflow.keras.initializers import RandomNormal

def VGG16(img_imput):
    # 512,512,3 -> 512,512,64
    x = layers.Conv2D(64,(3,3),
                      activation='relu',
                      padding='same',
                      kernel_initializer=RandomNormal(stddev=0.02),
                      name='block_conv1')(img_imput)
    x = layers.Conv2D()
    feat1 = x
    # 512,512,64 -> 256,256,64
    x = layers.MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)

    # 256,256,64 -> 256,256,128
    x = layers.Conv2D(128, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block2_conv1')(x)
    x = layers.Conv2D(128, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block2_conv2')(x)
    feat2 = x
    # 256,256,128 -> 128,128,128
    x = layers.MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(x)

    # 128,128,128 -> 128,128,256
    x = layers.Conv2D(256, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block3_conv1')(x)
    x = layers.Conv2D(256, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block3_conv2')(x)
    x = layers.Conv2D(256, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block3_conv3')(x)
    feat3 = x
    # 128,128,256 -> 64,64,256
    x = layers.MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(x)

    # 64,64,256 -> 64,64,512
    x = layers.Conv2D(512, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block4_conv1')(x)
    x = layers.Conv2D(512, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block4_conv2')(x)
    x = layers.Conv2D(512, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block4_conv3')(x)
    feat4 = x
    # 64,64,512 -> 32,32,512
    x = layers.MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(x)

    # 32,32,512 -> 32,32,512
    x = layers.Conv2D(512, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block5_conv1')(x)
    x = layers.Conv2D(512, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block5_conv2')(x)
    x = layers.Conv2D(512, (3, 3),
                      activation='relu',
                      padding='same',
                      kernel_initializer = RandomNormal(stddev=0.02), 
                      name='block5_conv3')(x)
    feat5 = x
    return feat1, feat2, feat3, feat4, feat5