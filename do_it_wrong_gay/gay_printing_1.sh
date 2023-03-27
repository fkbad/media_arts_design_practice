#gay() {
  #echo "$1" | gay -g
#}
#les() {
  #echo "$1" | gay -l
#}
#for ((i = 0; i < 10; i++)); do
  #gay "****************"
  #les "****************"
#done

#!/bin/bash
# tputcolors

#================================================== 
# https://stackoverflow.com/questions/18560647/how-to-make-bash-shell-display-colorful-text

# figuring out colored text
echo
echo -e "$(tput bold) reg  bld  und   tput-command-colors$(tput sgr0)"

for i in $(seq 1 7); do
  echo " $(tput setaf $i)Text$(tput sgr0) $(tput bold)$(tput setaf $i)Text$(tput sgr0) $(tput sgr 0 1)$(tput setaf $i)Text$(tput sgr0)  \$(tput setaf $i)"
done

echo ' Bold            $(tput bold)'
echo ' Underline       $(tput sgr 0 1)'
echo ' Reset           $(tput sgr0)'
echo


#================================================== 

# writing helper functions for easy display

bold_color_text() {
  echo " $(tput setaf $2) $(tput bold) $1"
}
blue_bold() {
  bold_color_text "$1" "4"
}
purple_bold() {
  bold_color_text "$1" "5"
}
gray_bold() {
  bold_color_text "$1" "7"
}
white_bold() {
  bold_color_text "$1" "15"
}
# tests
blue_bold "gaygay"
purple_bold "gaygay"
gray_bold "gaygay"
white_bold "gaygay"

#================================================== 
