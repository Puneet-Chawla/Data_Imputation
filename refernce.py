from sklearn.preprocessing import Imputer
import numpy as np


list = np.array([[23.56],[53.45],['NaN'],[44.44],[77.78],['NaN'],[234.44],[11.33],[79.87]])

print (list)

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
a = imp.fit_transform(list)

print (a)