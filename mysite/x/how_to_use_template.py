from django import template

t = template.Template("My name is {{ name }}.")
c = template.Context({"name": "liqirong"})
print(t.render(c))
c = template.Context({"name": "libo"})
print(t.render(c))
