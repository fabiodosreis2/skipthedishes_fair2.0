
### VANHACKTHON Fair 2.0

### Sentiment Analysis Amazon Fine Food Reviews
We've got a dataset from [Kaggle](https://www.kaggle.com/snap/amazon-fine-food-reviews) and based on the customer review text we've build a model to predict sentiment (positive, negative) about the product.


### Install

This project requires **Python >= 3.5** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [Flask](http://flask.pocoo.org)

pip install -r requirements.txt

- You have to install and run [docker](https://docs.docker.com/install/)

### Download the dataset
[download.zip](https://www.kaggle.com/snap/amazon-fine-food-reviews/downloads/amazon-fine-food-reviews.zip/2) and extract
Reviews.csv for the project directory. 

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
       {"sentiment": "Positive"}
       {"sentiment": "Negative"}
       ```

### How to Run
1 - Run all steps in Jupyet Notebook to generate the model.
2 - $python3 build_docker.py
3 - docker run -p 805:805 vanhackthon
4 - After you can use curl to post some review and get the response.
    ```
    curl -X POST \
  http://localhost:805 \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 52dd3e4a-a671-4b29-9efc-9ea8ce96396b' \
  -d '{
    "text_review": "Product arrived labeled as Jumbo Salted Peanuts...the peanuts were actually small sized unsalted. Not sure if this was an error or if the vendor intended to represent the product as \"Jumbo\"."}'
    ```


### Authors

[Fábio Eduardo dos Reis](https://www.linkedin.com/in/fabiodosreis/)

[Heros da Silva Araujo](https://www.linkedin.com/in/herosaraujo/)



