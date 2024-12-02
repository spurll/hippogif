#!/usr/bin/env python3


from setuptools import setup


setup(
    name='hippogif',
    packages=['hippogif'],
    version='0.2',
    description='Conversion of video files to GIF animations.',
    url='https://github.com/spurll/hippogif',
    download_url='https://github.com/spurll/hippogif/tarball/0.2',
    author='Gem Newman',
    author_email='spurll@gmail.com',
    license='MPL2',
    install_requires=['moviepy'],
    entry_points = {'console_scripts': ['hippogif = hippogif:main']},
    keywords=['movie', 'video', 'image', 'gif'],
    classifiers=[
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Programming Language :: Python',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)'
    ],
)

