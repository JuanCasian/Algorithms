import pickle
import numpy as np
from scipy.stats import mode


class NearestNeighbor:
	def __init__(self):
		pass

	def import_data(self, data_folder, batch_id):
		with open(data_folder + '/data_batch_' + str(batch_id), mode='rb') as file:
			batch = pickle.load(file, encoding='latin1')
		return batch['data'], batch['labels']
	
	def train(self, data_folder, batch_id):
		X, y = self.import_data(data_folder, batch_id)
		self.Xtr = np.array(X)
		self.ytr = np.array(y)
	
	def predict(self, X, k):
		num_test = X.shape[0]
		Ypred = np.zeros(num_test, dtype = self.ytr.dtype)
		for i in range(num_test):
			min_indexes = []
			distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
			min_indexes.append(np.argsort(distances)[:k])
			best_labels = []
			for j in range(len(min_indexes)):
				best_labels.append(self.ytr[min_indexes[j]])
			best_label = mode(best_labels, axis = None)[0][0]
			Ypred[i] = best_label
		return Ypred
		

	def evaluate(self, n, k):
		with open("./data/test_batch", mode='rb') as file:
			batch = pickle.load(file, encoding='latin1')
		X = batch["data"][:n]
		real = np.array(batch["labels"][:n])
		predictions = self.predict(X, k)
		accuracy = 0
		print(real)
		print(predictions)
		for i in range(n):
			if (predictions[i] == real[i]):
				accuracy += 1
		accuracy = accuracy / n * 100
		print("Accuracy = {}%".format(accuracy))

		
		


def main():
	classifier = NearestNeighbor()
	classifier.train("./data", 1)
	for i in range(1,10):
		print("Evaluating accuracy with k value of: {}".format(i))
		classifier.evaluate(128, i)



if __name__ == "__main__":
	main()