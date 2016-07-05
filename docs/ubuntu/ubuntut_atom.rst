Ubuntu Atom Editor
==================


http://flight-manual.atom.io/
https://atom-china.org/t/atom/62
http://atom-china.org/
https://atom.io/docs


Install
-------

https://github.com/atom/atom/blob/master/docs/build-instructions/linux.md

Requirements::

    sudo apt-get install build-essential git libgnome-keyring-dev fakeroot nodejs

Get deb package here: https://atom.io/
Install it like this::

    sudo dpkg -i atom-amd64.deb

Or::

    sudo add-apt-repository ppa:webupd8team/atom
    sudo apt-get update
    sudo apt-get install atom


Configurations
--------------


Plugins
-------

    you-complete-me
    autocomplete
    autocomplete-html
    autocomplete-css
    autocomplete-json
    autocomplete-paths

    python-tools
    python-indent
    autocomplete-python
    linter-pep8     (pip install pep8)
    atom-beautify

    docblockr

    file-icons

    tree-view-git-status

    vim-mode-plus or vim-mode + vim-mode-visual-block

    terminal-plus

    fuzzy-grep


Shortcuts
---------
::

    ctrl-o          Open file
    ctrl-shift-o    Open folder
    ctrl-\          Hide folder tree
    ctrl-/          Trigger line comments
    ctrl-,          Open Settings pane
    ctrl-w q        close current pane

    ctrl+p          serach files
    ctrl+g          go to line

    alt-<N>         Switch to tab <N>
    alt-\           Switch to foler-tree or return back

