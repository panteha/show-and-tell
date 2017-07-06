# showNtell

Dom McDonnell [@dmcd84](https://github.com/dmcd84)
Lubos Michalic [@lubosmichalic](https://github.com/lubosmichalic)
Panteha Ahmadi [@panteha](http://github.com/panteha)
Alex Satur [@alexanders89](http://github.com/alexanders89)

## What it does

Create an app to aid visually impaired users to receive an audio description of what is in front of the camera.

## How we plan on making it work

## Prerequisites

Python 2.7.9+


## Requirements
### TensorFlow Object Detention API
Tensorflow Object Detection API depends on the following libraries:

* Protobuf 2.6
* Pillow 1.0
* lxml
* tf Slim (which is included in the "tensorflow/models" checkout)
* Jupyter notebook
* Matplotlib
* Tensorflow

For detailed steps to install Tensorflow, follow the
[Tensorflow installation instructions](https://www.tensorflow.org/install/).
A typically user can install Tensorflow using one of the following commands:
```bash
$ pip install tensorflow
```
## Installation

```bash
# Clone this repository
$ git clone git@github.com:lubosmichalic/showNtell.git

# Go into the repository
$ cd showNtell

# Install dependencies
$ pip install tenserflow
$ pip install virtualenv

# Run the app
$ export FLASK_APP=app.py
$ flask run
```




### Technologies

TensorFlow  
