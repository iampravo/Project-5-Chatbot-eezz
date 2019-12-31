import spacy 
import pandas as pd  
import random  
from constants import *


df_esg_ratings = pd.read_csv("./data/esgratings.csv")
df_mcap = pd.read_csv('./data/marketCapital.csv')
df_profile_details = pd.read_csv('./data/profiledetails.csv')


ratings_df_dict = {'esg' : df_esg_ratings}


def return_org_in_text(text):
    """
    Return ORG name if found in text.
    Else returns None.
    """
    for company in ['Apple', 'Google', 'MSCI Inc.', 'General Motors', 'Tesla', 'Amazon', 'Walmart', 'Berkshire Hathaway', 'JPMC']:
        if company.lower() in text.lower():
                return company
    nlp = spacy.load('en_core_web_sm') 
    doc = nlp(text)   
    for ent in doc.ents:
        if ent.label_=='ORG':
            return(ent.text)    
        return None

def return_person_in_text(text):
    """
    Return PER name if found in text.
    Else returns None.
    """
    nlp = spacy.load('en_core_web_sm') 
    doc = nlp(text)   
    for ent in doc.ents:
        if ent.label_=='PERSON':
            return(ent.text)    
        return None

def esg_rating_response_generator(input):
    df_esg_ratings['Company_name_1'] = df_esg_ratings['Company_name_1'].str.lower()
    df_esg_ratings['Company_name_2'] = df_esg_ratings['Company_name_2'].str.lower()
    company_rating_dict_1 =  pd.Series(df_esg_ratings.ESG_Rating.values,index=df_esg_ratings.Company_name_1).to_dict()
    company_rating_dict_2 =  pd.Series(df_esg_ratings.ESG_Rating.values,index=df_esg_ratings.Company_name_2).to_dict()
    org_name = return_org_in_text(input)
    if org_name!= None:
        try:
            return f"{company_rating_dict_1[org_name.lower()]} is the ESG rating of {org_name}"
        except KeyError:
            try:
                return f"{company_rating_dict_2[org_name.lower()]} is the ESG rating of {org_name}"
            except KeyError:
                return "Cannot find ESG Rating of {}".format(org_name)
    return  "Cannot find ESG Rating"

def mcap_response_generator(input):
    df_mcap['Company_name'] = df_mcap['Company_name'].str.lower()
    company_m_cap_dict =  pd.Series(df_mcap.mcap_crores.values,index=df_mcap.Company_name).to_dict()
    org_name = return_org_in_text(input)
    if org_name!= None:
        try:
            return f"{company_m_cap_dict[org_name.lower()]} crore rupees is the mcap of {org_name}"
        except KeyError:
            return "Cannot find market cap of {}".format(org_name)
    return  "Cannot find market cap"

def profile_details_response_generator(input):
    df_profile_details['Person_name'] = df_profile_details['Person_name'].str.lower()
    person_profile_dict =  pd.Series(df_profile_details.Profile_details.values,index=df_profile_details.Person_name).to_dict()
    per_name = return_person_in_text(input)
    if per_name!= None:
        try:
            return person_profile_dict[per_name.lower()]
        except KeyError:
            return "Cannot find profile of {}".format(per_name)
    return  "Cannot find profile."


def greeting_intent(text):
    return random.choice(greeting_response)+" "+random.choice(greeting_predicate)


def goodbye_intent(text):
    return random.choice(goodbye_response)+" "+random.choice(goodbye_predicate)
 
