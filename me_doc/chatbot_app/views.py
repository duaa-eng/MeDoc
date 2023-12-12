from django.shortcuts import render
from django.http import HttpResponse

def chatbot_view(request):
    return render(request, 'chatbot_app/index.html')


def getResponse(request):
    # get the data sent from the frontend ajax funtion
    userMessage = request.GET.get('userMessage')
    
    #call RAG pipeline with the userMessage
    api_response = RAGPipeline(userMessage)
    # print(api_response)
    
    return HttpResponse(api_response.content)

def RAGPipeline(umessage):
    
    import os
    from langchain.chat_models import ChatOpenAI
    
    #openai key can be saved as a system variable and retrieved for security issues
    #or else you can include it here
    openai_api_key = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY"
    print(openai_api_key)

    #calling openai api 
    chat = ChatOpenAI(
        model='gpt-3.5-turbo'
    )
    
    from langchain.schema import(
        SystemMessage,
        HumanMessage,
        AIMessage
    )
    
    messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    # HumanMessage(content=umessage)
    ]
    
    # res = chat(messages)
    
    # # add latest AI response to messages
    # messages.append(res)
    
    #adding source knowledge data to answer specific questions
    diseases_symptoms = [
    "A LLMChain is the most common type of chain. It consists of a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser. This chain takes multiple input variables, uses the PromptTemplate to format them into a prompt. It then passes that to the model. Finally, it uses the OutputParser (if provided) to parse the output of the LLM into a final format.",
    "Chains is an incredibly generic concept which returns to a sequence of modular components (or other chains) combined in a particular way to accomplish a common use case.",
    "LangChain is a framework for developing applications powered by language models. We believe that the most powerful and differentiated applications will not only call out to a language model via an api, but will also: (1) Be data-aware: connect a language model to other sources of data, (2) Be agentic: Allow a language model to interact with its environment. As such, the LangChain framework is designed with the objective in mind to enable those types of applications."
    ]

    source_knowledge = "\n".join(diseases_symptoms)
    
    
    #answer based on the data source provided
    query = umessage

    augmented_prompt = f"""Using the contexts below, answer the query.

    Contexts:
    {source_knowledge}

    Query: {query}"""
    
    # create a new user prompt
    prompt = HumanMessage(
        content=augmented_prompt
    )
    # add to messages
    messages.append(prompt)

    # send to OpenAI
    res = chat(messages)
    
    
    return res