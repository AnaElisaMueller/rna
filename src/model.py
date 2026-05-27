from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
from tensorflow.keras.metrics import Recall

def criar_modelo(
    input_dim,
    neuronios_camadas,
    activation='relu',
    output_activation='sigmoid',
    learning_rate=0.001,
    optimizer_name='adam',
    loss='binary_crossentropy',
    metrics=None,
    dropout_rate=0.0
):

    model = Sequential()

    
    model.add(Dense(
        units=neuronios_camadas[0],
        activation=activation,
        input_dim=input_dim
    ))

    # Dropout opcional
    if dropout_rate > 0:
        model.add(Dropout(dropout_rate))

    for neuronios in neuronios_camadas[1:]:

        model.add(Dense(
            units=neuronios,
            activation=activation
        ))

        if dropout_rate > 0:
            model.add(Dropout(dropout_rate))


    model.add(Dense(
        units=1,
        activation=output_activation
    ))


    if optimizer_name.lower() == 'adam':
        optimizer = Adam(
            learning_rate=learning_rate
        )

    elif optimizer_name.lower() == 'sgd':
        optimizer = SGD(
            learning_rate=learning_rate
        )

    elif optimizer_name.lower() == 'rmsprop':
        optimizer = RMSprop(
            learning_rate=learning_rate
        )

    else:
        raise ValueError(
            "Otimizador inválido. Use: 'adam', 'sgd' ou 'rmsprop'."
        )

    if metrics is None:
        metrics = [Recall(name='recall')]

    model.compile(
        optimizer=optimizer,
        loss=loss,
        metrics=metrics
    )

    return model
