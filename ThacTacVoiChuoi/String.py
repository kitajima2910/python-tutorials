str = '  Phạm Xuân Hoài  '
str1 = '#$'

print(str.upper())
print(str.lower())

print(str.rjust(20, '*'))
print(str.ljust(20, '*'))
print(str.center(100, '$'))
print(str.__len__())
print(len(str))
print(str)
print(str1.strip('$'))

print(str1.startswith('#'))
print(str1.startswith('$'))
print(str1.endswith('#'))
print(str1.endswith('$'))