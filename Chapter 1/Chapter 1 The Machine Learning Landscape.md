---
size: 16:9
style: |
  .small-text {
    font-size: 0.75rem;
  }
marp: true
theme: default
paginate: true

npx marp --html --output=dist --input-dir=src
"marp": {
   "allowLocalFiles": true,
   "inputDir": "src",
   "output": "dist",
   "html": true
}
---

# Chapter 1 The Machine Learning Landscape

---
# Getting Inside
### 1) What is Machine Learning(ML)?
### 2) Why Use ML?
### 3) Example of Apps
### 4) Types of ML Systems
### 5) Main Challenges of ML
### 6) Testing and Validating
---
# 1) What is Machine Learning (ML)?

### Machine learning is the science of programming computers so they can `learn from data`

### "Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed." -Arthur Samuel, 1959

### "A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E. -Tom Mitchell, 1997
---
# 2) Why use ML?
+ Compare to traditional approach, a ML model can perform better with simpler code when existing solutions require a lot of tuning or many lists of rules.
+ An alternative solution to handle complex problems.
+ Require updating dataset (a ML system can easily handle this by retrained on new data)
+ Getting insights about complex problems and big data

---
### 3) Example of Apps
+ Computer Vision, using ML to classify image-based data with Convolutional Neural Networks (CNNs)
+ Classifying news article, using Natural Language Processing (NLP) text classification, with recurrent neural networks (RNNs) and CNNs, or better with transformers
+ Forecasting stocks, revenue or any value based on past performance metrics, using regression model, linear regression or polynomial regression, a support vector machine (SVM) or an Artificial Neural Network (ANN)
+ Segmenting account preference based on search-history, clustering task, using k-means, DBSCAN, etc
+ Recommending a product to client, based on past purchases, recommender system using feed past purchases to an ANN
+ Building Intelligent bot, using Reinforcement Learning (RL) to train agents/bots to pick action that maximize rewards over time
---
# 4) Types of ML Systems
## Distinguish based on following principle:
+ How they are supervised during training (supervised; unsupervised, semi-supervised, self-supervised)
+ Whether or not they can learn incrementally while in progress (online learning, batch learning)
+ Whether they work by simply comparing new data points to known data points, or instead by detecting patterns in the training data and building a predictive model, much like scientists do (instance-based versus model-based learning)
---
# 4.1) Training Supervision Model
### Classified according to the amount and type of supervision data get during training
+ ***Supervised learning***, the training set feeded to the algorithm includes the desired solutions, called labels. Typical tasks mainly about *classification* and *regression*. Training model given set value of *target* with respected *features* to separate between set of *class*
+ ***Unsupervised learning***, the training data is unlabeled. Typical tasks mainly about ***clustering***. Training model use *visualization* algorithms, other related task is *dimensionality reduction* algorithm called  *feature extraction*, *anomaly detection* and *association rule learning*
---
+ ***Semi-supervised learning***, a combination model between supervised and unsupervised learning. The main problem of labelling plenty of instances is usually time-consuming and costly, semi-supervised algo can deal with data that's partially labeled. Example app: Google Photos, Upload lots of photos to the service, it automatically recognizes the same person A, shows up in certain photos, and person B in another, and add label everyone in every photo. See [reference](https://www.computerworld.com/article/2988232/google-photos-custom-labeling.html).
+ ***Self-supervised learning***, another approach that involves generating a fully labeled dataset from a fully unlabeled one.The most infamous example would be image recovery, that masked images are used as the inputs, and the original images are used as the labels.
+ ***Reinforcement learning***, the learning system, called an *agent*, can observe the environment, select and perform actions, and get *rewards/penalties* in return. It must learn by itself what is the best strategy, called a *policy*, to get the most reward over time. Example implementation: DeepMind's AlphaGo program when it beat Ke Jie, the number 1 ranked Go player in the world at the time (May, 2017). See [reference](https://www.nytimes.com/2017/05/23/business/google-deepmind-alphago-go-champion-defeat.html).
---
# 4.2) Batch vs Online Learning
| Attributes         | Batch     | Online |
|--------------|-----------|------------|
| Training Data Process| Using all available data| Train incrementally by feeding *mini-batches* |
| Data Update | Retrain from scratch  | Continuously learning incrementally|
| Important Aspect| Time-consuming and costly when updating huge amount of data|*Learning rate*, how fast it adapt to changing data|

---
# 4.3) Instance-Based vs Model-Based Learning
## Categorize ML systems by how they *generalize/ making prediction*
| Attributes         | Instance-based learning   | Model-based learning |
|--------------|-----------|------------|
| Important Aspect| *Measure of similarity* | Utility Function/Performance|
| Validating/Training Process |Compare the new value/instance with the nearest cluster/class | Use Mathematic Model like linear regression, multivar regression|

---
## Categorize ML systems by how they *generalize/ making prediction*
| Attributes         | Instance-based learning   | Model-based learning |
|--------------|-----------|------------|
| Important Aspect| *Measure of similarity* | Utility Function/Performance|
| Validating/Training Process |Compare the new value/instance with the nearest cluster/class | Use Mathematic Model like linear regression, multivar regression|
---
# 5) Main Challenges of Machine Learning
### As a ML engineer, your main task mostlikely will be selecting a model and training data, "bad model" and "bad data" will be your most obstacle.
### Example of "bad data":
+ *Insufficient quantity of training data*
+ *Nonrepresentative training data*
+ *Poor quality data*
+ *Irrelevant features*
+ *Overfitting the training data*
+ *Underfitting the training data*
---

# 6) Testing and Validating
### After data training, you need to test your trained model to see how well it will make a prediction (generalize) to new cases.
### As a wise-man said, split your data pouch into two sets: the *training set* and *test set*. As each name imply, train your model using the training data set, and test/validate it using your test set. The error rate for training set and test set is called training error and generalization error respectively.

### Overfitting means the training error is low, but get the generalization error high. Inversely, you get underfitting.

### As rule of thumb, use 70-80% of the data as training set and the remaining as test set. Select the ratio of training set and test set hinder the model not to become overfitting and underfitting.
---

# 7) Hyperparameter Tuning and Model Selection