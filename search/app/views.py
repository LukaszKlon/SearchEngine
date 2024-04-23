from django.shortcuts import render
from .forms import TextInputForm
import scipy.sparse as sp
import numpy as np
from engine.request import make_request_normal,make_request_SVD



def text_input_view(request):
    if request.method == 'POST':

        form = TextInputForm(request.POST)
        if form.is_valid():
            # Do something with the form data (here, just fetch it)
            svd = form.cleaned_data['svd']
            text = form.cleaned_data['text']
            print(svd)
            if svd:
                res = make_request_SVD(text)
            else:
                res = make_request_normal(text)

            return render(
                request,
                template_name='display.html',
                context={
                    'query': text,
                    'page_list': res
                })
    else:
        form = TextInputForm()


    return render(request, 'input.html', {'form': form})
    
