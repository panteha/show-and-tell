# showNtell

- Dom McDonnell   [@dmcd84](https://github.com/dmcd84)
- Lubos Michalic  [@lubosmichalic](https://github.com/lubosmichalic)
- Panteha Ahmadi  [@panteha](http://github.com/panteha)
- Alex Satur      [@alexanders89](http://github.com/alexanders89)

## What it does

A web app to detect objects within an image. It displays and reads back the contents to the user.

- Next step: Create an app to aid visually impaired users to receive an audio description of what is in front of the camera.

## Prerequisites/Requirements

Python 2.7.9+

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
A typical user can install Tensorflow using one of the following commands:
```bash
$ pip install tensorflow
```
## Installation

```bash
# Clone this repository
$ git clone git@github.com:lubosmichalic/showNtell.git
$ git submodule init
$ git submodule update

# Go into the repository
$ cd showNtell

# Install dependencies
$ pip install tenserflow
$ pip install virtualenv

# Run the app
$ export FLASK_APP=app.py
$ flask run
```
