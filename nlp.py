# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:16:48 2019

@author: Dominick
"""

#rautken api
import requests
import argparse
import unirest

#amazon api
import boto3
import json

#requires from prior downloading for the amazon NLP 

def nlp_call():
    #text processing NLP call 
    response = unirest.post("https://japerk-text-processing.p.rapidapi.com/sentiment/",
    headers={
    "X-RapidAPI-Host": "japerk-text-processing.p.rapidapi.com",
    "X-RapidAPI-Key": "1cb24d07fdmsh0a4062c072f1dbdp164f8cjsn1c8a66bfc2fd",
    "Content-Type": "application/x-www-form-urlencoded"
    },
        params={
    "language": "english",
    "text": "How much damage does heroin do to the brain and how addictive is it?"
        }
        )
    for i in response.body['probability']:
        print (response.body['probability'][i])
    
    #microsoft NLP call
    response2 = unirest.post("https://microsoft-azure-text-analytics-v1.p.rapidapi.com/sentiment",
    headers={
    "X-RapidAPI-Host": "microsoft-azure-text-analytics-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "1cb24d07fdmsh0a4062c072f1dbdp164f8cjsn1c8a66bfc2fd",
    "Content-Type": "application/json"
  },
    params=("{\"documents\":[{\"language\":\"en\",\"id\":\"string\",\"text\":\"How much damage does heroin do to the brain and how addictive is it? \"}]}")
)
    print("microsoft: ", response2.body['documents'][0]['score'])
    if (response2.body['documents'][0]['score'] < 1):
        print("hello")
    
    #Amazon NLP call
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
                
    text = "It is raining today in Seattle"

    print('Calling DetectSentiment')
    print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectSentiment\n')

if __name__ == "__main__":
    nlp_call()
