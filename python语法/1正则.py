# -*- coding:UTF-8 -*-
#python ������ʽѧϰ
#�ο�:http://www.runoob.com/regexp/regexp-syntax.html    (main)
#�ο���http://www.runoob.com/python/python-reg-expressions.html
#�ο���http://www.jb51.net/article/65286.htm
#�ο�: http://www.jb51.net/article/50511.htm


import re
import sys
type = sys.getfilesystemencoding()

print (re.match('www', 'www.runoob.com').span()) #����.span()�᷵��һֱ��ַ
print (re.match('runoob', 'www.runoob.com'))

 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"


print(re.search('www', 'www.runoob.com').span())  # ����ʼλ��ƥ��
print(re.search('com', 'www.runoob.com').span())         # ������ʼλ��ƥ��


phone = "2004-959-559 # ����һ������绰����"
 
# ɾ���ַ����е� Pythonע�� 
num = re.sub(r'#.*$', "", phone) #��Ԫ���ţ�ƥ��һ���ַ����Ľ�β�����ַ��������Ļ��з�
print "�绰������: ", num
 
# ɾ��������(-)���ַ��� 
num = re.sub(r'\D', "", phone) #\D ������
print "�绰������ : ", num

stringTmp = 'c1212'
items = re.findall(r'[1-9][2-9{0, 1}]', stringTmp)
for item in items:
        print item[0]


test = "<span>�������⻻kindle�����飬���ն��������衣"
print test
if sys.version_info < (3, 4):  #python �ж� :https://segmentfault.com/q/1010000000127878
        pattern = re.compile('[\x80-\xff]+')
else:
        pattern = re.compile('[\u4e00-\u9fa5]+')
items = re.findall(pattern,test)
for item in items:
        print item
        