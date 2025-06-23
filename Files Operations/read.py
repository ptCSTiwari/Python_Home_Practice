# without "with" heree need to close the  file
'''r = open("File Operations\\Tiwari.txt", "r")
content = r.read()
print(content)
r.close()'''

#with ke sath
with open("File Operations\\Tiwari.txt", "r") as file:
  content = file.read()
print(content)