from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top AI news stories from the past 24 hours, including their titles, URLs, publication dates, and brief summaries. The news data should be collected from genuine and reputable sources. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""A list of top AI news story titles, URLs, and a brief summary for each story from the past 24 hours. 
                Example Output: 
                [
                    {'title': 'AI takes spotlight in Super Bowl commercials', 
                    'url': 'https://example.com/story1',
                    'published_at': '2023-02-13T10:30:00Z', # ISO 8601 format
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """
        )
    def summarize_news_task(self, agent, context):
        return Task(
        description='Summarize each news story in a concise and informative manner',
        agent=agent,
        async_execution=True,
        context=context,
        expected_output="""A list of dictionaries, where each dictionary represents a news story and contains the following keys:
            'title': The title of the news story
            'source': The name of the source where the news story was published
            'url': The URL of the news story
            'published_at': The publication date and time of the news story (in ISO 8601 format)
            'summary': A concise summary of the news story
            Example Output:
            [
                {
                    'title': 'AI takes spotlight in Super Bowl commercials',
                    'source': 'TechCrunch',
                    'url': 'https://techcrunch.com/2023/02/13/ai-super-bowl-commercials/',
                    'published_at': '2023-02-13T10:30:00Z',
                    'summary': 'Several companies, including Microsoft, showcased their AI products and assistants in high-profile Super Bowl commercials this year, highlighting the growing mainstream adoption of AI technology.'
                },
                {...}
            ]
        """
    )

    def extract_key_points_task(self, agent, context):
        return Task(
        description='Extract the key points or main takeaways from each news story',
        agent=agent,
        async_execution=True,
        context=context,
        expected_output="""A list of dictionaries, where each dictionary represents a news story and contains the following keys:
            'title': The title of the news story
            'key_points': A list of bullet points highlighting the main takeaways or key points from the news story
            Example Output:
            [
                {
                    'title': 'AI takes spotlight in Super Bowl commercials',
                    'key_points': [
                        '- Microsoft showcased its AI assistant Copilot in a commercial',
                        '- AI-powered chatbots and virtual assistants were featured prominently',
                        '- The commercials highlight the growing mainstream adoption of AI technology'
                    ]
                },
                {...}
            ]
        """
    )

    def analyze_sentiment_task(self, agent, context):
        return Task(
        description='Analyze the sentiment (positive, negative, or neutral) of each news story',
        agent=agent,
        async_execution=True,
        context=context,
        expected_output="""A list of dictionaries, where each dictionary represents a news story and contains the following keys:
            'title': The title of the news story
            'sentiment': The overall sentiment of the news story, classified as 'positive', 'negative', or 'neutral'
            Example Output:
            [
                {
                    'title': 'AI takes spotlight in Super Bowl commercials',
                    'sentiment': 'positive'
                },
                {...}
            ]
        """
    )
        
    def compile_newsletter_task(self, agent, context,callback_function):
        return Task(
        description='Compile a newsletter using the analyzed news stories, including a table of contents or section headers for better organization.',
        agent=agent,
        context=context,
        callback=callback_function,
        expected_output="""A well-structured newsletter with the following components:

1. Table of Contents or Section Headers: A list of news story titles or sections, with corresponding section numbers or anchors for easy navigation.

2. News Stories: Each news story should be presented in the following format:
    - Title
    - Source
    - URL
    - Published Date
    - Summary
    - Key Points
    - Sentiment (Positive, Negative, or Neutral)

Example Output:

Table of Contents:
1. AI takes spotlight in Super Bowl commercials
2. New AI model achieves state-of-the-art performance
3. Ethical concerns raised over AI surveillance technology

1. AI takes spotlight in Super Bowl commercials
   Source: TechCrunch
   URL: https://techcrunch.com/2023/02/13/ai-super-bowl-commercials/
   Published Date: 2023-02-13T10:30:00Z
   Summary: Several companies, including Microsoft, showcased their AI products and assistants in high-profile Super Bowl commercials this year, highlighting the growing mainstream adoption of AI technology.
   Key Points:
    - Microsoft showcased its AI assistant Copilot in a commercial
    - AI-powered chatbots and virtual assistants were featured prominently
    - The commercials highlight the growing mainstream adoption of AI technology
   Sentiment: Positive

2. New AI model achieves state-of-the-art performance
   ...

3. Ethical concerns raised over AI surveillance technology
   ...
"""
    )
    def editor_task(self, agent, context):
        return Task(
        description="""Review the compiled newsletter and ensure it meets the highest editorial standards.
        Your responsibilities include:
        
        1. Checking the overall structure and organization of the newsletter, including the table of contents and section headers.
        2. Reviewing the content of each news story for accuracy, clarity, and engagement.
        3. Ensuring that the summaries, key points, and sentiment analysis are consistent and coherent.
        4. Identifying any potential biases, errors, or inconsistencies in the content.
        5. Providing feedback and suggestions for improvement to the other agents involved in the newsletter creation process.
        6. Making final edits and revisions to the newsletter content as needed.
        
        Your goal is to produce a polished, informative, and engaging newsletter that captures the reader's attention and provides valuable insights into the latest AI news and developments.
        """,
        agent=agent,
        async_execution=True,
        context=context,
        expected_output="""A detailed report outlining your editorial review of the newsletter, including:
        
        1. An overall assessment of the newsletter's structure, organization, and flow.
        2. Specific feedback and suggestions for improving the content of each news story (e.g., clarity, accuracy, engagement).
        3. Recommendations for addressing any biases, errors, or inconsistencies identified.
        4. A summary of the edits and revisions made to the newsletter content.
        5. Any additional comments or suggestions for enhancing the overall quality and impact of the newsletter.
        """
        )
    def quality_assurance_task(self, agent, context):
        return Task(
        description="""Perform a comprehensive quality assurance review of the newsletter to ensure its accuracy, compliance, and adherence to editorial policies.
        Your responsibilities include:
        
        1. Fact-checking all information and data presented in the newsletter.
        2. Verifying the accuracy and credibility of sources cited.
        3. Ensuring compliance with ethical guidelines and editorial policies.
        4. Identifying any potential biases, errors, or inconsistencies in the content.
        5. Proofreading the newsletter for spelling, grammar, and formatting errors.
        
        Your goal is to maintain the highest standards of journalistic integrity and ensure that the newsletter is accurate, reliable, and compliant with all relevant policies and guidelines.
        """,
        agent=agent,
        async_execution=True,
        context=context,
        expected_output="""A detailed quality assurance report, including:
        
        1. A summary of the fact-checking process and any inaccuracies or inconsistencies identified.
        2. An assessment of the credibility and reliability of the sources cited.
        3. A list of any potential biases or ethical concerns identified in the content.
        4. A record of any spelling, grammar, or formatting errors found and corrected.
        5. An overall evaluation of the newsletter's compliance with editorial policies and guidelines.
        6. Recommendations for addressing any issues or concerns identified during the quality assurance review.
        """
        )
    # def user_feedback_task(self, agent, context):
    #     return Task(
    #     description="""Gather and analyze user feedback to understand their preferences, interests, and areas for improvement.
    #     Your responsibilities include:
        
    #     1. Collecting feedback from readers through various channels (e.g., surveys, social media, email).
    #     2. Analyzing the feedback to identify common themes, preferences, and areas for improvement.
    #     3. Identifying potential gaps or missed opportunities in the newsletter's content or format.
    #     4. Suggesting improvements or new features based on user feedback.
    #     5. Collaborating with other agents to implement changes and enhancements based on user feedback.
        
    #     Your goal is to ensure that the newsletter remains relevant, engaging, and tailored to the needs and interests of the target audience by continuously incorporating user feedback and insights.
    #     """,
    #     agent=agent,
    #     async_execution=True,
    #     context=context,
        #    expected_output="""A comprehensive user feedback analysis report, including:
        
        # 1. A summary of the feedback collection process and the channels used.
        # 2. An analysis of common themes, preferences, and areas for improvement identified in the feedback.
        # 3. Identification of any potential gaps or missed opportunities in the newsletter's content or format.
        # 4. Specific recommendations for improvements or new features based on user feedback.
        # 5. A plan for collaborating with other agents to implement the recommended changes and enhancements.
        # """
    
    # )
    