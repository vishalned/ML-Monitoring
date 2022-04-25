# **ML-Monitoring**
Monitoring Machine learning training using telegram bot

### **Description**
Training of Machine Learning models takes a sufficient amount of time. There have been many instances when we have had to train models for hours and the only way to keep track of the model was to open up the terminal and check. With this repository, we show that, the training can be monitored remotely using a telegram bot and also the learning rate can be controlled. Incase needed, plots of the train/validation loss can be visualized from your remote device (phone/laptop). 

### **How to run**
- Set up bot father. Open telegram, and type /botfather and create a new bot.
- Copy the http token of your bot to the "token" keyword in the main.py file. 
- When the training starts, open the bot on your device and type /start to begin displaying the results

### **Bot Commands**
- /start : start the bot
- /stop_bot : terminate the bot
- /stop_training : stop the training
- /plot_loss : plot the train/validation loss at that instance
- /quiet : stop displaying stats after every epoch
- **/anti_gravity : Read a comic, incase you get bored waiting for the training to complete**

### **Dependencies**
- Python-telegram-bot == 12.0.0
- Keras == 2.2.4
- Matplotlib
- sns
- Python
- Numpy


