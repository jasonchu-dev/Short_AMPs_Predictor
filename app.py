from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
from explainerdashboard.datasets import titanic_survive, feature_descriptions
import joblib

model = joblib.load("./model.joblib")

explainer = ClassifierExplainer(model, X_test, y_test,
                                cats=['Sex', 'Deck', 'Embarked'],
                                descriptions=feature_descriptions,
                                labels=['Negative', 'Positive'])

ExplainerDashboard(explainer).run()