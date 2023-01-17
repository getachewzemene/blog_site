from datetime import date
from django.http import Http404
from django.shortcuts import render

posts = [
    {
        "slug": "django-is-the-future-of-web-development",
        "image": "django_image.png",
        "author": "Getch",
        "date": date(2023, 1, 5),
        "title": "Django Course",
        "excerpt": "Django is a batteries-included web framework that takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.",
        "content": """
                    lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. 
                    Praesent et diam eget libero egestas mattis sit amet vitae augue. 
                    Nam tincidunt congue enim, ut porta lorem lacinia consectetur. 
                    
                    Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Aenean ut gravida lorem. Ut turpis felis, pulvinar a semper sed, adipiscing id dolor. 
                    Pellentesque auctor nisi id magna consequat sagittis. Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl imperdiet.
                    
                    Ut convallis libero in urna ultrices accumsan. Donec sed odio eros. Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus.
                    Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In rutrum accumsan ultricies. 
                    Mauris vitae nisi at sem facilisis semper ac in est.                
                   """
    },
    {
        "slug": "DevOps-is-the-future-of-software-development-and-deployment",
        "image": "devops.jpg",
        "author": "Getch",
        "date": date(2023, 1, 2),
        "title": "DevOps Course",
        "excerpt": "Dev Ops is the future of software development and deployment",
        "content": """
                    lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. 
                    Praesent et diam eget libero egestas mattis sit amet vitae augue. 
                    Nam tincidunt congue enim, ut porta lorem lacinia consectetur. 
                    
                    Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Aenean ut gravida lorem. Ut turpis felis, pulvinar a semper sed, adipiscing id dolor. 
                    Pellentesque auctor nisi id magna consequat sagittis. Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl imperdiet.
                    
                    Ut convallis libero in urna ultrices accumsan. Donec sed odio eros. Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus.
                    Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In rutrum accumsan ultricies. 
                    Mauris vitae nisi at sem facilisis semper ac in est.                
                   """
    },
    {
        "slug": "Flutter-is-the-future-of-mobile-development-and-Web-development",
        "image": "flutter_image.jpeg",
        "author": "Getch",
        "date": date(2023, 1, 10),
        "title": "Flutter Course",
        "excerpt": "Flutter is the future of mobile development and Web development",
        "content": """
                    lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. 
                    Praesent et diam eget libero egestas mattis sit amet vitae augue. 
                    Nam tincidunt congue enim, ut porta lorem lacinia consectetur. 
                    
                    Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Aenean ut gravida lorem. Ut turpis felis, pulvinar a semper sed, adipiscing id dolor. 
                    Pellentesque auctor nisi id magna consequat sagittis. Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl imperdiet.
                    
                    Ut convallis libero in urna ultrices accumsan. Donec sed odio eros. Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus.
                    Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In rutrum accumsan ultricies. 
                    Mauris vitae nisi at sem facilisis semper ac in est.                
                   """
    }
]
# response_not_found = render_to_string('404.html')
# Create your views here.


def home(request):
    sorted_posts = sorted(posts, key=lambda k: k['date'])
    latest_posts = sorted_posts[-3:]

    try:
        return render(request, 'blog/index.html', {
            "posts": latest_posts,
        })
    except:
        raise Http404("Page does not exist")
        # return HttpResponseNotFound(response_not_found)


def all_posts(request):
    try:
        return render(request, 'blog/all-posts.html', {
            "posts": posts,
        })
    except:
        raise Http404("Page does not exist")


def post_detail(request, slug):
    identified_post = next(post for post in posts if post["slug"] == slug)
    try:
        return render(request, 'blog/post_detail.html', {
            "post": identified_post,
        })
    except:
        raise Http404("Page does not exist")
