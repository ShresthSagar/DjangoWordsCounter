# from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    text = request.GET['text']
    diff_words = text.split()

    words_dict = {}
    for word in diff_words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    sorted_list = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'text': text, 'words': len(diff_words), 'each_word': sorted_list})
