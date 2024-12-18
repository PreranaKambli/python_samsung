htmlcode ='''
<html>
<body>
<h2> HEllo world </h2>
</body>
</html
'''
file_name = input('Enetr the name of the file')
with open(file_name,'w') as fp:
    fp.write(htmlcode)