#!/bin/bash
python3 $1 $2 $3

python_status=$?

current_date=`date "+%D %T"`

msg="A script has ran to error:  

Server: $HOSTNAME

Script Name: $1 
File name: $3

Time: $current_date"

echo "$python_status"
echo "$msg"

python request_jobs.py input_1.json embedded

#msg="The following Script ran to error: $1 at $current_date"
#if [ $python_status -ne 0 ]; then
##    echo "$msg" | mailx -s "Script Failure"  vash@email;
#fi;

