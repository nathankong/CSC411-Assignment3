from util import DataTable, ShowImage, Plot2D, LoadData
from preprocess import DoPCA, PlotHistogramOfLabels, DoAutoEncoder


def printSomeLabels(labels, number):
	# labels shape: [num_samples, 1]
	# number: number of labels to print
	i = 0
	for label in labels:
		i += 1
		if i == number+1:
			break
		print label


def dispSomeImages(images, number):
	# images shape: [num_samples, height, width, channels]
	# number: number of images to display
	i = 0
	for image in images:
		i += 1
		if i == number+1:
			break
		ShowImage(image, i)


def main(debug=0):

	dataDir = 'Data/NPZ_data/'
	listOfTrainingSetFiles = ['train_1_1000.npz', 'train_1001_2000.npz', \
							  'train_2001_3000.npz', 'train_3001_4000.npz', \
							  'train_4001_5000.npz', 'train_5001_6000.npz', \
							  'train_6001_7000.npz']

	# Get the distribution of training set labels
	#PlotHistogramOfLabels(dataDir, listOfTrainingSetFiles)

	# Reduce dimensionality
	DoAutoEncoder(dataDir, listOfTrainingSetFiles)


#	# Preprocess
#	lowDimInputs = DoPCA(flatInputs, numComponents=2)
#	print(lowDimInputs.shape)
#
#	colors = ['r', 'y', 'b', 'g', 'm', 'c', 'k', 'w']
#	Plot2D(lowDimInputs, labels, colors, 2)


if __name__ == '__main__':
	main(debug=0)



