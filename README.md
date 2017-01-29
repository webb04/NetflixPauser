Built using https://github.com/Hironsan/BossSensor

## Requirements

* WebCamera
* Python3.5
* OSX
* Anaconda
* Lots of images of your boss and other person image

Put images into [data/boss] and [data/other].

## Install
Install OpenCV, PyQt4, Anaconda.

```
conda create -n venv python=3.5
source activate venv
conda install -c https://conda.anaconda.org/menpo opencv3
conda install -c conda-forge tensorflow
pip install -r requirements.txt
```

## Usage
First, Train user image.

```
$ python boss_train.py
```


Second, start NetflixPauser.

```
$ python camera_reader.py
```
