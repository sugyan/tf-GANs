import tensorflow as tf

from models import DCGAN, LSGAN


def main(argv=None):
    dcgan = DCGAN()
    lsgan = LSGAN()
    print(dcgan, lsgan)


if __name__ == '__main__':
    tf.app.run()
