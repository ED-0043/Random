import textatistic
import nltk
import spacy
import re
import os
import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

class SentimentAnalyser:
    """
    Sentiment Analyser
    ------------------
    class used to perform some sentiment analysis on textual data, used in the  fileapi.py
    file for making a sentiment analysis API.
    """
    
    def __init__(self, data, y: str):
        self.data = data 
        self.x = pd.DataFrame(data).drop(y).values
        self.y = pd.DataFrame(data[y])
        self.model = MultinomialNB(alpha=0.1).fit(self.x, self.y)

    def clean_data(self, pattern:str , data: list ,) -> list:
        """Cleans the data using regex pattern and returns a list
        
        Args:
            pattern (str): regular expression patter used to clean the data         
            path (str): directory where the text files are stored

        Returns:
            list
            
        Raises:
            None
            
        this is the google documnetation format
        """
        clean_data = []
                
        for x in self.data:
            words = x[0]
            words = re.sub(pattern, "", string=words)
            clean_data.append(words)
        
        return clean_data
    
    
    def flesch_score(self, average=bool) -> int:
        """applies the textatistcs flesch readability test
        
        Parameters
        ----------
        data: list 
            a list of strings to best tested with said scores 
            
        Returns
        -------
        integer of the the flesch readability score 
        
        this is the numpy documentation format
        """
        scores = []
        for x in self.data[0]:
            scores.append(textatistic.flesch_score(x))
        if average == True:
            return sum(scores)/ len(scores)
        else:
            return scores

    
    def smog_score(self, data: list) -> int:
        """applies the textatistcs smog readability test
        
        Parameters
        ----------
        data: list 
            a list of strings to best tested with said scores 
            
        Returns
        -------
        int containing the smog score  
        
        this is the numpy documentation format
        """
        pass
        
    
    def return_predictions(self, test: int|list) -> int|list:
        """returns model prediction values

        Parameters
        ----------
        test (int | list):
            values on which the model would use to perform predictions

        Returns
        -------
            integars or list of predicted values
        """
        predictions = self.model.predict(test)
        return predictions