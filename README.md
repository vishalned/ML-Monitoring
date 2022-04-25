# **ML-Monitoring**
Monitoring Machine learning training using telegram bot

### **Description**
Training of Machine Learning models takes a sufficient amount of time. There have been many instances when we have had to train models for hours and the only way to keep track of the model was to open up the terminal and check. With this repository, we show that, the training can be monitored remotely using a telegram bot and also the learning rate can be controlled. Incase needed, plots of the train/validation loss can be visualized from your remote device (phone/laptop). 

### **How to run**
- Set up bot father. Open telegram, and type /botfather and create a new bot.
- Copy the http token of your bot to the "token" keyword in the main.py file.
- Set the user id to your Telegram user id so that only you can control the training 
- When the training starts, open the bot on your device and type /start to begin displaying the results

### **Bot Commands**
- /start : start the bot to get automatic updates
- /help: get a reply with all command options
- /status: get a reply with the latest epoch's results
- /getlr: get a reply with the current learning rate
- /setlr: change the learning rate (multiply by a factor of 0.5,0.1,2 or 10)
- /stoptraining : stop the training
- /plot: plot the train/validation loss at that instance
- /quiet: stop getting automatic updates each epoch
- **/antigravity : Read a comic, incase you get bored waiting for the training to complete**

### **Dependencies**
- Python-telegram-bot == 12.0.0
- Keras == 2.2.4
- Matplotlib
- sns
- Python
- Numpy


