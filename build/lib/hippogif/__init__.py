#!/usr/bin/env python3

# Written by Gem Newman, but this is a trivial remix of Zulko's work:
# http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/
# This program is licensed under the MPL2 License.


from os.path import splitext
from argparse import ArgumentParser, ArgumentTypeError
from moviepy.editor import VideoFileClip


DEFAULT_SCALE = 1


def video_to_gif(
    input_file, output_file=None, start=0, end=None, scale=DEFAULT_SCALE,
    crop=None, fps=None
):
    if output_file is None:
        output_file = splitext(input_file)[0] + ".gif"

    clip = VideoFileClip(input_file).subclip(start, end).resize(scale)

    if crop:
        clip = clip.crop(**crop)

    clip.write_gif(output_file, fps=fps)


def natural(value):
    value = int(value)
    if value <= 0:
        raise ArgumentTypeError(
            "{} is not a valid positive integer".format(value)
        )
    return value


def whole(value):
    value = int(value)
    if value < 0:
        raise ArgumentTypeError(
            "{} is not a valid non-negative integer".format(value)
        )
    return value


def zero_to_one(value):
    value = float(value)
    if value < 0 or value > 1:
        raise ArgumentTypeError(
            "{} is not a valid float between 0 and 1".format(value)
        )
    return value


def main():
    parser = ArgumentParser(
        description='Converts video files to animated GIFs.'
    )
    parser.add_argument('input', help='The filename of the video to convert.')
    parser.add_argument(
        '-o', '--output', help='The filename of the GIF to write. Defaults to '
        'the input file name with a .gif extension.', default=None
    )
    parser.add_argument(
        '-s', '--start', help='The timestamp (in seconds) at which to begin '
        'the clip. Defaults to 0.', type=float, default=0
    )
    parser.add_argument(
        '-e', '--end', help='The timestamp (in seconds) at which to end the '
        'clip. Defaults to the length of the video.', type=float, default=None
    )
    parser.add_argument(
        '-r', '--resize', help='The factor by which to scale the output (0 to '
        '1). Defaults to {}.'.format(DEFAULT_SCALE), type=zero_to_one,
        default=DEFAULT_SCALE
    )
    parser.add_argument(
        '-f', '--fps', help='The framerate of the output GIF. Defaults to the '
        'video\'s framerate.', type=natural, default=None
    )
    parser.add_argument(
        '-x1', '--left', help='Pixels to crop from the left.', type=whole,
        default=None
    )
    parser.add_argument(
        '-x2', '--right', help='Pixels to crop from the right.', type=whole,
        default=None
    )
    parser.add_argument(
        '-y1', '--top', help='Pixels to crop from the top.', type=whole,
        default=None
    )
    parser.add_argument(
        '-y2', '--bottom', help='Pixels to crop from the bottom.', type=whole,
        default=None
    )
    args = parser.parse_args()

    crop = None
    if any(x for x in (args.left, args.right, args.top, args.bottom)):
        crop = {
            'x1': args.left, 'x2': -args.right if args.right else None,
            'y1': args.top, 'y2': -args.bottom if args.bottom else None
        }

    video_to_gif(
        args.input, args.output, args.start,
        args.end, args.resize, crop, args.fps
    )


if __name__ == '__main__':
    main()
