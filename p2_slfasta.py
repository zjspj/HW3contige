import sys

def main():
	commands = [int(i) for i in sys.argv[2:]]
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
	for i in commands:
		if i> len(cklist)-1 or i<1:
			print("number " + str(i) + " is not within the contig count, the total count of contig in the fasta file is " + str(len(cklist)-1))
		else:
			masterfile.seek(cklist[i-1])
			position = masterfile.tell()
			first_line = masterfile.readline()
			firstline = first_line.strip("\n")
			subfilename = str(i) + first_line[1:-1] + ".fasta"
			subfile = open(subfilename, "w")
			text = ""
			while position <= cklist[i] and position != masterend:
				line = masterfile.readline()
				line = line.strip("\n")
				position = masterfile.tell()
				text += line
			subfile.write(first_line + "\n" + text)
			subfile.close()
main()
