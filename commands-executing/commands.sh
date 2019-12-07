#!/bin/bash

get_users()
{
    awk -F':' '{ print $1}' /etc/passwd
}

check_exist_user()
{
    for data in $(awk -F':' '{ print $1}' /etc/passwd)
    do
        if [[ $data == $1 ]]; then
            echo "TRUE"
            return
        fi
    done
    echo "FALSE"
}

check_exist_user $1