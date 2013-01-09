So, what does this do?

`automp` allows you to automatically append options or use different keybinding
depending on the file you're playing.
This is great if you want to skip the intro at the beginning (by providing an
`-ss xx:xx` option) without doing anything or skipping something with a known
length in the middle of the file at the press of a button(by providing a
`key=seek xx.xx` mapping)

The config file (which can be found in
`$XDG_CONFIG_HOME/mplayer-autocmd-config`) is a file that's parsed by Pythons
`configparser` module, for a description of the terminology and it's
possibilities look at `the documentation`_.

The section name is used as a "profile name", it has no special meaning except
for showing you which profile has been chosen.

There are only two supported options (or keys):

regex
    A regular expression that has to match the filename using Pythons
    `re.search`_ function in order for the other stuff in the section to be
    applied.

options
    A string containg the arguments to pass to mplayer for this profile.

Every other option is treated as a key (like on your keyboard) with the
value being the command the key is bound to.
For a list of all possible keys, use `mplayer --input=keylist`.
For a list of all possible commands, use `mplayer --input=cmdlist`.

An example config file called `example.config` is part of `the git
repository`_.

.. _the documentation: http://docs.python.org/3.3/library/configparser.html#supported-ini-file-structure

.. _re.search: http://docs.python.org/3.3/library/re.html#re.search

.. _the git repository: https://github.com/mineo/mplayer-autocmd
