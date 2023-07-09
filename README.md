
#  Sentiment Analysis with GUI

A Deep Learning Model which used for Sentiment analysis. The Accuracy it reach upto 85%. It train on 25000 text data. 

# Neural Network Info
The bert layer is integrated in the neural network at the second layer after input layer. The 3 GRU layer is for feature extraction
then a Conv1D Layer is use after that making the output flatten and passing through a bunch of dense layer.


## Info

1) "Bert_uncased_model_Tiwtter.h5" has reached to the accuracy upto 85% just on 30 epochs. Loss it got is 0.51. This model is purly train in Twitter dataset.
![SS1](https://github.com/somnathdashs/Sentiment-Analysis/blob/main/SS/Screenshot%202023-07-06%20215459.png?raw=true)

2) "Bert_uncased_model_Reddit.h5" has reached to the accuracy upto 84% just on 35 epochs. Loss it got is 0.81. This model is not purly train in Twitter dataset but a bit of reddit's dataset is also used.
![SS1](https://github.com/somnathdashs/Sentiment-Analysis/blob/main/SS/Screenshot%202023-07-06%20212910.png?raw=true)

Loss :- Sparse_categorical_crossentropy

Activatiion on last layer :- softmax

Note: Max input length is 768 words. 


## Screenshots

![Preview](https://github.com/somnathdashs/Sentiment-Analysis/blob/main/SS/Screenshot%202023-07-09%20103349.png?raw=true)

![Preview](https://github.com/somnathdashs/Sentiment-Analysis/blob/main/SS/Screenshot%202023-07-09%20103417.png?raw=true)

![Preview](https://github.com/somnathdashs/Sentiment-Analysis/blob/main/SS/Screenshot%202023-07-09%20103425.png?raw=true)

![Preview](https://github.com/somnathdashs/Sentiment-Analysis/blob/main/SS/Screenshot%202023-07-09%20103455.png?raw=true)

![Preview](https://github.com/somnathdashs/Sentiment-Analysis/blob/main/SS/Screenshot%202023-07-09%20104740.png?raw=true)


## Libray Used

 ##### > opencv
 ##### > tensorflow
 ##### > numpy 
 ##### > pickle 
 ##### > bert
 ##### > tensorflow_hub
 ##### > tensorflow_text





## Authors

- [@Somnath Dash](https://www.github.com/somnathdashs)

