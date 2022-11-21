import pickle
import requests

iris_data_set = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(iris_data_set)