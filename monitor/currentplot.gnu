#set xrange [0:20]
#set yrange [0:400]
##set size ratio -1
#if (GPVAL_DATA_X_MAX > 100) set xrange[GPVAL_DATA_X_MAX-100:GPVAL_DATA_X_MAX]; 
set xdata time
set timefmt x "%Y-%m-%d_%H:%M:%S"
plot "time_current.dat" using 1:2 with lines
pause 10
reread
