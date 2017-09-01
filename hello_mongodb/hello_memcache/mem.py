import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=True)
r1 = mc.add('python', 'lqr')
print(r1)
