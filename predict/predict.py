from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt
import glob

def linear_model(X_train, X_test, y_train, y_test):
	regressor = LinearRegression()
	regressor.fit(X_train,y_train)

	# score for accuracy
	print("Linear Model Score: ", regressor.score(X_test, y_test))

def rand_forest(X_train, X_test, y_train, y_test):
	rf = RandomForestRegressor(n_estimators=500, oob_score=True,random_state=42)
	rf.fit(X_train, y_train)

	print("Random Forest Score: ", rf.score(X_test, y_test))

# for all offenses
data = pd.read_csv('../data/num_all_offenses.csv')
X = data.loc[:,'min_temperature':'precipitation']
y = data['num_crimes']

# PCA
X = StandardScaler().fit_transform(X)
pca = PCA(0.95)
princip_comps = pca.fit_transform(X)

print('Num components: ', pca.n_components_)

X = pd.DataFrame(data=princip_comps)
#print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

linear_model(X_train, X_test, y_train, y_test)
rand_forest(X_train, X_test, y_train, y_test)

#data.describe()

#for data_file in glob.glob("../data/categories/*"):
#	print('For ', data_file)
#	data = pd.read_csv(data_file)	
#	X = data.loc[:,'min_temperature':'precipitation']
#	y = data['num_crimes']
#	
#	# PCA
#	X = StandardScaler().fit_transform(X)
#	pca = PCA(0.95)
#	princip_comps = pca.fit_transform(X)
#	
#	print('Num components: ', pca.n_components_)
#	
#	X = pd.DataFrame(data=princip_comps)
#	#print(X)
#	
#	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#	
#	linear_model(X_train, X_test, y_train, y_test)
#	rand_forest(X_train, X_test, y_train, y_test)
#	print('')
