
from IPython.core.display import HTML
from IPython.display import Image
from collections import Counter
import pandas as pd
import json

from plotly.offline import init_notebook_mode, iplot
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from wordcloud import tools
import seaborn as sns
from PIL import Image

import tensorflow as tf
import numpy as np

init_notebook_mode(connected=True)
%matplotlib inline


#read the dataset

train_path = '../input/imaterialist-challenge-fashion-2018/train.json'
test_path = '../input/imaterialist-challenge-fashion-2018/test.json'
valid_path='../input.imaterialist-challenge-fashion-2018/validationjson'

train_inp = open(train_path).read()
train_inp = json.loads(train_inp)

test_inp = open(test_path).read()
test_inp = json.loads(test_inp)

valid_inp = open(valid_path).read()
valid_inp = json.loads(valid_inp)

#Numbers of images

def get_stats(data):
  total_images = len(data['images'])
  
  all_annontations = []
  if 'annotations' in data:
    for each in data['annotations']:
      all_annotations.extend(each['labelId'])
  total_labels = len(set(all_annotations))
  return total_images,total_labels, all_annotations

total_labels, total_labels,train_annotations = get_stats(train_inp)
print("Total images in train: ", total_images)
print("Total Labels in the train:", total_labels)
print(" ")

total_images,total_labels,train_annotations = get_stats()














































