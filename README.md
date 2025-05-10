# About

This project is inspired by the 3Blue1Brown "Neural networks" series <https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi>.


# Project Setup

This project uses [uv](https://docs.astral.sh/uv/) for package and project management:

- run `uv sync` to setup `.venv`
- run `source .venv/bin/activate` to activate the virtual environment


# Training Data

MNIST data is available from <https://www.kaggle.com/datasets/hojjatk/mnist-dataset?select=train-labels.idx1-ubyte>:

- `train-images.idx3-ubyte`: training set images
- `train-labels.idx1-ubyte`: training set labels
- `t10k-images.idx3-ubyte`: test set images
- `t10k-labels.idx1-ubyte`: test set labels

Training data is expected in a folder `mnist/`, which is not part of the git repo:

```
$ tree .
.
├── README.md
├── LICENSE
├── pyproject.toml
├── uv.lock
├── src
│   └── ...
└── mnist
    ├── t10k-images.idx3-ubyte
    ├── t10k-labels.idx1-ubyte
    ├── train-images.idx3-ubyte
    └── train-labels.idx1-ubyte
```


# Execution

Given valid data in `mnist/`, run:
```
python src/main.py
```
