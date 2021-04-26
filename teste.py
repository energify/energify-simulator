import datetime
import dateutil.parser
import isodate

insertion_date = dateutil.parser.parse('2018-03-13T17:22:20Z')
now = dateutil.parser.parse(datetime.datetime.now().replace(microsecond=0).isoformat()+str('Z'))
diff = now - insertion_date

oi = isodate.parse_duration('PT15M')

if diff < oi:
    print("OLA")

print(diff)


