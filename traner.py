import os
import sys
from tudouNLP.models.train import train
trainer=train(task_name='classify',data_dir='datasets',model_dir='tudouNLP/models/model/sentiment_model/model',output_dir='datasets')
trainer()