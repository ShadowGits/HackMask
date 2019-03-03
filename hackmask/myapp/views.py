from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.
def contact(request):

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            text=form.cleaned_data['body']

            print(name, email,text)
            return redirect('parse/')

    else:
        form=ContactForm()
    return render(request,'form.html',{'form':form})


from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions,EntitiesOptions
import json

def parseUrl(request):


    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey='_rUw5fo4HSexS1ZUv7Ae5Ih9ZOGb4cWsu7JQF5c6FVxZ',
        url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
    )

    response = natural_language_understanding.analyze(
        url='www.ibm.com',
        features=Features(entities=EntitiesOptions(sentiment=True,limit=10))).get_result()

    print(json.dumps(response, indent=2))
    json_decode = response
    arr=list
    for i in response.get('entities'):
        print(i.get('text'))
        arr.append(i)
        arr.append('  \n  ')
    return HttpResponse("<h2> Output ="+json.dumps(response,indent=2)+" <br/>  "+arr+"</h2>")


