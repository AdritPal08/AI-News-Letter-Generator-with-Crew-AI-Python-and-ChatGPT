from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown

from dotenv import load_dotenv
load_dotenv()

# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Initialize the OpenAI GPT-4 language model
OpenAIGPT4 = ChatOpenAI(
    model="gpt-4"
)


# Instantiate the agents
editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()
quality_assurance = agents.quality_assurance_agent()

# Instantiate the tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
summarize_news_task = tasks.summarize_news_task(news_analyzer, [fetch_news_task])
extract_key_points_task = tasks.extract_key_points_task(news_analyzer, [fetch_news_task])
analyze_sentiment_task = tasks.analyze_sentiment_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [summarize_news_task,extract_key_points_task, analyze_sentiment_task], save_markdown)
quality_assurance_task = tasks.quality_assurance_task(quality_assurance,[compile_newsletter_task])
editor_task = tasks.editor_task(editor,[compile_newsletter_task])

# Form the crew
crew = Crew(
    agents=[news_fetcher, news_analyzer, newsletter_compiler,quality_assurance,editor],
    tasks=[fetch_news_task, summarize_news_task, extract_key_points_task, analyze_sentiment_task, compile_newsletter_task, quality_assurance_task, editor_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4,
    memory= True,
    verbose=True
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)
