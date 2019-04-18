# Turns Standord Dog Dataset http://vision.stanford.edu/aditya86/ImageNetDogs/
# into csv file for labels and ids

import os
import xml.etree.ElementTree
import pandas as pd

annotations_root_dir = os.path.join('Data', 'Annotation')

if __name__ =='__main__':

	ids = []
	breeds = []

	for item in os.listdir(annotations_root_dir):
		breed = item.split('-')[1].lower()
		for file in os.listdir(os.path.join(annotations_root_dir, item)):
			ids.append(file)
			breeds.append(breed)	

	df = pd.DataFrame({'id':ids, 'breed':breeds})
	df = df.sample(frac=1).reset_index(drop=True)
	df.to_csv('labels.csv')