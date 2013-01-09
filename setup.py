#!/usr/bin/env python3
from distutils.core import setup

setup(name="mplayer-autocmd",
      version="1",
      author="Wieland Hoffmann",
      author_email="themineo@gmail.com",
      description="mplayer wrapper providing per-file options & keybinding",
      long_description=open("README.rst").read(),
      scripts=["automp"],
      download_url=["https://github.com/mineo/mplayer-autocmd/tarball/master"],
      url=["http://github.com/mineo/mplayer-autocmd"],
      license="MIT",
      classifiers=[
      "Environment :: Console",
      "License :: OSI Approved :: MIT License",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Programming Language :: Python :: 3.3"],
      data_files=[("share/zsh/site-functions", ["_automp"])],
      )
