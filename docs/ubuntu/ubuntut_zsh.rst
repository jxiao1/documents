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

::

    # Path to your oh-my-zsh installation.
    export ZSH=/home/jxiao1/.oh-my-zsh

    # Set name of the theme to load.
    # Look in ~/.oh-my-zsh/themes/
    # Optionally, if you set this to "random", it'll load a random theme each
    # time that oh-my-zsh is loaded.
    ZSH_THEME="robbyrussell"

    # Uncomment the following line to use case-sensitive completion.
    # CASE_SENSITIVE="true"

    # Uncomment the following line to use hyphen-insensitive completion. Case
    # sensitive completion must be off. _ and - will be interchangeable.
    # HYPHEN_INSENSITIVE="true"

    # Uncomment the following line to disable bi-weekly auto-update checks.
    # DISABLE_AUTO_UPDATE="true"

    # Uncomment the following line to change how often to auto-update (in days).
    # export UPDATE_ZSH_DAYS=13

    # Uncomment the following line to disable colors in ls.
    # DISABLE_LS_COLORS="true"

    # Uncomment the following line to disable auto-setting terminal title.
    # DISABLE_AUTO_TITLE="true"

    # Uncomment the following line to enable command auto-correction.
    # ENABLE_CORRECTION="true"

    # Uncomment the following line to display red dots whilst waiting for completion.
    # COMPLETION_WAITING_DOTS="true"

    # Uncomment the following line if you want to disable marking untracked files
    # under VCS as dirty. This makes repository status check for large repositories
    # much, much faster.
    # DISABLE_UNTRACKED_FILES_DIRTY="true"

    # Uncomment the following line if you want to change the command execution time
    # stamp shown in the history command output.
    # The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
    # HIST_STAMPS="mm/dd/yyyy"

    # Would you like to use another custom folder than $ZSH/custom?
    # ZSH_CUSTOM=/path/to/new-custom-folder

    # Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
    # Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
    # Example format: plugins=(rails git textmate ruby lighthouse)
    # Add wisely, as too many plugins slow down shell startup.
    plugins=(git autojump)

    # User configuration

    # export PATH="/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
    # export MANPATH="/usr/local/man:$MANPATH"

    source $ZSH/oh-my-zsh.sh

    # You may need to manually set your language environment
    # export LANG=en_US.UTF-8

    # Preferred editor for local and remote sessions
    # if [[ -n $SSH_CONNECTION ]]; then
    #   export EDITOR='vim'
    # else
    #   export EDITOR='mvim'
    # fi

    # Compilation flags
    # export ARCHFLAGS="-arch x86_64"

    # ssh
    # export SSH_KEY_PATH="~/.ssh/dsa_id"

    # Set personal aliases, overriding those provided by oh-my-zsh libs,
    # plugins, and themes. Aliases can be placed here, though oh-my-zsh
    # users are encouraged to define aliases within the ZSH_CUSTOM folder.
    # For a full list of active aliases, run `alias`.
    #
    # Example aliases
    alias vi='vim'
    alias grep='grep --color=auto'
    alias zshconfig='source ~/.zshrc'
    alias vimconfig='source ~/.vimrc'
    alias time='/usr/bin/time -p'

    alias -s txt=vim          # Run *.txt as opening it in vim editor

    alias -g ...='../..'      # cd ... => cd ../..
    alias -g ....='../../..'
    alias -g .....='../../../..'
    alias -g L=' | less'      # cat 1.log L => cat 1.log | less
    alias -g M=' | more'	  # cat 1.log M => cat 1.log | more
    alias -g H=' | head'	  # cat 1.log M => cat 1.log | head
    alias -g T=' | tail'	  # cat 1.log M => cat 1.log | tail
    alias -g S=' | sort'	  # cat 1.log M => cat 1.log | sort

    # alias for paths (cd ~xxx)
    hash -d doc='/home/jxiao1/documents/documents.jxiao1'

    # auto pushed
    #setopt AUTO_PUSHD
    #setopt PUSHD_IGNORE_DUPS

    # "dpkg -l firefox*" will not report "no matches found"
    setopt no_nomatch

    # cmd #this is the comment
    setopt INTERACTIVE_COMMENTS 

    export PATH=$PATH:/home/jxiao1/tools/jbox/bin

    # Prompt
    local ret_status="%(?:%{$fg_bold[green]%}➜ :%{$fg_bold[red]%}➜ )"
    local suffix="%{$fg_bold[blue]%}$ %{$reset_color%}"
    export PROMPT='%{$fg_bold[cyan]%}%d%{$reset_color%} $(git_prompt_info)
    %F{magenta}%B%K{magenta}█▓▒░%F{white}%K{magenta}%B%* %D%b%F{magenta}%K{black}█▓▒░ ${ret_status}%b%k%f%{$reset_color%} '
