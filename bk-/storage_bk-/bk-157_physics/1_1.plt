if (exist("n") == 0 || n < 0) n = 0

#plot sin(x)
#plot for [i=1:5] sin(x*i)*exp(-i)
#plot for [i=1:5] sin(x)*exp(-i)
i = 1

#n_max = 20
#n_max = 40
#n_max = 80
#n_max = 120
#n_max = 300
n_max = 400

set samples 500
#set xrange [-3 : 3]
set xrange [-6*pi : 6*pi]
set yrange [- n_max : n_max]

set grid lw 2
#plot  sin(x), sin(x)*exp(-i)
#plot exp(-1)

set terminal jpeg  enhanced font "Times" 15 size 600, 600

#time_label = "20170719_142747"
#time_label = "20170719_143118"
#time_label = "20170719_143244"
#time_label = "20170719_144218"
time_label = "20170719_144607"

dname_images = sprintf("images_%s", time_label)
#dname_images = "images_20170719_142533"

outfile = sprintf("images/%s/%s_%02d.jpg", time_label, dname_images, n)
#outfile = sprintf("images/%s_%02d.jpg", dname_images, n)
#outfile = sprintf("images/%s.jpg", strftime("%Y%m%d_%H%M%S", time(0)+9*3600))

set output outfile

#n = 5

str_Title = sprintf("sum of sins : sin(x * %d)", n)

set title str_Title


#plot exp(-x), sin(x)
#plot exp(-x) * sin(x), sin(x)
#plot sin(x), sin(x*2)
#plot for [i=1:5] sin(x * i)
#plot sum[i=1:5] sin(x * i)
#plot sum[i=1:5] cos(x * i)
#plot sum[i=1:n] cos(x * i)
plot sum[i=1 : (n + 1)] cos(x * i)

########################
#
# repeat
#
########################
#n_max = 20
#n_max = 210
#wait = 0.5
#wait = 0.1
wait = 0

if (n < n_max)  pause wait; n = n + 1; unset label; reread

n = 0


