with open("in.txt", encoding="utf-8") as file:
	out = open("out.txt", "w", encoding="utf-8")
	for line in file:
		if line == '\n' or line == '  \n':
			continue
		if line[0] != '*' and line[0] != "▍":
			line = '    '+line
		else:
			line = '\n'+line
		out.write(line)
	out.close()