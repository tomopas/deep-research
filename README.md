Open Source Deep Research using Ollama

You can change the useAI() Function to use Huggingface Models or ChatGPT API or other LLM's.

First you will need to install the dependencies by doing
```
pip install -r requirements.txt
```

Then you can run the program by doing
```
python main.py
```

The Code which was commented out can improve the response if you are using LLM's with more parameters than tinyllama for example which can't format the response in the correct way. You can edit the code to first make your LLM create a Plan which search terms to look up and then use the duckduckgosearch to get the information.
