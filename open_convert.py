import re
file = open('convertedtext.txt', 'w')
input = open('C:/Users/j.hung/Desktop/chapter_0100_introduction.xml', 'r')
o = input.read()


o = re.compile(r'^\s+', re.MULTILINE).sub('', o)

o = re.compile(r'<eq\s+label\s*=\s*"(\w+)"\s*>\s*(.*)\s*</eq>').sub(
r'''
.. math::
     :label: \1

     \2
''', o
)

o = re.compile(r'<eq>').sub(
r'''
.. math::''', o
)

o = re.compile(r'</eq>').sub('', o)
o = re.compile(r'<f>(.*?)</f>').sub(r':math:`\1`', o)
o = re.compile(r'<e>(.*?)</e>').sub(r'*\1*', o)
o = re.compile(r'<p>').sub('', o)
o = re.compile(r'</p>', re.MULTILINE).sub(
r'''

''', o)



print o

file.write(o)
