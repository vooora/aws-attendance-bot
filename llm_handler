from openai import OpenAI
import os

client = OpenAI(api_key)
def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_sql_query(prompt):
    return call_llm(prompt)

def generate_response(prompt):
    return call_llm(prompt)

