import time as time
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

current_time_tick = time.time()
X, y = make_classification(n_samples=1000, n_features=4,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)

print(clf.predict([[0, 0, 0, 0]]))
program_time_tick = current_time_tick - time.time()
print(program_time_tick)
