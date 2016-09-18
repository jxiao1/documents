Ubuntu Zsh Usage
================

zsh
---------
https://wiki.gentoo.org/wiki/Zsh/Guide

::

    sudo apt-get install zsh
    chsh -s $(which zsh)  # need to reboot the system


oh-my-zsh
---------

**install oh-my-zsh**::

    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

**themes**

Preview: https://github.com/robbyrussell/oh-my-zsh/wiki/Themes

or::

    autoload -U promptinit
    prompinit
    prompt -p

Modify the prompt in ~/.oh-my-zsh/themes/robbyrussell.zsh-theme
or export prompt directly in .zshrc::

    local ret_status="%(?:%{$fg_bold[green]%}➜ :%{$fg_bold[red]%}➜ )"
    local suffix="%{$fg_bold[blue]%}$ %{$reset_color%}"                             
    PROMPT='%{$fg_bold[cyan]%}%d%{$reset_color%} $(git_prompt_info)
    ${ret_status} %{$fg[green]%}[%* %D]%{$reset_color%} ${suffix}'

    local ret_status="%(?:%{$fg_bold[green]%}➜ :%{$fg_bold[red]%}➜ )"
    local suffix="%{$fg_bold[blue]%}$ %{$reset_color%}"
    export PROMPT='%{$fg_bold[cyan]%}%d%{$reset_color%} $(git_prompt_info)
    %F{magenta}%B%K{magenta}█▓▒░%F{white}%K{magenta}%B%* %D%b%F{magenta}%K{black}█▓▒░ ${ret_status}%b%k%f%{$reset_color%} '

    Sequence    Printed
    %T          System time (HH:MM)
    %*          System time (HH:MM:SS)
    %D          System date (YY-MM-DD)
    %n          Your username
    %B - %b     Begin - end bold print
    %U - %u     Begin - end underlining
    %d          Your current working directory
    %~          Your current working directory, relative to ~
    %M          The computer's hostname
    %m          The computer's hostname (truncated before the first period)
    %l          Your current tty 

**plugins**

1. git:
Git is include by default. It will show git information in prompt line.

2. autojump::

    sudo apt-get install autojump


The final plugins::

    plugins=(git autojump)


FAQ
---

#. | Q: vi ~/.z  (TAB Complete) 
   |    arguments:450: _vim_files: function definition file not found.
   | A: rm -rf ~/.zcompdump* ; then relogin the zsh
   |
#. | Q: time -p ls (Command not found: -p)
   | A: time in zsh is a shell reserved word, but not /usr/bin/time binary tool.


zshrc example
-------------

https://raw.githubusercontent.com/jxiao1/documents/master/files/workenv/zshrc

