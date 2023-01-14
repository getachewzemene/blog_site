from datetime import date

from django.shortcuts import render

posts = [
    {
        "slug": "Blog Site Using Django",
        "image": "django_image.png",
        "author": "Getch",
        "date": date(2023, 1, 5),
        "title": "Django Course",
        "excerpt": "This is a blog site using Django",
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
        "slug": "DevOps is the future of software development",
        "image": "devops.jpg",
        "author": "Getch",
        "date": date(2023, 1, 5),
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
        "slug": "Flutter is the future of mobile development",
        "image": "flutter_image.jpeg",
        "author": "Getch",
        "date": date(2023, 1, 5),
        "title": "Flutter Course",
        "excerpt": "FLutter is the future of mobile development and Web development",
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

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def all_posts(request):
    return render(request, 'blog/all-posts.html')


def post_detail(request, slug):
    return render(request, 'blog/post_detail.html')
