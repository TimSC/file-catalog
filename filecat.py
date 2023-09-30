import os
import hashlib
import csv
import sys

def file_digest(fi, hashfunc):

	data = None
	h = hashlib.new('sha1')

	while True:
		data = fi.read(1024*1024)
		h.update(data)
		if len(data) == 0:
			break

	return h.hexdigest()

if __name__=="__main__":

	pth = "."
	if len(sys.argv) > 1:
		pth = sys.argv[1]

	out = csv.writer(open("files.csv", "wt"))

	for root, dirs, files in os.walk(pth):
		print (root, len(dirs), len(files))
		
		for fi in files:

			fiPth = os.path.join(root, fi)
			digest = file_digest(open(fiPth, "rb"), "sha1")

			out.writerow((root, fi, os.path.getsize(fiPth), os.path.getmtime(fiPth), digest))
	del out
