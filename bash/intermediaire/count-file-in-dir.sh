#!/bin/bash
echo "Enter a directory path"
read dir
ls -l $dir | wc -l
