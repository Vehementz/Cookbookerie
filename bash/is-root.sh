#!/bin/bash
if [ "$UID" -eq 0 ]
then
echo "root user"
else
echo "Not a root user"
fi

