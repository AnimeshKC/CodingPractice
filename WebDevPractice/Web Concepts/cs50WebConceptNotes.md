Letter analogy: 
    Sender and recipient both have an IP address which identifies them. A port number also identifies type, i.e. 80 for HTTP.

DNS coverts domain names to IP addresses.

#
anatomy of an url:
http://www.example.com/

www => subdomain or hostname
example.com => domain
/ => implicitly index.html

http => protocol
HTTP is a protocol for clients and servers.
#

Browser sends a GET request to a server with the HTTP version and the host name being requested.

Form that redirects to google:
```
<form action="https://www.google.com/search" method="get">
<input name="q" type="text">
<input type="submit" value="Search">
```