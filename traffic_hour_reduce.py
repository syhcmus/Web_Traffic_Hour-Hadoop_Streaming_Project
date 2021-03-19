#!/usr/bin/env python
import sys

(cur_hour, cur_date, num_access, num_date) = (None, None, 0.0, 0)
hour_stats = {}
for line in sys.stdin:
	(hour, date) = line.strip().split("\t")
	hour = int(hour)
	if cur_hour is not None and cur_hour != hour:
		#print("%d\t%.2f" % (cur_hour, float(num_access/num_date)))
		hour_stats[cur_hour] = float(num_access/num_date)
		(cur_date, num_access, num_date) = (None, 0.0 ,0)
	cur_hour = hour
	if cur_date != date:
		cur_date = date
		num_date += 1
	num_access += 1

#print("%s\t%f" % (cur_hour, float(num_access/num_date)))
hour_stats[cur_hour] = float(num_access/num_date)
our_stats = dict(sorted(hour_stats.items(), key= lambda item:item[0]))
for key in hour_stats:
	print("%d\t%.2f" % (key, hour_stats[key]))

