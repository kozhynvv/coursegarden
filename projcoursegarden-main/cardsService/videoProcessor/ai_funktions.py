import openai
from . import local_settings
from openai import OpenAI

client = OpenAI(
    api_key=local_settings.GPT_API_KEY,
)


def transcription_ai_cleanup(text):
    print(text)
    # Define the prompt for the model
    prompt = f"""
    Please clean the text of repetitions.
    Don't add anything by yourself.

    The text is: "{text}"
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=4096,
        temperature=0.7,
    )
    completion = response.choices[0].message.content
    return completion


def separate_transcription_into_themes(text):
    # Define the prompt for the model
    # Change after receiving prompt from tech dir
    prompt = f"""
    Please divide the following text into logical themes or sections.
    For each section, provide a brief title or theme and then the
    corresponding text. Format the output as follows:

    Theme: [Theme 1]
    Text: [Corresponding text]

    Theme: [Theme 2]
    Text: [Corresponding text]

    The text is: "{text}"
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=4096,
        temperature=0.7,
    )
    completion = response.choices[0].message.content    
    return completion


def questions_from_text(text):
    # Define the prompt for the model
    # Change after receiving prompt from tech dir
    # Creating query of questions, options and right answers
    prompt = f"""
        Text included themes and corresponding to them texts.  
        Please create question for each theme with 4 answer options, 
        only one answer is correct for each question and 
        answer should be taken from corresponding to that theme text. 
        Format must be straight as followed:
        Question 1, (answer1;answer2;answer3;answer4), Correct answer;

        {text}
        """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=4096,
        temperature=0.7,
    )
    completion = response.choices[0].message.content
    return completion


