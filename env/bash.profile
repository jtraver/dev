export PATH=/Users/jtraver/dev/lua/install/lua-5.2.2/src:$PATH

unset PROMPT_COMMAND
PROMPT_COMMAND='echo -ne "\033]0;mac ${PWD##/*/}\007"'
export PROMPT_COMMAND

cd dev/git/jtraver/dev/env
