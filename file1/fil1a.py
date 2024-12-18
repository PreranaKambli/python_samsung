htmlcode ='''
<html>
<body>
<h2>Name:  prerana
    USN:2KE23CS101</h2>
</body>
</html
'''
file_name = input('Enetr the name of the file')
with open(file_name,'w') as fp:
    fp.write(htmlcode)