from django.shortcuts import render


def counter_view(request):
    return render(request, 'stimulus_basic/counter.html')