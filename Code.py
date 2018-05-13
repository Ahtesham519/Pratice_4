
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

total_images,total_labels,train_annotations = get_stats(train_inp)
print("Total Images in the train: ", total_images)
print("Total Labels in the train: ", total_labels)
print("")

total_images, total_labels, test_annotations = get_stats(test_inp)
print("Total Images in the test: " , total_images)
print("Total Labels in the test: ", total_labels)
print("")

total_images, total_labels,valid_annotations = get_Stats(valid_inp)
print("Total Images in the valid: ", total_images)
print("Total labels in the valid: ", total_labels)

train_labels = Counter(train_annotations)

xvalues = list(train_labels.keys())
yvalues = list(train_labels.values())

tracel = go.Bar(x= xvalues, y=yvalues, opacity = 0.8 , name = "year count", marker = dict(color='rgba(20,20,20,1)'))
layout = dict(width=800 , title='Distribution of different labels in the train dataset', legend = dict(orientation = "h"));

fig = go.Figure(data=[trace1], layout = layout);
iplot(fig);


valid_labels = Counter(valid_annotations)

xvalues = list(valid_labels.keys())
yvalues = list(valid_labels.values())

tracel = go.Bar(x = xvalues, y = yvalues , opacity = 0.8 , name= "year count", marker = dict(color = 'rgba(20,20,20,1)'))
layout = dict(width = 800, title='Distributation of different labels in the valid dataset', legend = dict(orientation = "h"));


fig = go.Figure(data = [trace1] , layout = layout);
iplot(fig);


def get_images_for_labels(labellist, data):
  image_ids = []
  for each in data['annotations']:
    if all(x in each [' labelId'] for x in labellist):
      image_ids.append(each['imageId'])
      if len(image_ids) == 2:
        break
image_urls = []
for each in data ['images']:
  if each ['imageId'] in image_ids :
      image_urls.append(each['url'])

      return image_urls
    
    
    
temps = train_labels.most_common(10)
labels_tr = ["Label -" + str(x[0]) for x in temps]
values = [x[1] for x in temps]

tracel = go.Bar(x = labels_tr, y= values, opacity=0.7, name= "year count" , marker = dict(color = 'rgba(120,120,120,0.8)'))
layout = dict(height = 400 , title = 'Top 10 Labels in the train dataset', legend = dict(orientation="h"));

fig = go.Figure(data = [trace], layout = layout);
iplot(fig);

temps = valid_labels.most_common(10)
labels_vl = ["Label-" +str(x[0]) for x in temps]
values = [x[1] for x in temps]

tracel = go.Bar(x=labels_vl, y = values, opacity = 0.7, name = "year count" , marker = dict(color='rgba(120,120,120, 0.8)'))
layout = dict(height=400 , title = 'Top 10 Labels in valid dataset', legend = dict(orientation="h"));

fig = go.Figure(data= [trace1], layout= layout);
iplot(fig);



def cartesian_reduct(alist):
  results = []
  for x in alist:
    for y in alist:
      if x == y:
        continue
      srtd = sorted([int(x), int(y)])
      srtd = "AND ".join([str(x) for in srtd])
      results.append(srtd)
  return results


co_occurance = []
for i , each in enumerate(train_inp['annotations']):
  prod = cartesian_reduct(each ['labelId'])
  co_occurance.extend(prods)
  
  












































