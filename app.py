from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
from explainerdashboard.datasets import titanic_survive, feature_descriptions
import pandas as pd
import joblib

model = joblib.load("./model.joblib")

X_test = pd.read_csv('static/X_test.csv')
y_test = pd.read_csv('static/y_test.csv')
y_test = y_test['y']

explainer = ClassifierExplainer(model, X_test, y_test,
                                cats=['AAC_K', 'AAC_D', 'AAC_E'],
                                descriptions=feature_descriptions,
                                labels=['Negative', 'Positive'])

ExplainerDashboard(explainer).run()