from mnist_dataloader import MnistDataloader
from os import path
import random
import matplotlib.pyplot as plt
from typing import List
from array import array
from numpy import ndarray


def show_images(
        images: List[ndarray],
        title_texts: List[str]
        ) -> None:

    cols = 5
    rows = int(len(images)/cols) + 1
    plt.figure(figsize=(30,20))
    index = 1
    for x in zip(images, title_texts):
        image = x[0]
        title_text = x[1]
        plt.subplot(rows, cols, index)
        plt.imshow(image, cmap=plt.cm.gray)
        if (title_text != ''):
            plt.title(title_text, fontsize = 15);
        index += 1
    plt.show()


def main() -> None:

    input_path = 'mnist'
    training_images_filepath: str = path.join(input_path, 'train-images.idx3-ubyte')
    training_labels_filepath: str = path.join(input_path, 'train-labels.idx1-ubyte')
    test_images_filepath: str = path.join(input_path, 't10k-images.idx3-ubyte')
    test_labels_filepath: str = path.join(input_path, 't10k-labels.idx1-ubyte')

    mnist_dataloader: MnistDataloader = MnistDataloader(
        training_images_filepath,
        training_labels_filepath,
        test_images_filepath,
        test_labels_filepath
        )

    training_images: List[ndarray]
    training_labels: array
    training_images, training_labels = mnist_dataloader.read_images_labels(training_images_filepath, training_labels_filepath)

    test_images: List[ndarray]
    test_labels: array
    test_images, test_labels = mnist_dataloader.read_images_labels(test_images_filepath, test_labels_filepath)

    images_2_show: List[ndarray] = []
    titles_2_show: List[str] = []
    for i in range(0, 10):
        r: int = random.randint(1, 60000)
        images_2_show.append(training_images[r])
        titles_2_show.append('training image [' + str(r) + '] = ' + str(training_labels[r]))

    for i in range(0, 5):
        r: int = random.randint(1, 10000)
        images_2_show.append(test_images[r])
        titles_2_show.append('test image [' + str(r) + '] = ' + str(test_labels[r]))

    show_images(images_2_show, titles_2_show)


if __name__ == "__main__":
    main()
