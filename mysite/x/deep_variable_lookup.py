from django.template import Template, Context
import datetime

person = {'name': 'liqirong', 'age': '28'}
t = Template('{{ person.name }} is {{ person.age }} years old.')
c = Context({'person': person})
print t.render(c)

d = datetime.date(2017, 8, 4)
print d.year
print d.month
print d.day
t = Template('The month is {{ date.month }} and the year is {{ date.year }}.')
c = Context({'date': d})
print t.render(c)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name


t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.')
c = Context({'person': Person('li', 'qirong')})
print t.render(c)

t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
print t.render(Context({'var': 'hello'}))

t = Template('Item 2 is {{ items.2 }}.')
c = Context({'items': ['apples', 'bananas', 'carrots']})
print t.render(c)

person = {'name': 'liqirong', 'age': '28'}
t = Template('{{ person.name.upper }} is {{ person.age }} years old.')
c = Context({'person': person})
print t.render(c)
