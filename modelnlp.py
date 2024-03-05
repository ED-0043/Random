import textatistic
import nltk
import spacy
import re
import os
import numpy as np
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


class SentimentAnalyser:
    """
    Sentiment Analyser
    ------------------
    class used to perform some sentiment analysis on textual data, used in the  fileapi.py file for making 
    a sentiment analysis API.
    
    Params
    ------
    arg 1():
        ...
    arg2 ():
        ...
        
    Returns
    -------
        ...
    """
    lemmatizer = nltk.stem.WordNetLemmatizer()
    model = MultinomialNB()
    tfid = TfidfVectorizer()
    CountVectorizer()
    textatistic.Textatistic()
    
    clean_data = [] # make this a global variable for the class
    
    def __init__(self, ):
        
        
        pass
    
    @classmethod
    def clean_data(self, pattern:str , path: str ,) -> list:
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
                
        os.chdir(path=path)
        for x in os.listdir():
            words = x[0]
            words = re.sub(pattern, "", string=words)
        
        return clean_data.append(words)
    
    def readablility_score(self, data: list):
        """applies the textatistcs smog and flesch readability tests
        
        Parameters
        ----------
        data: list 
            a list of strings to best tested with said scores 
            
        Returns
        -------
        tuple containing the two readability test scores  
        
        this is the numpy documentation format
        """
        for x in data:
            smog = self.text_score.smog_score(x)
            flesch = self.text_score.flesch_score(x)
            
            avg_smog = np.avg(smog)
            avg_flesch = np.avg(flesch)
            
        return ({"smog_score": avg_smog}, {"flesch_score": avg_flesch}) #FIXME
        pass
    
    def dataframer(self, ) -> pd.Dataframe:
        pass
        
    def preprocess_text():
        pass
    
    def return_predictions():
        
        pass
    
    def new_function(self):
        
        return