from django.template import Context

c = Context({'foo': "bar"})
print c['foo']
del c['foo']
print c['foo']
c['newvariable'] = 'hello'
print c['newvariable']
