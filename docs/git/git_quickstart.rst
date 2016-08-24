Git Quickstart
==============

https://git-scm.com/book

Installation
------------
For example, in Ubuntu::

    sudo apt-get install git
    sudo apt-get install git-doc git-svn git-email git-gui gitk 
    sudo apt-get install gitg
    sudo apt-get install qgit
    sudo apt-get install kdiff3

Get help
--------
::

    git help [command]

Configuration
-------------
::

    git config --global user.name "myname"
    git config --global user.email "my@example.com"
    git config --global core.editor vim
    git config --global color.ui true
    git config --global merge.tool kdiff3 

    # For current user only
    git config --global alias.st status
    git config --global alias.ci commit
    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.lg log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

    # For all user
    sudo git config --system alias.st status
    sudo git config --system alias.ci commit
    sudo git config --system alias.co checkout
    sudo git config --system alias.br branch

    # Get current repo settings
    git config --get remote.origin.url
    git config -f path-to-repo/.git/config --get remote.origin.url
    git ls-remote <rempte-origin-url> refs/heads/master #remote head id
    git ls-remote ./ refs/heads/master                  #local head id

