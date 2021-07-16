model = tf.keras.sequential([
tf.keras.flatten(),
tf.keras.layers.Dense(40, activation=“elu”),
tf.keras.layers.Dense(20), tf.keras.layers.Dense(10),
tf.keras.layers.Dense(20)
tf.keras.layers.Dense(40)
])
model.compile(loss=“bce”,optimizer=“ADAM”,metrics=[“accuracy”])