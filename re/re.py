import re
 
line = "Cats are smarter than dogs \ntcccsac"
print(line)
matchObj = re.findall( '\S+ar\S+',line)
b = re.match( '^Cat.*c$',line,re.S)
print(b)
