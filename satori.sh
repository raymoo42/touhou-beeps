for oct in 3 5 7
do
	# Noten
	as2=$((116*$oct))
	h2=$((123*$oct))

	cs3=$((139*$oct))
	d3=$((146*$oct))
	e3=$((164*$oct))
	f3=$((174*$oct))
	fs3=$((185*$oct))
	g3=$((196*$oct))
	gs3=$((207*$oct))
	a3=$((220*$oct))
	as3=$((233*$oct))
	h3=$((246*$oct))

	cs4=$((277*$oct))
	d4=$((293*$oct))

	# Beeps
	beep -f$h2  -l 600 \
	-n   -f$cs3 -l 100 \
	-n   -f$d3  -l 100 \
	-n   -f$fs3 -l 200 \
	-n   -f$h2  -l 200 \
	-n   -f$d3  -l 200 \
	-n   -f$fs3 -l 200 \
	-n   -f$g3  -l 200 \
	-n   -f$h2  -l 200 \
	-n   -f$cs3 -l 200 \
	-n   -f$g3  -l 200 \
	-n   -f$fs3 -l 600 \
	-n   -f$fs3 -l 200 \
	-n   -f$f3  -l 200 \
	-n   -f$h2  -l 200 \
	-n   -f$cs3 -l 200 \
	-n   -f$f3  -l 200 \
	-n   -f$e3  -l 300 \
	-n   -f$d3  -l 300 \
	-n   -f$cs3 -l 200 \
	-n   -f$as2 -l 600 \
	-n   -f$cs3 -l 100 \
	-n   -f$d3  -l 100 \
	-n -f$fs3 -l 200 \
	-n -f$e3 -l 100 \
	-n -f$fs3 -l 100 \
	-n -f$as2 -l 400 \
	-n -f$h2 -l 400 \
	-n -f$cs3 -l 200 \
	-n -f$d3 -l 100 \
	-n -f$cs3 -l 100 \
	-n -f$h2 -l 300 \
	-n -f$d3 -l 300 \
	-n -f$fs3 -l 200 \
	-n -f$g3 -l 200 \
	-n -f$a3 -l 200 \
	-n -f$h3 -l 200 \
	-n -f$g3 -l 200 \
	-n -f$fs3 -l 600 \
	-n -f$fs3 -l 200 \
	-n -f$f3 -l 200 \
	-n -f$cs3 -l 200 \
	-n -f$gs3 -l 200 \
	-n -f$cs3 -l 200 \
	-n -f$h3 -l 200 \
	-n -f$f3 -l 100 \
	-n -f$gs3 -l 100 \
	-n -f$h3 -l 100 \
	-n -f$d4 -l 100 \
	-n -f$f3 -l 100 \
	-n -f$h3 -l 100 \
	-n -f$cs4 -l 600\
	-n -f$h3 -l 100 \
	-n -f$cs4 -l 100 \
	-n -f$h3 -l 100 \
	-n -f$as3 -l 100 \
	-n -f$fs3 -l 400 -D 200
done
