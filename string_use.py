import time

str_finished = "*"
str_under_finish = "."
print("\r------Start------", end="")
time.sleep(1)
for i in range(10, 100, 10):
	k = i // 10
	str1 = str_finished * k
	str2 = str_under_finish * (10 - k)
	str3 = "[{0}->{1}]".format(str1, str2)
	str4 = "\r%{0:2} :{1}".format(i, str3) # \r is carriage return
	print(str4, end="")
	time.sleep(1)
print("\r------End------")