import os

d = {}
with open("geneId_key.txt") as file:
    next(file)
    for line in file:
        (key, value) = line.split()
        d[(key)] = value
#print (d)
f1 = open('genelist.txt','r')
content = f1.read()
f = content.split()
f1.close()
#print (f)
for key, value in d.items():
    def translation_id(f,d):
        new_list = []
        for x in f:
            entrez = d.get(x)
            new_list.append(entrez)
        return new_list 
        
new_list= translation_id(f,d)
for item in new_list:
  with open ('results.txt','w') as f2:
      print("Symbols for the given ids\n", *new_list, sep='\n', file=f2)
print("Results written to a new file")
