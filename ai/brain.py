import boto3
import json
from prompts import ideas_generator, tech_stack_advisor, boilerplate_writer
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain


region_name = "us-east-1" #us-east-1
aws_access_key_id = "ASIA3CW6ONM4E7KVLKHB" #Paste the aws access key id here
aws_secret_access_key = "mRSj7ogSND3OcXgMyU9bOmGl1uOvn/e6osHIbTxA" #Paste the aws secret access key here
aws_session_token = "IQoJb3JpZ2luX2VjEAMaCXVzLWVhc3QtMSJHMEUCIQD9+uFAqfCn7eKmI1yw2ZhL8fxjPBUQGTGPk8NqsK2VdQIgVDYY10ratqUykQ/Ve4dzHnftJ7/oM3q3wk9W57TvofMqrgMI3P//////////ARAAGgw3NjE3NDk0NjU5MTIiDFcoSQRjshL7SgZSNSqCAze31Go6xT5suwwSDp8AhKdB4E7SrAooeEpSHhZUtWNxM+QkEXNeS6sFNzsH8CHddx01NHaqyJlDBCWX++LxG1YOwq97o4KjfzSgWLIHMV7JR/OVojvwLPJKi7Ka0eTwvZjG2NoQfwNE+xUQ/son8SHArD1JGvc6O/yuXbjyFKC+eU1+L17eyZeyksNvJaLmehjr2dt/3biuMFZUU6s1KT++tuzzSOcFSLGM78QzZIdXhYK7xMQ7346AnwjX/KCHo9b9C+r8HRjbCbXDxjw2mX/PjK0qVlLDLua7AWt207sMnXUcfL24PK/auLQ1DWNvvFVHJrf7PMVxLVGCl3ygfl3x5LEAN8fCPF1i9lvWw+SLjy1+tfNiag6DoOXS271EW83sq+PdtlN3vHc3wPcftzoKMEliX1h9WORojFgpbIa8BlmiXELZh89qBrhe+CVg4sDHdo015S5DDUM6F6WYrn1/MIXxAsd7jnvrxPQU1OO8wErv+ghsGCmuz6KCuen+Gk66MOj0w64GOqYB5b4Jl2FMvSH+reTWdHih9vPAfW6mPhv5yHWBAzmqmtj0sNz/SxFmzEaPcpIh+Ok5QPpXGeWWoQIkt7l1dGM+GC/9c800cvXogpDKLA0zvbLXPmMOI08krcFkwSIdtfqj3yC4ysQJXKBDsP31Hx4qht7+qJbq10acXgD55GGgZcvEi6c721WLtfZG+xTxzwe9u4fwyVrrqYTMypAjI261rrGnZKZ/Og==" #Paste the session token here
session = boto3.Session (
	region_name = region_name,
	aws_access_key_id = aws_access_key_id,
	aws_secret_access_key = aws_secret_access_key,
	aws_session_token = aws_session_token
)

generate_ideas_prompt = PromptTemplate.from_template(ideas_generator)
write_boilerplate_prompt = PromptTemplate.from_template(boilerplate_writer)


bedrock = session.client('bedrock-runtime') 

modelId = 'anthropic.claude-v2:1'
accept = 'application/json'
contentType = 'application/json'

memory = ConversationBufferMemory(ai_prefix="Assistant")

def generate_ideas(user_input: str):
    llm = Bedrock(
        model_id=modelId,
        client=bedrock,
        model_kwargs={"max_tokens_to_sample": 1500, "temperature": 0.6, "top_k": 250}
    )
    
    conversation = ConversationChain(llm = llm, verbose=False, memory=memory)   
    conversation.prompt = generate_ideas_prompt
    data = {}
    data['response'] = conversation.predict(input=user_input)
    return json.dumps(data)

def generate_stack(input: str, level:str):
    formatted = tech_stack_advisor.format(level=level, input=input)
    # print(formatted)
    formatted = PromptTemplate.from_template(formatted)
    llm = Bedrock(
        model_id=modelId,
        client=bedrock,
        model_kwargs={"max_tokens_to_sample": 1000, "temperature": 0.5}
    )
    conversation = ConversationChain(llm = llm, verbose=False)
    conversation.prompt = formatted   
    data = {}
    data['response'] = conversation.predict(input=input)
    return json.dumps(data)

def write_boilerplate(input: str, level: str, tech_stack: str):
    formatted = boilerplate_writer.format(input=input, level=level, tech_stack=tech_stack)
    print(formatted)
    formatted = PromptTemplate.from_template(formatted)
    llm = Bedrock(
        model_id=modelId,
        client=bedrock,
        model_kwargs={"max_tokens_to_sample": 1000, "temperature": 0.5}
    )
    conversation = ConversationChain(llm = llm, verbose=False)
    conversation.prompt = formatted   
    data = {}
    data['response'] = conversation.predict(input=input)
    return json.dumps(data)