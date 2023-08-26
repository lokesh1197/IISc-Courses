import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from numpy.linalg import svd, norm

# (a)
# load image
# find svg
# make image with low rank svg
class ProcessImage:
    def __init__(self, file):
        self.img = np.array(Image.open(file), dtype='uint')
        self.red = svd(self.img.transpose()[0], False)
        self.green = svd(self.img.transpose()[2], False)
        self.blue = svd(self.img.transpose()[1], False)

    def compress(self, r):
        self.r = r;
        self.red_reduced = np.delete(
            self.red[0],
            slice(r-1, -1),
            axis=1
        ).dot(np.diag(self.red[1][0:r]).dot(self.red[2][0:r]))
        self.green_reduced = np.delete(
            self.green[0],
            slice(r-1, -1),
            axis=1
        ).dot(np.diag(self.green[1][0:r]).dot(self.green[2][0:r]))
        self.blue_reduced = np.delete(
            self.blue[0],
            slice(r-1, -1),
            axis=1
        ).dot(np.diag(self.blue[1][0:r]).dot(self.blue[2][0:r]))

        self.img_reduced = np.array(
            [self.red_reduced, self.green_reduced, self.blue_reduced],
            dtype='uint'
        ).transpose()
        return self

    def compare(self):
        fig, (ax1, ax2) = plt.subplots(1,2)
        ax1.imshow(self.img)
        ax2.imshow(self.img_reduced)
        plt.show()
        return self

    def error(self):
        l2_norm_red = norm(np.subtract(self.red, self.red_reduced), 2)
        l2_norm_green = norm(np.subtract(self.green, self.green_reduced), 2)
        l2_norm_blue = norm(np.subtract(self.blue, self.blue_reduced), 2)
        fro_norm_red = norm(np.subtract(self.red, self.red_reduced))
        fro_norm_green = norm(np.subtract(self.green, self.green_reduced))
        fro_norm_blue = norm(np.subtract(self.blue, self.blue_reduced))

        l2_red = self.red[1][self.r+1]
        l2_green = self.green[1][self.r+1]
        l2_blue = self.blue[1][self.r+1]

        fro_red = norm(self.red[1][self.r+1:])
        fro_green = norm(self.green[1][self.r+1:])
        fro_blue = norm(self.blue[1][self.r+1:])

        return [
            [l2_norm_red, l2_norm_green, l2_norm_blue],
            [fro_norm_red, fro_norm_green, fro_norm_blue],
            [l2_red, l2_green, l2_blue],
            [fro_red, fro_green, fro_blue],
        ]

# ProcessImage("Webb’s_First_Deep_Field.png").compress(80).compare()
compressed = ProcessImage("Webb’s_First_Deep_Field.png")
compressed.compress(80).compare()
print(compressed.error())

# (b)
# find the number of entries to send
# 80

# (c)
# L2 norm and frobenius norm error of the reduced matrix
# check if they satisfy the mentioned equations
