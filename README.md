# Source for http://mmngreco.github.io

This repository contains the source for http://mmngreco.github.io/.

## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/mmngreco/mmngreco.github.io.git
$ git submodule update --init --recursive
```

Install the required packages:

```
$ conda env create -f environment.yml
$ conda activate mmngreco36
(mmngreco36) $ npm install -g less
```

Build the html and serve locally:

```
$ make html && make serve
$ open http://localhost:8000
```

Deploy to github pages

```
$ make publish-to-github
```
