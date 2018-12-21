Ubuntu Vim Editor
=================

Awesome-vim
-----------
https://github.com/akrawchyk/awesome-vim

https://github.com/matteocrippa/awesome-vim


Setup
-----
https://github.com/VundleVim/Vundle.vim/wiki/Examples

**Dependencies**::

    $ sudo apt-get install python vim exuberant-ctags git
    $ sudo pip install dbgp vim-debug pep8 flake8 pyflakes isort
    $ sudo npm -g install instant-markdown-d

**Install vundle**::
    $ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

**Prepare for YouCompleteMe**::

    $ sudo apt-get install cmake build-essential libclang1 libclang-dev python-dev
    $ vim vimrc:
        Plugin 'Valloric/YouCompleteMe'

**Install plugins**::

    :PluginInstall                  # Install all defined plugins
    :PluginUpdate                   # Update all defined plugins

    or:

    $ vim +PluginInstall +qall        # Install all defined plugins outside Vim.

**Postinstall for YouCompleteMe**::

    $ cd ~/.vim/bundle/YouCompleteMe
    $ git submodule update --init --recursive
    $ ./install.py --clang-completer


Plugins Usage
-------------

**YouCompleteMe**
https://github.com/Valloric/YouCompleteMe

::

    ctrl+o              # Return
    ctrl+i              # Go ahead


Plugins Shortcuts
-----------------

nerdtree::

    <CR>|o: open in prev window (auto close if NERDTreeQuitOnOpen = 1)
    go:     preview only, so will not change the window focuse.
    gi:     split in preview window
    gs:     vsplit in preview window
    i:      split current nerdtree window, so it's better useing it with NERDTreeQuitOnOpen = 1
    s:      open vsplist


vimrc Example
-------------

https://raw.githubusercontent.com/jxiao1/documents/master/files/workenv/vimrc
https://github.com/liuchengxu/space-vim
