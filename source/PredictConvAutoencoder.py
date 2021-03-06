import os
import numpy as np

from core.ConvAutoencoder import ConvAutoEncoder2D
from core.util import save_array, normalize, load_array
import config

if os.path.isdir(config.training_saved_filename):
    X = load_array(config.training_saved_filename)
else:
    raise Exception('You have to run TrainConvAutoencoder to create the data.')

# Predict data
net = ConvAutoEncoder2D(
    config.checkpoint_autoencoder_filename, X.shape[1], X.shape[2], encoding_decoding_choice=config.encoding_decoding_choice)
net.predictModel(X, config.image_sink)
