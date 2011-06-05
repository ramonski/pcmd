Introduction
============

This Script is mainly a shell command generator which executes the command in
the parent shell.

Requirements
------------

This script needs Python 2.7 because of argparse and depends on appscript.

Installation
------------

The best thing is to install it in a Python 2.7 virtualenv for testing::

    $ virtualenv -p python2.7 --no-site-packages pcmd
    $ . pcmd/bin/activate
    $ pip install --editable=git+https://github.com/ramonski/pcmd#egg=pcmd

Configuration
-------------

You can configure your **p-commands** in **$HOME/.p.ini**.

Syntax::

    [<p-section>]
    <p-command> = <any arbitrary shell command>

Call::

    $ p <p-command> <p-section>

Example::

    [develop]
    goto = cd /Users/rbartl/develop
    mvim = mvim /Users/rbartl/develop

The p-command executes the shell command by default in the **Terminal.app**.
This can be overwritten with the Environment Variable **PTERM**, e.g.::

    $ vim .bashrc
    export PTERM="iTerm"


Usage
-----

After you configured some commands, you can execute them like this::

    $ p goto develop # executes -> cd /Users/rbartl/develop
    $ p mvim develop # executes -> mvim /Users/rbartl/develop

Bash Completion
---------------

The p-command supports now bash completion.
If you use bash, you can source the pcmd_wrapper.sh to enable bash completion::

    $ source pcmd_wrapper.sh
    $ p o<TAB>
    option1 option2

    $ p option1 s<TAB>
    section1 section2
