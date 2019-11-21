## ask-me-anything-chatbot
This repository is to implement ask me anything chat-bot with the help of existing implementations here on GitHub. 
Many thanks goes to `anuj`. I meraly created some wrapper to get people understand and implement it easily. 
I also created some functions which will help the new comers'. For example to check if they have the correct dependencies installed. 
***
Here is one expample 
```python
def lib_check(): 
    import tensorflow as tf
    if (tf.__version__) != '1.2.0':
        print("you must need tensorflow 1.2.0 to use this project")
        print("you are running on tensorflow {} version".format(tf.__version__))
    import numpy as np
    if (np.__version__) != '1.13.0':
        print("you must need numpy 1.13.0 to use this project")
        print("you are running on numpy {} version".format(np.__version__))
    import keras
    if (keras.__version__) != '2.0.2':
        print("you must need keras 2.0.2 to use this project")
        print("you are running on keras {} version".format(keras.__version__))
    else:
        print("congratulations...! you already have all the correct dependencies installed")

lib_check()
```
***
If you get the message saying `congratualtions...!` then you are good to go else follow the instructions to install correct library
versions. One way could  be to follow following instructions. 
***
```
git clone git@github.com:nirajdevpandey/Ask_me_anything-chatbot.git

cd Ask_me_anything-chatbot

pip install -r requirements.txt
```
***
>If you have the latest or later version of any used library you will recieve an error. There are some differences between tensorflow/keras older and newer versions and so on...... you might get text encoding error. 

### Here is what the output looklike. 
![title](https://github.com/nirajdevpandey/Ask_me_anything-chatbot/blob/master/Output/Output.gif)

