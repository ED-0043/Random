from keras.models import Sequential, Model
from keras.layers import Dense, Input, concatenate
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

class Model(Sequential):
    def __init__(self):
        self.model = Sequential()
        self.build()

    def build(self):
        self.model.add(Dense())
        self.model.add(Dense())

    def compiler(self):
        self.model.compile(optimizer='adam', loss='mse')

    def summarize(self):
        self.model.summary()

hmm = Model()

class Functionality(Model):
    def __init__(self):
        self.in1 = Input()
        self.layerA1 = Dense(100, activation='relu', )(self.in1)
        self.layerA2 = Dense(100, activation='relu', )(self.layerA1)
        self.in2 = Input()
        self.layerB1 = Dense(50, activation='relu', )(self.in2)
        self.layerB2 = Dense(25, activation='relu', )(self.layerB1)
        self.model = concatenate([self.layerA2, self.layerB2])
    # cant tell what im supposed to do next, but will revisit this
        