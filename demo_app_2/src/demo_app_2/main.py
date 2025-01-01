#!/usr/bin/env python
import sys
import warnings

# # Initialize Langfuse handler
# from langfuse.callback import CallbackHandler
# langfuse_handler = CallbackHandler(
#     secret_key="sk-lf-e25dad24-b42e-4883-b1ce-9b0a37c828ee",
#     public_key="pk-lf-6cdc2498-438f-4f8b-9d56-3c0a7a762571",
#     host="http://localhost:3000", # Localhost
#     # host="https://cloud.langfuse.com", # 🇪🇺 EU region
#   # host="https://us.cloud.langfuse.com", # 🇺🇸 US region
# )
 
# # Your Langchain code
 
# # Add Langfuse handler as callback (classic and LCEL)
# chain.invoke({"input": "<user_input>"}, config={"callbacks": [langfuse_handler]})

from demo_app_2.crew import DemoApp2

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    DemoApp2().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        DemoApp2().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DemoApp2().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        DemoApp2().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
