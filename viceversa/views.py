from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['user_text']
    reversed_text = user_text[::-1]
    user_str = str(user_text).split()
    count = len(user_str)
    return render(request, 'reverse.html', {'user_text': user_text, 'reversed_text': reversed_text, 'count': count})


