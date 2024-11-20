
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


# from langchain.llms import Ollama
# from langchain_community.llms import Ollama
# ollama_openhermes = Ollama(model="openhermes")
# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

# from langchain_ollama import OllamaLLM
# ollama_llm = OllamaLLM(model="ollama/llama3.2")




from langchain_openai import ChatOpenAI

# Deliberately set the OPENAI_API_KEY to an invalid value to ensure that the code is not using it.
import os
os.environ['OPENAI_API_KEY'] = "Nope!"

# Must precede any llm module imports
from langtrace_python_sdk import langtrace
langtrace.init(api_key = os.environ['LANGTRACE_API_KEY'])


# Uncomment the following line to use an example of a custom tool
# from demo_app.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# llm=LLM(model="ollama/qwen2.5-coder", base_url="http://localhost:11434")
ollama_llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
#llm=LLM(model="ollama/llama3.1", base_url="http://localhost:11434")
# llm=LLM(model="ollama/opencoder", base_url="http://localhost:11434")
# llm=LLM(model="ollama/llama3.2", base_url="http://192.168.2.16:11434")
# llm=ChatOpenAI(base_url="http://127.0.0.1:1234/v1") # Wow! This still uses OpenAI's API!

@CrewBase
class DemoApp():
	"""DemoApp crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=ollama_llm
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=ollama_llm
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the DemoApp crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
