lines_seen = set() # holds lines already seen
with open("secondevolfin.txt", "w") as output_file:
	for each_line in open("secondevol.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)