import sys
import random

def grab(stdin):

	buf = stdin.readline()
	emails = []
	while buf.strip() != "done":
		if buf.strip() != '':
			emails.append(buf.strip())
		buf = stdin.readline()

	sample = random.sample(emails, 300)
	s = ""
	for email in sample:
		print (email + ',')
	


grab(sys.stdin)