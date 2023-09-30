import csv
import sys

def ReadFileList(fina):

	fi = csv.reader(open(fina, "rt", encoding='utf-8'))
	hashDict = {}

	for li in fi:

		pth = li[0]
		fn = li[1]
		si = int(li[2])
		modTime = float(li[3])
		ha = li[4]
		data = (pth, fn, si, modTime)

		if ha not in hashDict:
			hashDict[ha] = []
		hashDict[ha].append(data)

	return hashDict

def MergeHashDicts(*hashDicts):
	
	out = {}
	
	for hd in hashDicts:
		for ha, data in hd.items():
			if ha not in out:
				out[ha] = []
			out[ha].extend(data)
			
	return out	
	
if __name__=="__main__":
	
	existingFi = sys.argv[1]
	existingFileData = ReadFileList(existingFi)

	inpFiles = sys.argv[2:]
	inpFileDataList = []
	for inpFile in inpFiles:
		inpFileDataList.append(ReadFileList(inpFile))
	inpFileData = MergeHashDicts(*inpFileDataList)

	for existingHash, existingData in existingFileData.items():
		
		if existingHash in inpFileData:
			print (existingData, "exists", inpFileData[existingHash][0])
		else:
			print (existingData, "not found")

