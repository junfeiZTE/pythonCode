import re
p1="cat"
p2="bird"
string="dog runs to cat"

print(p1 in string)
print(p2 in string)


print(re.search(p1,string))
print(re.search(p2,string))

print(re.search(r"r[au]n",string))


print(re.search(r"r[0-9]n",string))

print(re.search(r"r\dn","run r4n"))
print(re.search(r"n\sr","run r4n"))


print(re.search(r"r\wn","run r4n"))


print(re.search(r"\Brun\B"," run r4n"))

print(re.search(r"run\\"," run\ r4n"))

print(re.search(r"r.n"," run r4n"))

print(re.search(r"^dog","dog runs to cat"))
print(re.search(r"cat$","dog runs to cat"))

print(re.search(r"Mon(day)?","Monday"))

string="""
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I",string,flags=re.M))

print(re.search(r"ab*","a"))
print(re.search(r"ab*","abbbbbbbbb"))

print(re.search(r"ab+","a"))
print(re.search(r"ab+","abbbbbbbbb"))

print(re.search(r"ab{2,10}","a"))
print(re.search(r"ab{2,10}","abbbbbbbbb"))

match=re.search(r"(\d+), Date: (.+)","ID: 021, Date: Feb/12/2017")
print(match.group())
print(match.group(1))
print(match.group(2))

match=re.search(r"(?P<id>\d+), Date: (?P<date>.+)","ID: 021, Date: Feb/12/2017")
print(match.group())
print(match.group('id'))
print(match.group('date'))

print(re.findall(r"r[ua]n","run ran ren"))

print(re.sub(r"r[au]ns","catches","dog runs to cat"))

print(re.split(r"[,;\.]","a;b.c,d;e"))

compiled_re=re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))
