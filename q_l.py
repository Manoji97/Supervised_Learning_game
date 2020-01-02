import random
import numpy as np
import os
import csv
import tflearn
from tflearn.layers.core import input_data,dropout,fully_connected
from tflearn.layers.estimator import regression
from tflearn.data_utils import load_csv
import ast

train_data = []

def data_to_train(a_x,c_x,t_x,t_y,x_c):
	#a = a_x - t_x
	if x_c == -4:
		out = [1,0,0]
	elif x_c == 0:
		out = [0,1,0]
	else:
		out = [0,0,1]
	train_data.append([a_x,c_x,t_x,t_y,out])


def cvt_train_data_to_csv(train_data):
	with open('mnb_2.csv','w') as f:
		writer = csv.writer(f,lineterminator = '\n')
		for i in train_data:
			x = []
			for j in i:
				x.append(j)
			writer.writerow(x)


def data_prep(file):
	data,lables = load_csv(file,target_column = 3)
	return data,lables


def neural_net():
	net = input_data(shape = [None,4],name = 'inputs')
	net = fully_connected(net,32,activation ='relu')
	net = dropout(net,0.8)
	net = fully_connected(net,64,activation = 'relu')
	net = dropout(net,0.8)
	net = fully_connected(net,32,activation = 'relu')
	net = dropout(net,0.8)
	net = fully_connected(net,3,activation = 'softmax')
	net = regression(net,name = 'targets')
	model = tflearn.DNN(net)

	return model


def train_model(model,data,lables):
	model.fit({'inputs':data},{'targets':lables}, n_epoch=10, batch_size=16, show_metric=True)
	return model


def conv(file):
	d,l = load_csv(file,target_column = 4)
	l = [ast.literal_eval(i) for i in l]
	data = []
	for i in d:
		x = []
		for j in i:
			x.append(ast.literal_eval(j))
		data.append(x)

	train = []
	left = []
	straight = []
	right = []
	for i in range(len(data)):
		if l[i] == [1,0,0]:
			left.append([data[i],l[i]])
		elif l[i] == [0,1,0]:
			straight.append([data[i],l[i]])
		elif l[i] == [0,0,1]:
			right.append([data[i],l[i]])
		else:
			continue
	straight = straight[0:max(len(left),len(right))]
	train = left+straight+right
	data = []
	lables = []
	for i in range(len(train)):
		data.append(train[i][0])
		lables.append(train[i][1])
		
	return data,lables


#data1,lables1 = conv('mnb_0.csv')
#data2,lables2 = conv('mnb_1.csv')
#data3,lables3 = conv('mnb_2.csv')
#data = data1+data2+data3
#lables = lables1+lables2+lables3
#print(len(data3),len(lables3))
#data = np.array(data)
#lables = np.array(lables)
#print(data.shape,lables.shape)


model = neural_net()
#model = train_model(model,data,lables)

#model.save('game.model')

model.load('game.model')

def my_agent(a):
	c = model.predict(a)[0]
	c = c.tolist()
	if c.index(max(c)) == 0:
		x_c = -15
	elif c.index(max(c)) == 1:
		x_c = 0
	else:
		x_c = 15
	return x_c
 
#print(my_agent([[350,50,492,280]]))







