# RAFT_test_bot_OpenAI
# Telegram bot using OpenAI API in RAFT
 
1. [Descriprion bot](#description)
2. [Installation](#install)
3. [Run bot](#run)
4. [Examples](#examples)
   
# <a name="description">Desctiption project</a>

This project is a telegram bot that transfers the image style. There is a picture of content at the input, and a stylized image at the output. [The Fast Neural Style algorithm](https://clck.ru/34sQ3q) was used for the development
The idea is to train the network to transfer a certain style to many different images.

List of available bot commands:
- /start - Start of the bot
- /help - list of available commands
- /info - information about neural style transfer
- /examples - examples of images created by this bot
- /transfer_style - transferring the style of the original image

# <a name="install">Installation</a>

### Git clone
```
git clone https://github.com/Shubin-vadim/Background-Segmentation.git
```
### Installing dependencies

```
pip3 install -r requirements.txt
```

# <a name="run">Run bot</a>

```
python app.py
```

# <a name="examples">Examples</a>
<img src="https://github.com/Shubin-vadim/DLSHool_tg_bot/blob/master/imgs/cat.jpg" width="400" alt="cat" />
<img src="https://github.com/Shubin-vadim/DLSHool_tg_bot/blob/master/imgs/city.jpg" width="400" alt="city" />
<img src="https://github.com/Shubin-vadim/DLSHool_tg_bot/blob/master/imgs/zebras.jpg" width="400" alt="zebras" />
