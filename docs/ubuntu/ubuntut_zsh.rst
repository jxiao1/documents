Zsh Usage
=========

zsh
---------

::

    sudo apt-get install zsh
    chsh -s $(which zsh)  # need to reboot the system


oh-my-zsh
---------

**install oh-my-zsh**::

    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

**themes**

Preview: https://github.com/robbyrussell/oh-my-zsh/wiki/Themes

modify the prompt in ~/.oh-my-zsh/themes/robbyrussell.zsh-theme::

    PROMPT='${ret_status} %{$fg[cyan]%}%d%{$reset_color%} $(git_prompt_info)'

**plugins**

1. git:
Git is include by default. It will show git information in prompt line.

2. autojump::

    sudo apt-get install autojump


The final plugins::

    plugins=(git autojump)


FAQ
---

**Q**: vi ~/.z  (TAB Complete)          
_arguments:450: _vim_files: function definition file not found

**A**: rm -rf ~/.zcompdump* ; then relogin the zsh
