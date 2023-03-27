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
  echo " $(tput setaf $1) $(tput bold)"
}
blue_bold() {
  bold_color_text "45"
}
purple_bold() {
  bold_color_text "5"
}
gray_bold() {
  bold_color_text "7"
}
pink_bold() {
  bold_color_text "219"
}

white_bold() {
  bold_color_text "15"
}
# tests
# blue_bold "gaygay"
# purple_bold "gaygay"
# gray_bold "gaygay"
# white_bold "gaygay"
# pink_bold "gaygay"


cycle() {
  echo
  echo "beginning:"
  switch=0
  for ((i = 1; i < 128; i++)); do
    # delay between each print in seconds
    sleep .1
    if [ $switch -eq 0 ]; then
      echo "gay"
    else 
      echo
    fi

    if [ $(( i % $1 )) -eq 0 ]; then
      # toggle the switch
      if [ $switch -eq 1 ]; then
        switch=0
      else
        switch=1
      fi
    fi 
  done
  white_bold 
  echo "end"
  echo
}
blue_bold
cycle 7
#================================================== 
