from django.shortcuts import render

post = [
    {
        'author': 'Parth',
        'title': 'Post',
        'content': 'First',
        'date': 'June 21, 2026'
    },
    {
        'author': 'Neel',
        'title': 'Post2',
        'content': 'Second',
        'date': 'June 22, 2026'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'about' })

