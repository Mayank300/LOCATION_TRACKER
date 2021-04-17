import pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('47.41.29.122')
for key, val in res.items():
    print('%s : %s' % (key, val))
