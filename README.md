# Image_Captioning using coco dataset and pretrained model

---

- encoder vgg16 (Pretrained model)

- decoder RNN(GRU) 

in this project we alternate between LSTM and GRU to improve accuracy

---


### Table of Contents


- [Description](#description)
- [Flowchart](#Flowchart)
- [Technologies](#Technologies)
- [Link dataset](#dataset)
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

We will use this vector as the initial state of the Gated Recurrent Units (GRU). However, the internal state-size of the GRU is 

only 512, so we need an intermediate fully-connected (dense) layer to map the vector with 4096 elements down to a vector with

only 512 elements.

The decoder then uses this initial-state together with a start-marker "ssss" to begin producing output words. In the first 

iteration it will hopefully output the word "big". Then we input this word into the decoder and hopefully we get the word 

"brown" out, and so on. Finally we have generated the text "big brown bear sitting eeee" where "eeee" marks the end of the text.

The flowchart of the algorithm is roughly:

---

<p>

<img src="https://user-images.githubusercontent.com/50107057/82888889-398a9080-9f4a-11ea-9acf-4d8dfad06df4.PNG">

</p>

---


## Technologies


---


## dataset

To download click Here :point_down:

[download]()

- how to use it :open_mouth:



---

## license


---

[Back To The Top](#README.md) :point_up:

---

End :raising_hand:
