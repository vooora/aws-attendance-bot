from llm_handler import generate_sql_query, generate_response
from sql_executor import run_query
import os

def lambda_handler(event, context):
    user_question = event['sessionState']['intent']['slots']['UserQuestion']['value']['originalValue']

    schema = open('schema.md', 'r').read()

    prompt = f"""
        Database schema:
        {schema}

        User asked:
        "{user_question}"

        Write an SQL query to answer it.
        Just return the query.
        """

    sql_query = generate_sql_query(prompt)

    try:
        data = run_query(sql_query)
    except Exception as e:
        return format_response(f"Error while querying: {str(e)}")

    response_prompt = f"User asked: {user_question}\nData: {data}\nRespond in clear English."
    final_response = generate_response(response_prompt)

    return format_response(final_response)

def format_response(message):
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": "ExamAttendanceQuery",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message
            }
        ]
    }

def main():
    # Mock AWS Lambda event structure
    mock_event = {
        "sessionState": {
            "intent": {
                "name": "ExamAttendanceQuery",
                "slots": {
                    "UserQuestion": {
                        "value": {
                            "originalValue": "list the students enrolled in computer networks?"
                        }
                    }
                }
            }
        }
    }
    
    # Mock AWS Lambda context (not used here, but required)
    mock_context = {}

    # Call the Lambda handler
    result = lambda_handler(mock_event, mock_context)
    print("Lambda Response:", result)

if __name__ == "__main__":
    main()
