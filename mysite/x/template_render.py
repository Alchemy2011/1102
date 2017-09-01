from django.template import Template, Context
import datetime
raw_template = """<p>Dear {{ person_name }},</p>
<p>Thanks for placing an order from {{ company }}. It's scheduled to
    ship on {{ ship_date|date:"F j, Y" }}</p>
<p>Here are the items you've ordered:</p>
<ul>
    {% for item in item_list %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
{% if ordered_warranty %}
    <p>Your warranty information will be included in the packaging.</p>
{% else %}
    <p>You didn't order a warranty, so you're on your own when
        the products inevitably stop working.</p>
{% endif %}
<p>Sincerely,<br/>{{ conpany }}</p>
"""
t = Template(raw_template)
c = Context({'person_name': 'liqirong',
            'company': 'python',
             'ship_date': datetime.date(2017, 8, 4),
             'ordered_warranty': False})
print t.render(c)
