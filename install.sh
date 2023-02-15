#!/bin/bash

NAME="MyScript"

[[ ! -d ${NAME} ]] && exit

mv ${NAME} ~
cd ~/${NAME}
chmod +x myscript/myscript

if [ -f ~/.bashrc ]; then
    echo "export PATH=\$PATH:$(pwd)/links:$(pwd)/myscript" >> ~/.bashrc
elif [ -f ~/.zshrc ]; then
    echo "export PATH=\$PATH:$(pwd)/links:$(pwd)/myscript" >> ~/.zshrc
else
    printf "\033[33mYour terminal cannot have MyScript\033[m"
fi