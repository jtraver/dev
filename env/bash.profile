# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH

export PATH=/mnt/hgfs/jtraver/dev/git/jtraver/qaa/tools/bin:/mnt/hgfs/jtraver/dev/lua/install/lua-5.2.2/src:.:$PATH

unset PROMPT_COMMAND
PROMPT_COMMAND='echo -ne "\033]0;CentOs1 ${PWD##/*/}\007"'
export PROMPT_COMMAND

SSH_ASKPASS=./pass.sh
export SSH_ASKPASS

PYTHON_VERS=2.6
export PYTHON_VERS

PYTHONPATH=:/mnt/hgfs/jtraver/dev/git/jtraver/qaa/lib/:/mnt/hgfs/jtraver/dev/git/jtraver/qaa/tools/python
export PYTHONPATH

LD_LIBRARY_PATH=/mnt/hgfs/jtraver/dev/git/jtraver/qaa-tools/luna:/mnt/hgfs/jtraver/dev/git/jtraver/qaa/tools/lib
export LD_LIBRARY_PATH

PACKAGE=http://v1:8080/job/aerospike-server+matrix+dev3.0/OS=centos6/lastSuccessfulBuild/artifact/pkg/packages/aerospike-server.el6.x86_64.rpm
export PACKAGE

SSHAGENT=/usr/bin/ssh-agent
SSHAGENTARGS="-s"
if [ -z "$SSH_AUTH_SOCK" -a -x "$SSHAGENT" ]; then
  eval `$SSHAGENT $SSHAGENTARGS`
  trap "kill $SSH_AGENT_PID" 0
fi

SSH_ENV="$HOME/.ssh/environment"

function start_agent {
     echo "Initialising new SSH agent..."
     /usr/bin/ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
     echo succeeded
     chmod 600 "${SSH_ENV}"
     . "${SSH_ENV}" > /dev/null
     /usr/bin/ssh-add;
}

# Source SSH settings, if applicable

if [ -f "${SSH_ENV}" ]; then
     . "${SSH_ENV}" > /dev/null
     #ps ${SSH_AGENT_PID} doesn't work under cywgin
     ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
         start_agent;
     }
else
     start_agent;
fi

# cd /mnt/hgfs/jtraver/dev/git/jtraver/dev/env/centos
# cd /mnt/hgfs/jtraver/dev/git/jtraver/test/john/env/centos
cd /home/jtraver/dev/git/jtraver/test/john/env/centos
