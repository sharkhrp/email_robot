import email_1

from  csv_1 import name, project, email

content = "..."

for n, p, e in zip(name, project, email):

    content = content.replace("[name]", n)

    content = content.replace("[Project]", p)

    email_1.send(email, content)
