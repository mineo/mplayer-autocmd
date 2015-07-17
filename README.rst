So, what does this do?

`automp` allows you to automatically append options or use different keybinding
depending on the file you're playing.
This is great if you want to skip the intro at the beginning (by providing an
`-ss xx:xx` option) without doing anything or skipping something with a known
length in the middle of the file at the press of a button(by providing a
`key=seek xx.xx` mapping)
To use it, just type `automp` every time you want to start mplayer instead of
`mplayer` or use an alias.

The config file (which can be found in
`$XDG_CONFIG_HOME/mplayer-autocmd-config.yml`) is a file containing
options in the `YAML <http://www.yaml.org/spec/1.2/spec.html>`_.  A
global mapping maps arbitrary names to the options. While the keys used
in the global mapping don't have a special meaning, they're used for
informational output.

These are the supported options:

call_after_playing
    An application to call after the file has been played. If the application
    needs any arguments, separate them with commas from each other and the
    applications name.

options
    A list of strings containg the arguments to pass to mplayer for this profile.

regex
    A regular expression that has to match the filename using Pythons
    `re.search`_ function in order for the other stuff in the section to be
    applied.

remove_after_playing
    If this is True the file will be removed after it has been played.

keys
    This is another mapping that maps key names to a command that will be
    executed when the key is pressed.

For a list of all possible keys, use `mplayer --input=keylist`.
For a list of all possible commands, use `mplayer --input=cmdlist`.

An example config file called `example.config` is part of `the git
repository`_.

.. _re.search: http://docs.python.org/3.3/library/re.html#re.search

.. _the git repository: https://github.com/mineo/mplayer-autocmd
