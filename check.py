f = open("/root/task3/mnist.py", "r")
check_code = f.read()

if 'keras' and 'Convolution2D' and 'MaxPooling2D' and 'Sequential' in check_code:				
	print('CNN_code')
elif 'sklearn' and 'numpy' in check_code:
	print('ML_code')
else:
	print("None")