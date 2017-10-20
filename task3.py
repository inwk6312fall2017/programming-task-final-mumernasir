fin=open("running-config.cfg")
for line in fin:
	line=line.replace("172","192")
	print(line)
