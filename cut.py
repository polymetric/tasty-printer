from escpos.printer import Serial
p=Serial(devfile='/dev/ttyS3')
p.cut()
