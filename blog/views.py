from django.shortcuts import render

posts = [
    {
        'author': 'Aperlae',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 7, 2023'
    },
    {
        'author': 'Maria',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 8, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
