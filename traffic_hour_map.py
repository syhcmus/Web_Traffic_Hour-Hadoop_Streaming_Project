#!/usr/bin/env python
import sys
from datetime import datetime

for line in sys.stdin:
	if line[0].isdigit():
		fields = line.strip().split(",")
		dt_log = fields[1][1:]
		dt_log = datetime.strptime(dt_log, "%d/%b/%Y:%H:%M:%S")
		date_log = dt_log.date()
		hour = dt_log.time().hour
		print("%d\t%s" % (hour, date_log))

