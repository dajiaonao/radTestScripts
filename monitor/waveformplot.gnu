#http://www.gnuplotting.org/multiple-lines-with-different-colors/
set style line 2  lc rgb '#25ad00' lt 1 lw 1.5 # --- blue
set style line 3  lc rgb '#42ad00' lt 1 lw 1.5 #      .
set style line 4  lc rgb '#60ad00' lt 1 lw 1.5 #      .
set style line 5  lc rgb '#7cad00' lt 1 lw 1.5 #      .
set style line 6  lc rgb '#99ad00' lt 1 lw 1.5 #      .
set style line 7  lc rgb '#ada400' lt 1 lw 1.5 #      .
set style line 8  lc rgb '#ad8800' lt 1 lw 1.5 #      .
set style line 9  lc rgb '#ad6b00' lt 1 lw 1.5 #      .
set style line 10 lc rgb '#ad4e00' lt 1 lw 1.5 #      .
set style line 11 lc rgb '#ad3100' lt 1 lw 1.5 #      .
set style line 12 lc rgb '#ad1400' lt 1 lw 1.5 #      .
set style line 13 lc rgb '#ad0009' lt 1 lw 1.5 # --- green

plot 'sample_link_0' using 1:2 w l ls 2,\
     'sample_link_1' using 1:2 w l ls 4,\
     'sample_link_2' using 1:2 w l ls 6,\
     'sample_link_3' using 1:2 w l ls 8,\
     'sample_link_4' using 1:2 w l ls 11

pause 10
system('./link_files.py')
reread
