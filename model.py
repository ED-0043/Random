import keras

class Model(keras.Model):
    def __init__(self):
        super().__init__()
        self.layer1 = keras.layers.Dense(units=100, activation='elu')
        self.layer2 = keras.layers.Dense(units=100, activation='relu')
        self.layer3 = keras.layers.Dense(units=100, activation='relu')
        self.output = keras.layers.Dense(10, activation='softmax')

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)

        return self.output(x)
