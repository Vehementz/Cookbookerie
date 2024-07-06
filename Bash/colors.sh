#! /usr/bin/env bash

RED="31"
GREEN="32"
BOLDGREEN="\e[1;${GREEN}m"
ITALICRED="\e[3;${RED}m"
ENDCOLOR="\e[0m"

echo -e "${BOLDGREEN}Behold! Bold, green text.${ENDCOLOR}"
echo -e "${ITALICRED}Italian italics${ENDCOLOR}"
