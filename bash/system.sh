#### Description: dmesg command is used to examine the kernel's ring buffer and also to display the kernel related messages
dmesg

#### Description: sleep command will be used to suspend a program execution for the specified time
sleep 30

#### List all the files under "/etc" directory which are modified in last 30 days ?
find /etc -iname "*" -type f -mtime -30

#### count root time in the file
grep "root" -c /var/log/auth.log 

grep "root" /var/log/auth.log | wc -l
