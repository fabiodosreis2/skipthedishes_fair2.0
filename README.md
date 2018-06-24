
### VANHACKTHON Fair 2.0

### Sentiment Analysis Amazon Fine Food Reviews
We've got a dataset from [Kaggle](https://www.kaggle.com/snap/amazon-fine-food-reviews) and based on the customer review text we've build a model to predict the rating score [between 1 and 5] of the product.


### Install

This project requires **Python >= 3.5** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [Flask](http://flask.pocoo.org)

pip install -r requirements.txt

### Download the dataset
[download.zip](https://www.kaggle.com/snap/amazon-fine-food-reviews/downloads/amazon-fine-food-reviews.zip/2)

### About the data
We've got the texts reviews (Text column) and used TF-IDF transformation to extract features and the Score columns as the target.
You can see the code to build the model in this [Jupyter Notebook](https://github.com/fabiodosreis2/skipthedishes_fair2.0/blob/master/vanhackthon.ipynb).


### API
We developed a RESTFUL API using Flask to expose this model.

 ## API parameters
       ```
       Request
       Content-Type = "application/json"
       {"text_review": "your review about the project here"}
       
       Response
       {"sentiment": "positive"}
       {"sentiment": "negative"}
       ```

### How to Run



### Authors

[Fábio Eduardo dos Reis](https://www.linkedin.com/in/fabiodosreis/)

[Heros da Silva Araujo](https://www.linkedin.com/in/herosaraujo/)



