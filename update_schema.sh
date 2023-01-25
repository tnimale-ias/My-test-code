#!/bin/bash
echo "Syncing you sql schema...."
sleep 3
tput cuu1
tput el

{ # try

    git clone git@github.com:integralads/firewall-db.git
    #save your output

} || {
    # catch
    # could not clone firewall-db repo
    echo"*"
    echo"*"
    echo"*"
    echo "Sorry): It seems you do not have access to firewall-db repo"
    echo"*"
    echo"*"
    echo"*"
}

python3 firewall_db_update_poc.py
echo "Syncing you sql schema...."
#rm -rf firewall-db
