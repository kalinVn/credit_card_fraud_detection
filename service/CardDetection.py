import pandas as pd
import numpy as np
import config

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from factory.Classifier import Classifier




class CardDetection:

    def __init__(self):
        self.standard_data = None
        self.x = None
        self.y = None
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.legit = None
        self.fraud = None
        self.legit_simple = None
        self.new_dataset = None

        csv_path = config.CSV_PATH
        self.dataset = pd.read_csv(csv_path)

        self.scaler = StandardScaler()
        self.classifier_factory = Classifier()
        self.model = self.classifier_factory.get_model()
        print(self.model)

    def standardize_data(self):
        self.legit = self.dataset[self.dataset.Class == 0]
        self.fraud = self.dataset[self.dataset.Class == 1]
        self.legit_simple = self.legit.sample(n=492)
        self.new_dataset = pd.concat([self.legit_simple, self.fraud])
        self.x = self.new_dataset.drop(columns='Class', axis=1)
        self.y = self.new_dataset['Class']

    def build(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2,
                                                                                stratify=self.y, random_state=2)
        self.model.fit(self.x, self.y)

    def test_accuracy_score(self):
        x_train_prediction = self.model.predict(self.x_train)
        training_data_accuracy = accuracy_score(x_train_prediction, self.y_train)
        print("Accuracy on training data: ", training_data_accuracy)

        x_test_prediction = self.model.predict(self.x_test)
        test_data_accuracy = accuracy_score(x_test_prediction, self.y_test)
        print("Accuracy on test data: ", test_data_accuracy)

    def predict(self, data):
        inputs = np.array([data])
        columns = list(self.dataset.columns)[:-1]
        df = pd.DataFrame(inputs, columns=columns)

        prediction = self.model.predict(df)

        if prediction[0] == 0:
            print('Transaction is legit')
        else:
            print('Transaction is fraud')
