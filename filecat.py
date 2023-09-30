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
	excludePaths = []
	if len(sys.argv) > 2:
		excludePaths = [os.path.abspath(fld) for fld in sys.argv[2:]]

	out = csv.writer(open("files.csv", "wt", encoding='utf-8'))

	for root, dirs, files in os.walk(pth):
		print (root, len(dirs), len(files))
		
		match = False
		for ef in excludePaths:
			if root[:len(ef)] == ef:
				match = True
				break
		if match:
			print ("Skipping as requested", root)
			continue
		
		for fi in files:

			fiPth = os.path.join(root, fi)
			if not os.path.exists(fiPth):
				continue # Path is probably too long
			
			try:
				digest = file_digest(open(fiPth, "rb"), "sha1")
			except PermissionError:
				print ("Skipping", fiPth)

			out.writerow((root, fi, os.path.getsize(fiPth), os.path.getmtime(fiPth), digest))
	del out
