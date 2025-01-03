# Deliberately set the OPENAI_API_KEY to an invalid value to ensure that the code is not using it.
import os
os.environ['OPENAI_API_KEY'] = "Nope!"

# Must precede any llm module imports
# from langtrace_python_sdk import langtrace
# import os
# langtrace.init(api_key = os.environ['LANGTRACE_API_KEY'])


from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


from  openai import OpenAI

local_openai_client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")


#from crewai import LLM
#lmstudio = LLM(model="qwen2.5-14b-instruct", base_url="http://localhost:11434/v1", api_key="lmstudio")



# https://docs.crewai.com/concepts/agents#agent-tools
# let's try adding some tools for the researcher agent
# from crewai_tools import SerperDevTool, WikipediaTools
# from crewai_tools import SerperDevTool

# Create tools
# search_tool = SerperDevTool()
# wiki_tool = WikipediaTools()

# # Deliberately set the OPENAI_API_KEY to an invalid value to ensure that the code is not using it.
# import os
# os.environ['OPENAI_API_KEY'] = "Nope!"

# # Must precede any llm module imports
# from langtrace_python_sdk import langtrace
# import os
# langtrace.init(api_key = os.environ['LANGTRACE_API_KEY'])

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class LatestAiDevelopment():
	"""LatestAiDevelopment crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[search_tool, wiki_tool],
			# tools=[search_tool],
			verbose=True,
			llm=local_openai_client
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=local_openai_client
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
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
		"""Creates the LatestAiDevelopment crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
