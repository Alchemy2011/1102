from contact.forms import ContactForm

f = ContactForm()
print f
print f.as_ul()
print f.as_p()
print f.as_table()
print f['subject']
print f['message']
f = ContactForm({'subject': 'Hello', 'email': 'lqr@qq.com',
                 'message': 'Nice site!'})
print f.is_bound
print f.is_valid()
f = ContactForm({'subject': 'Hello', 'message': 'Nice site!'})
print f.is_valid()
f = ContactForm({'subject': 'Hello', 'message': ''})
print f.is_valid()
print f['message'].errors
print f['subject'].errors
print f['email'].errors
# f.cleaned_data
