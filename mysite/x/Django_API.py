from books.models import Publisher

p1 = Publisher(name="Libo", address='0352 henganxinqu',
               city='datong', state_province='shanxi',
               country='China', website='http://www.lqr.com/')
p1.save()
p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',
               city='Cambridge', state_province='MA',
               country='U.S.A.',
               website='http://www.oreilly.com/')
p2.save()
p3 = Publisher.objects.create(name='Apress',
                              address='2855 Telegraph Avenue',
                              city='Berkeley', state_province='CA',
                              country='U.S.A.',
                              website='http://www.apress.com/')
publisher_list = Publisher.objects.all()
print publisher_list
print Publisher.objects.filter(name='liqirong')
print Publisher.objects.filter(country='China')
print Publisher.objects.filter(state_province="shanxi", country="China")
print Publisher.objects.filter(name__contains='qirong')
print Publisher.objects.get(name="Apress")

try:
    p = Publisher.objects.get(name="Apress")
except Publisher.DoesNotExist:
    print "Apress isn't in the database yet."
else:
    print 'Apress is in the database.'

print Publisher.objects.filter(country='China').order_by("-name")
print Publisher.objects.order_by('name')[0]
print Publisher.objects.filter(id=3).update(name="Liqirong")
Publisher.objects.filter(name="liqirong").delete()
