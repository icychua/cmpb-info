import json
import csv
import pandas as pd
from helper_functions import llm

df = pd.read_csv(r"./data/Vocation_info.csv")

vocation_info = df.to_json(orient="records")

def identify_most_suitable_vocation(user_message):
    delimiter = "####"

    system_message = f"""
    You are a chatbot in the Singapore context, helping pre-enlistees into the Singapore Armed Forces \
    decide what is the most suitable vocation for them.
    You will be provided with a self-written description about the user, including any skills \
    they would like to develop in the course of their National Service (NS).

    The self-written description will be enclosed in
    the pair of {delimiter}.

    Decide if the skills and description are relevant to any specific Vocations \
    in the Python list below, where details about each vocation are in the dictionary within.

    If there are more than 3 vocations, get the top 3 most relevant vocations.
    Else, get all the relevant vocations.

    {df}

    Provide your output in the below format. When providing the skills, provide ALL skills listed in the vocation found in the \
    python list of dictionaries provided earlier.

    <example format>
    Based on your self description, I would recommend the following three vocations: \n
    Vocation 1: Guards \n
    Skills honed throughout NS: Motivation,Teamwork,Survival skills,Resilience,Drive to succeed \n

    Vocation 2: Air Defence \n
    Skills honed throughout NS: Alertness,Commitment,Teamwork,Decision-making skills \n
    </example>
    """
    
    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    vocation_response = llm.get_completion_by_messages(messages)
    return vocation_response

def process_user_message(user_input):

    reply = identify_most_suitable_vocation(user_input)

    return reply