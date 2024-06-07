# performing unittest
import unittest
import pandas as pd

from random import shuffle
from sklearn.linear_model import LinearRegression

data = pd.read_csv()

xtrain = data.drop()
xtest = shuffle(xtrain[300, :], random=4.54)
ytrain = data[None].values

model = LinearRegression()

class NewTest(unittest.TestCase):
    def setup(self):
        self.model = model
        self.xtest = xtest

    def test_data_output_shape(self):
        y_pred = self.model.predict(self.xtest)
        self.assertEqual(y_pred.shape, self.xtest.shape[0])

    def test_input(self):
        for input in xtest:
            for value in input:
                self.assertIn(value, [0, 500])

# using feast to store features
from feast import Field, Entity, ValueType, FeatureStore
from feast.data_source import FileSource

patient = Entity(name='patient', join_keys=['patient_id'])
chol = Field(name='chol', dtype=Float32)
age = Field(name='age', dtype=Int32)

data_source = FileSource(path="/path to csv",
                         event_timestamp_column='event_timestamp',
                         created_timestamp_column='created')
# -- creating a feature-view
heartd_fv = FeatureView(name='heart_d', 
                        entities=['patient_id'], 
                        schema=[cholesterol, ...],
                        ttl=timedelta(days=1),
                        input=data_source)

#register and store the features
store = FeatureStore(repo_path=".")
store.apply([patient, heartd_fv])

# logging with python
import logging
import matplotlib.pyplot as plt

logging.basicConfig(filename='predictions.log', level=logging.INFO)

for i in range(xtest.shape[0]):
    instance = xtest[1, :].reshape(1, -1)
    prediction = model.predict(instance)
    logging.info(f"inst. {i} - Predclass: {prediction[0]}, Realclass: {ytest[i]}")

with open(logfile, 'r') as f:
    lines = f.readlines()
    predicted_classes = [int(line.split("predicted class: ")[1].split(",")[0]) for line in lines]

# data drift test
from scipy.stats import ks_2samp

sample1, sample2 = training_data, inference_sample

test_statistics, p_value = ks_2samp(sample1, sample2)
if p_value < 0.05:
    print("reject null hypothesis, data might be drifting")
else:
    print('samples are likely from the same dataset ')