#����python��requestģ��(��urllib������)��ֻ����urlopen����
#ѧϰurllib��:https://docs.python.org/3/library/urllib.html
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())