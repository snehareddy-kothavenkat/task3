f = open("/root/task3/mnist.py", "r")
contents = f.readlines()
f.close()

conv_count =0
for x in contents:
	if x == "model.add(Conv2D(8,kernel_size=(3,3),activation='relu')) \n":
		conv_count = conv_count+1 
			
print(conv_count)

hidden_count =0
for x in contents:
	if x == "model.add(Dense(8, activation='sigmoid'))\n":
		hidden_count = hidden_count+1 

print(hidden_count)

if conv_count < 2:
	print("Add a Convolutional layer")	
	contents.insert(39, "model.add(Conv2D(8,kernel_size=(3,3),activation='relu')) \n")
	contents.insert(40, "model.add(Conv2D(8,kernel_size=(3,3),activation='relu')) \n")
	contents.insert(41, "model.add(MaxPooling2D(pool_size=(2, 2))) \n")
	num = int(contents[60][9])
	num = num + 2
	str_num = str(num)
	contents[60] = "epochs = "+str_num+"\n"
	print(contents[60])
	f = open("/root/task3/mnist.py", "w")
	contents = "".join(contents)
	f.write(contents)
	f.close()
elif conv_count == 2:
	print("Convolution layers are correct")
	if hidden_count < 2:
		print("Add a Hidden layer")
		contents.insert(46, "model.add(Dense(8, activation='relu'))\n")
		contents.insert(47, "model.add(Dense(8, activation='relu'))\n")
		num = int(contents[62][9])
		num = num + 2
		str_num = str(num)
		contents[62] = "epochs = "+str_num+"\n"
		print(contents[62])
		f = open("/root/task3/mnist.py", "w")
		contents = "".join(contents)
		f.write(contents)
		f.close()
	elif hidden_count == 2:
		print("Hidden layers are correct")
		print("Increase Epochs")
		num = int(contents[62][9])
		num = num + 2
		str_num = str(num)
		contents[62] = "epochs = "+str_num+"\n"
		print(contents[62])
		f = open("/root/task3/mnist.py", "w")
		contents = "".join(contents)
		f.write(contents)
		f.close()
else:
	print("Close the program")
