Linux tmux
==========

shortcuts & cheatsheet
----------------------
https://gist.github.com/MohamedAlaa/2961058


Configuration Example
---------------------
::

    #--basic-------------------------------------------------------#
    ##set -g default-terminal "screen"
    set -g default-terminal "screen-256color"
    set -g display-time 5000
    set -g repeat-time 1000
    set -g escape-time 0
    set -g history-limit 65535
    set -g base-index 1
    set -g pane-base-index 1
    set -g history-limit 10000
    set -g terminal-overrides 'xterm*:smcup@:rmcup@'


    #--bindkeys----------------------------------------------------#
    #Escape key
    unbind C-b
    set -g prefix C-a
    bind a send-prefix

    #windows
    unbind '"'
    bind h split-window -h
    unbind %
    bind v split-window -v
    unbind i
    bind C-g display-message

    #pane
    bind j select-pane -L
    bind i select-pane -U
    bind k select-pane -D
    bind l select-pane -R

    #quit
    unbind x
    unbind &
    unbind q
    bind q confirm-before -p "kill-pane #P? (y/n)" kill-pane
    bind Q confirm-before -p "kill-window #W? (y/n)" kill-window
    bind e confirm-before -p "kill-session #S? (y/n)" kill-session

    #misc
    bind r source-file ~/.tmux.conf \; display "Reloaded!"
    #bind m command-prompt "splitw -h 'exec man %%'"
    #bind @ command-prompt "splitw -h 'exec perldoc -f %%'"


    #--Window------------------------------------------------------#
    setw -g mode-keys vi
    setw -g utf8 on
    setw -g window-status-current-bg red
    setw -g window-status-current-fg white
    setw -g window-status-current-attr bright
    setw -g window-status-attr bright
    setw -g window-status-format '#[fg=cyan,dim]#I#[fg=blue] #[default]#W#[fg=grey,dim]'
    setw -g window-status-current-format '#[fg=cyan,dim]#I#[fg=blue] #[default]#W#[fg=grey,dim]'


    #--Statusbar---------------------------------------------------#
    set -g status-keys vi
    set -g status-utf8 on
    set -g status-left ""
    set -g status-left-length 0
    set -g status-interval 2
    set -g status-fg white
    set -g status-bg blue
    set -g status-right "#[fg=white]#S:#W:#P [#(tmux ls|wc -l) sessions]#[default]"
    #set -g status-justify centre
    #set -g status-right-length 10


    #--Mouse-------------------------------------------------------#
    setw -g mode-mouse on
    set -g mouse-resize-pane on
    set -g mouse-select-pane on
    set -g mouse-select-window on

