from django.shortcuts import render

posts = [
    {
        'author' : 'Sreehari J',
        'title'  : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'July 12, 2023'
    },
        {
        'author' : 'Vishnu TS',
        'title'  : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'July 13, 2023'
    },
        {
        'author' : 'Ajay Suresh',
        'title'  : 'Blog Post 3',
        'content' : 'Third Post Content',
        'date_posted' : 'July 14, 2023'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{ 'title':'About' })