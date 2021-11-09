import hashlib

string = "@DBApp"

for i in range(100000,999999):
	s = str(i)+string
	x = hashlib.sha1(s.encode())
	cnt = x.hexdigest()
	if "6e32d0943418c2c33385bc35a1470250dd8923a9" == cnt:
		print(str(i)+string)
