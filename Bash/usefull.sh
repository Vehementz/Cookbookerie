history 

# show when pwd commmand have been used 
history | grep pwd

    # # # Return 
    #   405  pwd
    #   921  pwd
    #   924  history | grep pwd
    #   925  pwd
    #   932  history | grep pwd

#run the pwd with the 925 id that we se above
!925


# Show the sha256 checksum of the ye.txt file 
sha256sum ye.txt



## Create symbolic link
ln -s /home/clement/Bureau/yu/ya/yu/ye ~/shortcut 

curl -C  -H "Authorization: Bearer ya29.beartruc" https://www.googleapis.com/drive/v3/files/truc -o namefile.file.vmdk



# # # need to include the output of a complex command in your script, you can write the statement inside back ticks.
#!/bin/bash

var=`df -h | grep tmpfs`
echo $var


# Cron job example
* * * * * sh /path/to/script.sh
Here, * represent represents minute(s) hour(s) day(s) month(s) weekday(s), respectively.

Below are some examples of scheduling cron jobs.
SCHEDULE 	SCHEDULED VALUE
5 0 * 8 * 	At 00:05 in August.
5 4 * * 6 	At 04:05 on Sunday.
0 22 * * 1-5 	At 22:00 on every day-of-week from Monday through Friday.



crontab -l lists the already scheduled scripts for a particular user.

find . -type f -name "*.sh"
