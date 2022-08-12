import webbrowser
from googlesearch import search

webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
for i in search(query="Python", tld="co.in", start=10, stop=10, pause=2):
    print(i)
