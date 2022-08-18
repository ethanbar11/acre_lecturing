import scipy.signal
import numpy as np
import cv2


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


if __name__ == '__main__':
    kernel_size = 1
    kernel = ((1 / (kernel_size ** 2)) * np.ones(kernel_size ** 2))
    kernel = kernel.reshape(kernel_size, kernel_size)

    # Reading the image.
    path = 'jack_nicholson.jpg'
    img = cv2.imread(path)
    img_gray = rgb2gray(img)

    # Writing grayscale to new image.
    cv2.imwrite('jack_nicholson_gray.png', img_gray)

    # Convolution
    output = scipy.signal.convolve2d(img_gray, kernel)

    cv2.imwrite('output.png', output)
