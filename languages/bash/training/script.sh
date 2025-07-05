#!/bin/bash

# Challenge setup
echo -e "\n##############################################################################"
echo "#                      Mise en place du challenge                            #"
echo "#                                                                            #"
echo "#                       Construction de la maison                            #"
echo -e "##############################################################################\n"
# Define a variable for the URL of the maison file archive
Maison_URL="https://github.com/WildCodeSchool/ASD_Resources/raw/main/Quests_resources/maison.tar.gz"

# Download the file
wget -O maison.tar.gz "$Maison_URL"

# Extract the content
tar -xzf maison.tar.gz

# Challenge instructions
echo -e "\n##############################################################################"
echo "#                           Début du challenge                               #"
echo "#                                                                            #"
echo "#                             À toi de jouer !                               #"
echo -e "##############################################################################\n"
echo "La construction de la maison est terminée ! Le jeu peut commencer."
echo "Règles du jeu :"
echo "Tu es dans une magnifique maison, composée de 4 pièces, à la recherche d'un trésor légendaire."
echo "Utilise les commandes 'ls' et 'cd' pour te déplacer à travers celle-ci et trouver un coffre à trésor."
echo "Utilise 'cat' pour afficher le contenu des différents éléments que tu trouves au fur et à mesure de ton exploration."
echo "Une fois en possession du contenu du coffre, complétes la quête qui t'a mené ici :)."
echo "Bonne chasse !"

# Indiquez comment commencer
echo "Pour commencer, exécutez :"
echo "cd Maison"
echo "ls"
