if status is-interactive
    # Commands to run in interactive sessions can go here
end

set PATH ~/.cargo/bin $PATH
#neofetch
set fish_greeting "Welcome, Dave"
set -g theme_display_user yes
set -g theme_hide_hostname no
set -g theme_hostname always
alias ll "exa -l -g --icons"

function fish_prompt
    powerline-shell --shell bare $status
end
