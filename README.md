# task3

PROBLEM STATEMENT
Creation of docker container image that has python3 installed with all essential libraries like keras , numpy , pandas, tensorflow, etc  required for training ML CNN(Convolutional Neural Network) model. 

On launching image, execution of the trained ML model takes place.

Creating required number of jobs in jenkins to test, notify, train , tweak , retrain and monitor the ML model to get desired accuracy.



WORKFLOW/ALGORITHM OF THE TASK
Pull the code from GitHub. 
Execute relevant model accordingly .
Check for desired accuracy if less tweak the model and go to step 2 else go go step 4.
On achieving the desired accuracy notify the developer through mail .
Monitor the containers from crashing during the entire task.


DESCRIPTION OF THE TASK
1. Create docker container image using python3 and installing necessary libraries  by using the docker file.

2. We will launch this image that automatically trains the desired ML model and achieve targeted accuracy using jenkins jobs.

3. The jenkins jobs are as follows using which we build a pipeline ml that helps in continuous integration and deployment

DETAILED DESCRIPTION OF THE ENTIRE TASK
https://snehakothavenkat.blogspot.com/2020/06/blog-post.html



