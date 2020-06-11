f = open("/root/task3/mnist.py", "r")
contents = f.readlines()
f.close()
#counts convolutional layers
conv_count =0
for x in contents:
	if x == "model.add(Conv2D(8,kernel_size=(3,3),activation='relu')) \n":
		conv_count = conv_count+1 
#prints convolutional layers added		
print("No. of Convolutional layers added = ",conv_count)
#counts hidden layers
hidden_count =0
for x in contents:
	if x == "model.add(Dense(8, activation='sigmoid'))\n":
		hidden_count = hidden_count+1 
#prints hidden layers added
print("No. of Hidden layers added = ",hidden_count)
#adds convolution, pooling, dense layers and increases epochs
if conv_count < 2:
	print("Adding Convolutional layers")	
	contents.insert(36, "model.add(Conv2D(8,kernel_size=(3,3),activation='relu')) \n")
	contents.insert(37, "model.add(Conv2D(8,kernel_size=(3,3),activation='relu')) \n")
	print("Adding Pooling layers")
	contents.insert(38, "model.add(MaxPooling2D(pool_size=(2, 2))) \n")
	print("Increasing no. of Epochs")
	num = int(contents[57][9])
	num = num + 2
	str_num = str(num)
	contents[57] = "epochs = "+str_num+"\n"
	print(contents[57])
	f = open("/root/task3/mnist.py", "w")
	contents = "".join(contents)
	f.write(contents)
	f.close()
elif conv_count == 2:
	print("Sufficient Convolution layers are added.")
	if hidden_count < 2:
		print("Adding Hidden layers")
		contents.insert(43, "model.add(Dense(8, activation='relu'))\n")
		contents.insert(44, "model.add(Dense(8, activation='relu'))\n")
		print("Increasing no. of Epochs")
		num = int(contents[59][9])
		num = num + 2
		str_num = str(num)
		contents[59] = "epochs = "+str_num+"\n"
		print(contents[59])
		f = open("/root/task3/mnist.py", "w")
		contents = "".join(contents)
		f.write(contents)
		f.close()
	elif hidden_count == 2:
		print("Sufficient Hidden layers are added.")
		print("Increasing no. of Epochs")
		num = int(contents[59][9])
		num = num + 2
		str_num = str(num)
		contents[59] = "epochs = "+str_num+"\n"
		print(contents[59])
		f = open("/root/task3/mnist.py", "w")
		contents = "".join(contents)
		f.write(contents)
		f.close()
else:
	print("Close the program")