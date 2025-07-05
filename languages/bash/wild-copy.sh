#!/bin/bash


token="y"


while [ "$token" = "y" ]

    do

        read -p "Quel dossier souhaitez-vous sauvegarder ? " target_folder


        if [ ! -d "$target_folder" ]; then

            echo "Erreur, le dossier n'existe pas."

            exit 0

        fi


        read -p "Où souhaitez-vous sauvegarder le fichier ? " target_save


        read -p "Vous souhaitez sauvegarder $target_save ? [y/n] " confimation


        if [ ! -d "$target_save" ] && [ "$confirmation" = "y" ]; then

            mkdir $target_save

            cp $target_folder $target_save

            echo "Sauvegardé !"

        elif [ "$confirmation" = "y" ]; then

            cp $target_folder $target_save

            echo "Sauvegardé !"

        fi


        read -p "Souhaitez-vous sauvegarder un autre dossier ? [y/n] " token


    done
