HippoGIF
========

Python package that provides very simple command-line interface for conversion
of video files to animated GIFs using MoviePy.

Usage
=====

Installation
------------

Download the source and run `python3 setup.py install`.

Requirements
------------

* moviepy

Basic Usage
-----------

In Python:

```python
>>> from hippogif import video_to_gif
>>> video_to_gif('video.mkv', start=10, end=15, scale=0.5, fps=12)
```

Here's the relevant function declaration:

```python
video_to_gif(input_file, output_file=None, start=0, end=None, scale=1, crop=None, fps=None)
```

From the console:

```bash
$ hippogif video.mkv -s 10 -e 15 -r 0.5 -f 12
```

You can view the available flags by passing `-h`.

### Seeking/Trimming Clips

The start and endpoint of the video clip you'd like to turn into a GIF can be
specified with the `-s` and `-e` options, respectively. Passing `-s 70 -e 75`
will create a 5-second GIF that starts at the 70 second mark in the video and
ends at the 1 minute, 15 second mark. The `-e` option also accepts a negative
value: `-e -10` indicates that the endpoint of the GIF should end ten seconds
prior to the end of the video.

The framerate of the clip can be modified with the `-f` option.

### Output File

By default, `hippogif` will write the resulting GIF to a file with the same name
as the video file, but with the extension replaced with `.gif`. You can specify
a different name with the `-o` option.

### Output Dimensions

By default, the output GIF will be the same dimensions/resolution as the input
file. In many cases, this will mean a very large file size.

The output can be scaled down with the `-s` flag, which takes a scaling factor
between zero and one. The output can also be cropped using the `--left`,
`--right`, `--top`, and `--bottom` options, each of which specify a number of
pixels to remove from one side of the image.

Note that cropping happens **after** scaling, which means that a 100x100 video
file scaled by a factor of 0.5 with 10 pixels cropped from the bottom will
result in a 50x40 GIF.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Add support for overlaying text on the image

Known Bugs
----------

None

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).

