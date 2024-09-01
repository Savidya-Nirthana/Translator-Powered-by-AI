from django.shortcuts import render, HttpResponse
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Create your views here.
def translate(translate_from, translate_to, data):
    os.environ['GROQ_API_KEY'] = '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'
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "{input_language} to {output_language}.",
            ),("human", "{input}")
        ]
    )

    chain = prompt | llm

    out = chain.invoke({
        "input_language": translate_from,
        "output_language": translate_to,
        "input": data,
    })
    return out.content


def index(request):
    context = {}
    if request.method == 'POST':
        translate_from = request.POST.get('input_langs')
        translate_to = request.POST.get('output_langs')
        data = request.POST.get('data')
        translated = translate(translate_from, translate_to, data)
        context["translated"] = translated
        return render(request, 'translates/translates.html', context=context)
    return render(request, 'translates/translates.html')


