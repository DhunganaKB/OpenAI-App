def generate(question, llm, PromptTemplate):
    with open('input_text.txt', 'r') as file:
        input_text = file.read()  # Reads the entire file
        #print(content)

    template="""
    you are a political analyst and you have been asked to analyze the 2024 United States presidential election based on the information provided below.

    {input_text}
    please generate a concise and clear answer to the question.

    question: {question}

    answer:
    """
    prompt_template = PromptTemplate(input_variables=["input_text", "question"], template=template)

    final_prompt = prompt_template.format(input_text=input_text, question=question)
    print(final_prompt)
    response = llm.invoke(final_prompt)
    print(response.content)
    return response.content
