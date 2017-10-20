fin=open("running-config.cfg")
def readFile(fin):
    d={}
    for line in fin:
	word=line.split("object")
	print(word)
	d=d.update(word)
    print(d)

readFile(fin)
