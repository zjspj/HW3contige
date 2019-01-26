import sys

def main():
	filename = sys.argv[1]
	masterfile = open(filename)
	masterfile.seek(0,2)
	masterend = masterfile.tell()
	masterfile.seek(0)
	cklist = []
	in_pro = True
	while in_pro:
		line = masterfile.readline()
		if  line == "" and masterfile.tell() == masterend:
			in_pro = False
		else:
			if line[0] == ">":
				cklist.append(masterfile.tell()-len(line))
	cklist.append(masterend)
	masterfile.seek(0)
	for i in range(len(cklist)-1):
		masterfile.seek(cklist[i])
		position = masterfile.tell()
		first_line = masterfile.readline()
		firstline = first_line.strip("\n")
		subfilename = str(i+1) + first_line[1:-1] + ".fasta"
		subfile = open(subfilename, "w")
		text = ""
		while position <= cklist[i+1] and position != masterend:
			line = masterfile.readline()
			line = line.strip("\n")
			position = masterfile.tell()
			text += line
		subfile.write(first_line + "\n" + text)
		subfile.close()
main()
