from keras.models import Sequential
from keras.layers import Dense
# from keras.

class Predator(Sequential):
    def __init__(self):
        self.layer_one  = Dense(100, input_shape=(4, ), activation='linear')
        self.layer_two = Dense(75, activation='relu')
        self.layer_three = Dense(30, activation='relu')
        self.output = Dense(1)

    def forward(self, value):
        x = self.layer_one(value)
        x = self.layer_two(x)
        x = self.layer_three(x)        
        return self.output(x)
    
pred = Predator()
pred.predict()

# UNDERSTAND HOW TO IMPLEMENT A MODEL WITH KERAS AND PYTORCH