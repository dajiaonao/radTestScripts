#http://www.gnuplotting.org/multiple-lines-with-different-colors/
set style line 2  lc rgb '#0025ad' lt 1 lw 1.5 # --- blue
set style line 3  lc rgb '#0042ad' lt 1 lw 1.5 #      .
set style line 4  lc rgb '#0060ad' lt 1 lw 1.5 #      .
set style line 5  lc rgb '#007cad' lt 1 lw 1.5 #      .
set style line 6  lc rgb '#0099ad' lt 1 lw 1.5 #      .
set style line 7  lc rgb '#00ada4' lt 1 lw 1.5 #      .
set style line 8  lc rgb '#00ad88' lt 1 lw 1.5 #      .
set style line 9  lc rgb '#00ad6b' lt 1 lw 1.5 #      .
set style line 10 lc rgb '#00ad4e' lt 1 lw 1.5 #      .
set style line 11 lc rgb '#00ad31' lt 1 lw 1.5 #      .
set style line 12 lc rgb '#00ad14' lt 1 lw 1.5 #      .
set style line 13 lc rgb '#09ad00' lt 1 lw 1.5 # --- green

plot 'sample_link_0' using 1:2 w l ls 2,\
     'sample_link_1' using 1:2 w l ls 4,\
     'sample_link_2' using 1:2 w l ls 6,\
     'sample_link_3' using 1:2 w l ls 8,\
     'sample_link_4' using 1:2 w l ls 11

pause 10
system('./get_files.py')
reread
