import boto3
import json
from . import prompts
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain


region_name = ""  # us-east-1
aws_access_key_id = ""  # Paste the aws access key id here
aws_secret_access_key = ""  # Paste the aws secret access key here
aws_session_token = ""  # Paste the session token here
session = boto3.Session(
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
)

generate_ideas_prompt = PromptTemplate.from_template(prompts.ideas_generator)
tech_stack_advisor_prompt = PromptTemplate.from_template(prompts.tech_stack_advisor)
write_boilerplate_prompt = PromptTemplate.from_template(prompts.boilerplate_writer)


bedrock = session.client("bedrock-runtime")

modelId = "anthropic.claude-v2:1"
accept = "application/json"
contentType = "application/json"

memory = ConversationBufferMemory(ai_prefix="Assistant")


def generate_ideas(user_input: str):
    llm = Bedrock(
        model_id=modelId,
        client=bedrock,
        model_kwargs={"max_tokens_to_sample": 1500, "temperature": 0.6, "top_k": 250},
    )

    conversation = ConversationChain(llm=llm, verbose=False, memory=memory)
    conversation.prompt = generate_ideas_prompt
    data = {}
    data["response"] = conversation.predict(input=user_input)
    return json.dumps(data)


def generate_stack(input: str, level: str):
    formatted = tech_stack_advisor_prompt.format(level=level, input=input)
    # print(formatted)
    formatted = PromptTemplate.from_template(formatted)
    llm = Bedrock(
        model_id=modelId,
        client=bedrock,
        model_kwargs={"max_tokens_to_sample": 1000, "temperature": 0.5},
    )
    conversation = ConversationChain(llm=llm, verbose=False)
    conversation.prompt = formatted
    data = {}
    data["response"] = conversation.predict(input=input)
    data["level"] = level
    return json.dumps(data)


def write_boilerplate(input: str, level: str, tech_stack: str):
    formatted = write_boilerplate_prompt.format(
        input=input, level=level, tech_stack=tech_stack
    )
    print(formatted)
    formatted = PromptTemplate.from_template(formatted)
    llm = Bedrock(
        model_id=modelId,
        client=bedrock,
        model_kwargs={"max_tokens_to_sample": 1000, "temperature": 0.5},
    )
    conversation = ConversationChain(llm=llm, verbose=False)
    conversation.prompt = formatted
    data = {}
    data["response"] = conversation.predict(input=input)
    data["level"] = level
    data["tech_stack"] = tech_stack
    return json.dumps(data)
