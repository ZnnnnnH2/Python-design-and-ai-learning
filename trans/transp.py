with open(r"C:\Users\ZnH2\PycharmProjects\python_and_ai\trans\in.txt","r",encoding="utf-8") as f:
	out = open("out.txt", "w", encoding="utf-8")
	for line in f:
		out.write(">"+line)

	out.close()