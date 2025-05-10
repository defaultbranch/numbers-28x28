from mnist_dataloader import MnistDataloader
from os import path

def main():

    input_path = 'mnist'
    training_images_filepath = path.join(input_path, 'train-images.idx3-ubyte')
    training_labels_filepath = path.join(input_path, 'train-labels.idx1-ubyte')
    test_images_filepath = path.join(input_path, 't10k-images.idx3-ubyte')
    test_labels_filepath = path.join(input_path, 't10k-labels.idx1-ubyte')

    mnist_dataloader = MnistDataloader(training_images_filepath, training_labels_filepath, test_images_filepath, test_labels_filepath)
    (x_train, y_train), (x_test, y_test) = mnist_dataloader.load_data()

if __name__ == "__main__":
    main()
