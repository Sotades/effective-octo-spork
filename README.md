# effective-octo-spork
Pipe and Filter Design Pattern implementation

This is the implementation of the Pipe and Filter Design Pattern as described by rauchc at https://tech.stylight.com/pipes-and-filters-architectures-with-python-generators/

The architecture uses iterators and generators; it is lighting fast with a very small footprint.

## Required Packages
numpy
opencv_python
tubo

All available within the Pycharm environment.

## Instructions
Run image_processing_pipeline.py. It will create a pipeline that does the following:
1. Read the image from a file and convert it into an image
2. Convert image to grey scale
3. Decrease resolution by 50%

Finally, the output of the pipeline is saved to a file in the output_files directory

## Pipe and Filter Architecture and Rationale:
[Pipes and Filters](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html)

[Pipes and filters architectures with Python generators (and other iterators)](https://tech.stylight.com/pipes-and-filters-architectures-with-python-generators/)

[Tubo is a library that provides a simple pipeline system for Python](https://pypi.org/project/tubo/)

## Adding Processing steps ('Filters')
1. Create a new python file.
2. Define your filter in it, passing in the data stream (see any existing files in the project).
3. Add the reference to the file and function in the image_processing_pipeline.py file
4. Add the function to the pipeline.
