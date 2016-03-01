from os import listdir
from os.path import isfile,join
from gabil import  AttributeBinaryStream


def trainDatasetsInDir(dataset_directory):

	for index,file_name in enumerate(listdir(dataset_directory)):
		print "%s)=============================================================" %(index+1)
		print "Training network from dataset: %s" %(file_name)
		data_file = join(dataset_directory,file_name)
		if not isfile(data_file): continue

		with open(data_file,'r+') as dataset:
			data = dataset.readlines()
			for entry in data:
				(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,classification) = entry.split(',')

if __name__ == '__main__':
	A1BinaryStream = AttributeBinaryStream(['b','a'])
	A4BinaryStream = AttributeBinaryStream(['u','y','l','t'])
	A5BinaryStream = AttributeBinaryStream(['g','p','gg']) 
	A6BinaryStream = AttributeBinaryStream(['c','d','cc','i','j','k','m','r','q','w','x','e','aa','ff'])
	A7BinaryStream = AttributeBinaryStream(['v','h','bb','j','n','z','dd','ff','o'])
	A9BinaryStream = AttributeBinaryStream(['t','f'])
	A10BinaryStream = AttributeBinaryStream(['t','f']) 
	A12BinaryStream = AttributeBinaryStream(['t','f'])
	A13BinaryStream = AttributeBinaryStream(['g','p','s'])
	ClassificationBinaryStream = AttributeBinaryStream(['+','-'])

	binaryStreams = [A1BinaryStream,A4BinaryStream,A6BinaryStream,A7BinaryStream,A9BinaryStream,
					A10BinaryStream,A12BinaryStream,A13BinaryStream,ClassificationBinaryStream]

	for binaryStream in binaryStreams:
		binaryStream.computeBinaryStream()
	ClassificationBinaryStream.printBinaryStream() 




	datasets_dir = 'datasets'
	trainDatasetsInDir(datasets_dir)
