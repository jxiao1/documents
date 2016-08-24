Ubuntu Vim Editor
=================

Setup
-----
https://github.com/VundleVim/Vundle.vim/wiki/Examples

**Dependencies**::

    $ sudo apt-get install python vim exuberant-ctags git
    $ sudo pip install dbgp vim-debug pep8 flake8 pyflakes isort

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

::

    "===============================================================
    " For vundle plugin management
    "===============================================================
    set nocompatible              " be iMproved, required
    filetype off                  " required

    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()

    " let Vundle manage Vundle, required
    Plugin 'VundleVim/Vundle.vim'
    Plugin 'scrooloose/nerdtree'
    Plugin 'Valloric/YouCompleteMe'
    Plugin 'kien/ctrlp.vim'
    Plugin 'rking/ag.vim'
    Plugin 'majutsushi/tagbar'
    Plugin 'tmhedberg/SimpylFold'
    Plugin 'vim-scripts/indentpython.vim'
    Plugin 'nvie/vim-flake8'
    "Plugin 'bling/vim-airline'
    "Plugin 'jiangmiao/auto-pairs'

    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required

    "===============================================================
    " Normal settings
    "===============================================================
    let mapleader = ","
    let g:mapleader = ","

    "syntax highlight
    let python_highlight_all=1
    syntax on

    "highlight the current line (under line)
    set cursorline
    set hls
    set spell spelllang=en_us
    set number
    set noswapfile
    set nobackup
    set nowritebackup

    set autoindent
    set cindent
    set backspace=eol,start,indent
    set showmatch

    set expandtab
    set smarttab
    set shiftwidth=4

    "auto read when a file is changed from the outside
    "set autoread
    "set autowrite

    "encoding format
    set encoding=utf-8
    set langmenu=utf-8
    set fileencodings=utf-8
    set fileencodings=ucs-bom,utf-8,gb18030,gb2312,cp936,big5,euc-jp,euc-kr,latin1
    let &termencoding=&encoding

    au BufNewFile,BufRead *.py set textwidth=100
    au BufNewFile,BufRead *.sh set textwidth=80
    au BufNewFile,BufRead *.sh,*.py set fileformat=unix

    au BufNewFile,BufRead *.js, *.html, *.css set shiftwidth=2

    " Use the below highlight group when displaying
    " bad whitespace at end or behind tab.
    highlight BadWhitespace ctermbg=red guibg=red
    au BufRead,BufNewFile * match BadWhitespace /\s\+$/
    au BufRead,BufNewFile * match BadWhitespace /^\t\+/

    "!! and @@ for 4 space, replace of tab key
    "inoremap !! <esc>hl<del>h<del>h<del>h<del>i
    "inoremap @@ <esc>lhi<space><space><space><space><esc>i
    "map !! h<del>h<del>h<del>h<del>
    "map @@ i<space><space><space><space><esc>l

    " Tab commands in vim
    nmap <c-t> :tabnew<CR>
    nmap <c-j> :tabn<CR>
    nmap <c-k> :tabp<CR>

    " Toggle some check
    nmap <F8> :set nospell<CR>:set nopaste<CR>

    " Toggle the paste mode to fix autoindent issue
    set pastetoggle=<leader>v

    " Enable folding
    set foldmethod=indent
    set foldlevel=99
    nnoremap <space> za

    "set laststatus=2

    "===============================================================
    " For plugin Valloric/YouCompleteMe
    "===============================================================
    nnoremap <leader>j :YcmCompleter GoToDefinitionElseDeclaration<CR>
    "let g:ycm_key_list_select_completion = ['<TAB>', '<c-n>', '<Down>']
    "let g:ycm_key_list_previous_completion = ['<Up>']
    "let g:ycm_auto_trigger = 1
    "let g:ycm_min_num_of_chars_for_completion = 3
    "set completeopt-=preview

    "===============================================================
    " For plugin kien/ctrlp.vim
    "===============================================================
    " Press ctel+p to open the ctrlp windown and input the filename
    " enter to open file in current windown
    " ctrl+t to open file in new tab
    let g:ctrlp_map = '<c-p>'
    let g:ctrlp_cmd = 'CtrlP'
    let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn|pyc)$'

    "===============================================================
    " For plugin rking/ag.vim
    "===============================================================
    "let g:ag_prg = 'ag --nogroup --noheading '

    "===============================================================
    " For plugin majutsushi/tagbar
    "===============================================================
    nmap <F3> :TagbarToggle<CR>

    "===============================================================
    " For plugin scrooloose/nerdtree
    "===============================================================
    map <F4> :NERDTreeToggle<CR>
    let NERDTreeQuitOnOpen = 1

    "===============================================================
    " For tmhedberg/SimpylFold
    "===============================================================
    let g:SimpylFold_docstring_preview=1

