#!/bin/bash

# trap ctrl_c INT
# 
# function ctrl_c() {
#         echo "** Trapped CTRL-C"
# 	pkill gnuplot
# }

proj=$1
/usr/bin/gnuplot -e "projname='$proj'" currentplot.gnu &
/usr/bin/gnuplot -e "projname='$proj'" waveformplot.gnu 


