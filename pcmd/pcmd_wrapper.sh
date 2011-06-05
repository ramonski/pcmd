# -*- mode: shell-script -*-

if [ -n "$BASH" ] ; then
    _cmds () {
        local cur="${COMP_WORDS[COMP_CWORD]}"

        if [ ${COMP_CWORD} -eq 1 ]
        then
            COMPREPLY=($(compgen -W "`_p_options`" -- ${cur}))
        else
            COMPREPLY=($(compgen -W "`_p_sections`" -- ${cur}))
        fi
    }

    complete -o default -o nospace -F _cmds p
fi
