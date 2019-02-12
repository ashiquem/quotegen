# Quote Generation

This projects uses AI to generate motivational quotes. I built a twitter bot using the outputs of this project, which tweets motivational quotes everyday. You can follow it [@ai.motivate](https://twitter.com/AiMotivate)

The following methods are explored here:

1. Maximum likelihood model
2. Character based RNN
3. Word based RNN
4. Word based RNN with word embeddings

## Data

The data used for this project was scraped off the internet. The quotes.csv file contains 964 motivational quotes from 554 unique authors.

## Usage

The textgen.ipynb outlines the diffrent models. You can use this notebook to generate texts using any of the models. A GPU is required for training. If you wish to train on a CPU, please replace all [CuDNNLSTM](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CuDNNLSTM) layers with [LSTM](https://keras.io/layers/recurrent/) ones. More details [here](https://stackoverflow.com/questions/49987261/what-is-the-difference-between-cudnnlstm-and-lstm-in-keras).

I'll write an article on medium detailing all the different steps involved. Stay tuned!

## Twitter Bot

I have used the popular tweepy libary for building this bot. The tweet.py script expects a text file with quotes for each day, with each line in the format `MM-DD~Your Quote`. You can use a free service such as [Python Anywhere](https://www.pythonanywhere.com/) to schedule your script. Update the config.py file with your details and upload the files to the server. A really good guide for this can be found [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library).
