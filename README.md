# Image_Captioning using coco dataset and pretrained model
# from udacity computer vision nanodegree

---

- encoder resnet (Pretrained model)

- decoder RNN(lstm) 

in this project we alternate between LSTM and GRU to improve accuracy

---


### Table of Contents


- [Description](#description)
- [Flowchart](#Flowchart)
- [Technologies](#Technologies)
- [instructions](#instructions)
- [License](#license)

---

## Description :point_left:

Machine Translation showed how to translate text from one human language to another. 

It worked by having two Recurrent NeuralNetworks (RNN), the first called an encoder and the second called a decoder. 

The first RNN encodes the source-text as a single vector of numbers and the second RNN decodes this vector into the destination-

text. The intermediate vector between the encoder and decoder is a kind of summary of the source-text, which is sometimes called

a "thought-vector". The reason for using this intermediate summary-vector is to understand the whole source-text before it is 

being translated. This also allows for the source- and destination-texts to have different lengths.

In this project we will replace the encoder with an image-recognition model similar to Transfer Learning and Fine-Tuning in 

 The image-model recognizes what the image contains and outputs that as a vector of numbers - the "thought-vector" or summary-
 
 vector, which is then input to a Recurrent Neural Network that decodes this vector into text.


---

## Flowchart :ear:

We will use the VGG16 model that has been pre-trained for classifying images. But instead of using the last classification 

layer, we will redirect the output of the previous layer. This gives us a vector with 4096 elements that summarizes the image-

contents - similar to how a "thought-vector" summarized the contents of an input-text  on language translation. 

We will use this vector as the initial state of the Gated Recurrent Units (lstm). However, the internal state-size of the We will use

this vector as the initial state of the Gated Recurrent Units (lstm). However, the internal state-size of the GRU is 
 

only 512, so we need an intermediate fully-connected (dense) layer to map the vector with 4096 elements down to a vector with

only 512 elements.

The decoder then uses this initial-state together with a start-marker "ssss" to begin producing output words. In the first 

iteration it will hopefully output the word "big". Then we input this word into the decoder and hopefully we get the word 

"brown" out, and so on. Finally we have generated the text "big brown bear sitting eeee" where "eeee" marks the end of the text.

The flowchart of the algorithm is roughly:

---




## Technologies

- pretrained model(resnet)
- convolution neural network
- RNN(LSTM)
- deep learning


---
## instructions

1. Clone this repo: https://github.com/cocodataset/cocoapi  
```
git clone https://github.com/cocodataset/cocoapi.git  
```

2. Setup the coco API (also described in the readme [here](https://github.com/cocodataset/cocoapi)) 
```
cd cocoapi/PythonAPI  
make  
cd ..
```

3. Download some specific data from here: http://cocodataset.org/#download (described below)

* Under **Annotations**, download:
  * **2014 Train/Val annotations [241MB]** (extract captions_train2014.json and captions_val2014.json, and place at locations cocoapi/annotations/captions_train2014.json and cocoapi/annotations/captions_val2014.json, respectively)  
  * **2014 Testing Image info [1MB]** (extract image_info_test2014.json and place at location cocoapi/annotations/image_info_test2014.json)

* Under **Images**, download:
  * **2014 Train images [83K/13GB]** (extract the train2014 folder and place at location cocoapi/images/train2014/)
  * **2014 Val images [41K/6GB]** (extract the val2014 folder and place at location cocoapi/images/val2014/)
  * **2014 Test images [41K/6GB]** (extract the test2014 folder and place at location cocoapi/images/test2014/)

4. The project is structured as a series of Jupyter notebooks that are designed to be completed in sequential order (`0_Dataset.ipynb, 1_Preliminaries.ipynb, 2_Training.ipynb, 3_Inference.ipynb`).


---

## license

MIT License

Copyright (c) 2018 Udacity

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

[Back To The Top](#README.md) :point_up:

---

End :raising_hand:
