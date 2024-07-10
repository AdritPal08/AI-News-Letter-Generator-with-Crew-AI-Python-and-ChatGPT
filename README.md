# AI News Letter Generator with Crew AI, Python, and ChatGPT

This project utilizes Crew AI, Python, and ChatGPT to generate informative and engaging AI newsletters. 


## It leverages the following technologies:

**Crew AI:** Crew AI is an open-source framework that allows engineers to orchestrate autonomous AI agents to work together to solve complex tasks
**ChatGPT (OpenAI):** A large language model for generating human-quality text.
**Python Libraries:**
1. `crewai:` Python library for interacting with Crew AI.
2. `crewai_tools:` Additional utilities for working with Crew AI.
3. `langchain_openai:` Python library for interacting with OpenAI's language models.
4. `python-docx:` Python library for creating and manipulating DOCX documents.


## Project Structure
The project consists of the following files and directories:

**agents.py:** Defines Crew AI agents responsible for specific tasks in the newsletter creation process.
**tasks.py:** Defines Crew AI tasks for each agent of the newsletter creation.
**search_tools.py:** Provides a custom search tool using a Search Engine API (SERPER).
**file_io.py:** Contains functions for saving the generated newsletter in Markdown and docx formats.
**main.py:** The main script that instantiates Crew AI agents, tasks, and the OpenAI GPT-4 language model. It then forms a Crew object and kicks off the newsletter generation process.
**.env (hidden file):** Stores API keys (e.g., SERPER API key) used by the project.
**requirements.txt:** Stores all the python libraries. 


## How it Works

1. **News Fetching:** The `news_fetcher` agent retrieves top AI news stories using the `search_tools.search_internet` function.
2. **News Analysis:** The `news_analyzer` agent analyzes the fetched stories, generating summaries, extracting key points, and performing sentiment analysis.
3. **Newsletter Compilation:** The `newsletter_compiler` agent compiles the analyzed news stories into a well-formatted newsletter using the provided context (summaries, key points, sentiment).
4. **Quality Assurance:** The `quality_assurance` agent reviews the compiled newsletter for accuracy, compliance with editorial policies, and adherence to ethical guidelines.
5. **Editorial Review:** Finally, the `editor` agent performs a final review of the newsletter, ensuring overall structure, clarity, and engagement.


## Running the Project
1. **Install Requirements:**

```bash
pip install -r requirements.txt

```

2. **Set Up Environment Variables:**

Create a `.env` file in your project directory and add any required API keys (e.g., SERPER API key).

3. **Run the Script:**

```bash
python main.py
```

This will initiate the Crew AI workflow and generate an AI newsletter in Markdown and docx formats.


## Conclusion
This project demonstrates how Crew AI can be leveraged to automate AI newsletter generation using various AI tools and services. The project is extensible and can be further enhanced by incorporating additional functionalities or using different language models.


## License :

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) (LICENSE)


## Follow Me :

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adritpal/)


## Authors

- [@adrit](https://github.com/AdritPal08)


## 
- If you like my work and it helped you in anyway then please do ⭐ the repository it will motivate me to make more amazing projects