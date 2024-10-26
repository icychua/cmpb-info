import json
from helper_functions import llm



def response_to_PE_query(user_message):
    
    with open("./data/PE_info.md") as file:
        context = file.read()

    delimiter = "####"

    system_message = f"""
    You are a chatbot in the Singapore context, helping pre-enlistees to the Singapore Armed forces.
    Pre-enlistees will be asking you questions about the process and activities leading up to the actual enlistment date.

    The questions and queries will be enclosed in
    the pair of {delimiter}.

    Below, you will be provided context to answer the pre-enlistee's questions. 
    Only answer from the given context, and you can reply "I don't know" if the answer cannot be found in the given context.

    <context>
    {context}
    </context>

    """
    
    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    cmpb_info_response = llm.get_completion_by_messages(messages)
    return cmpb_info_response

def process_query(user_input):

    reply = response_to_PE_query(user_input)

    return reply