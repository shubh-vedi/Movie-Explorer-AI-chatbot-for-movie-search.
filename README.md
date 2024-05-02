# Movie Explorer

Movie Explorer is a Python-based application that utilizes AI models to recommend films based on user queries. It leverages OpenAI's language models for natural language understanding and Pinecone's similarity search for retrieving relevant movie recommendations.

## Features

- **Advanced Search**: Users can search for films using natural language queries with specific criteria such as genre, release year, director, and more.
- **Contextual Recommendations**: The application provides recommendations based on the user's query and the context of retrieved films.
- **Structured Output**: Film recommendations are presented in a structured format including title, runtime, release year, streaming availability, and reasoning.
- **Customizable**: The application's behavior can be customized by adjusting the configuration file and integrating different AI models.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/film-search.git

2. Install dependencies:

  ```bash
   pip install -r requirements.txt
 ```

3. Set up API keys:
 ```bash
   Create .env file and write this
   PINECONE_API_KEY = ""
   PINECONE_INDEX_NAME = ""
   OPENAI_API_KEY = ""
```

4. Run the Streamlit
  ```bash
  Streamlit run app.py
  ```

Contributing
Contributions are welcome! Here are a few ways you can contribute:

Report bugs or suggest improvements by opening an issue.
Implement new features or enhancements and submit a pull request.
Improve documentation to make it more comprehensive and user-friendly.


Acknowledgments
Movie Explorer was inspired by the desire to create a user-friendly film recommendation system powered by AI. We would like to thank the developers of OpenAI and Pinecone for their incredible tools and support.

Contact
For questions, feedback, or collaboration opportunities, please contact shubhamnv2@gmail.com.
   

