#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

# Get data from query string
form = cgi.FieldStorage()
values = form.getlist('value')

# Add the values together
try:
    total = 0
    for value in values:
        total += int(value)

    body = f"Total: {total}"
except (ValueError, TypeError):
    body = "No data, or bad type.  Please provide integer values in query string."

# Display the content/body
print("Content-type: text/plain")
print("")
print(body)
