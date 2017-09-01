from django.template import Template, Context

t = Template("Hello, {{ person_name }}")
for name in ('liqirong', 'libo', 'lqr'):
    print t.render(Context({'person_name': name}))
