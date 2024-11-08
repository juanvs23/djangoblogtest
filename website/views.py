from django.shortcuts import render


pages = [
    {
        "title": "Home",
        "url": "/",
        'name':'home',
        "meta_description": "Home Page",
        "active": True
    },
    {
        "title": "About Us",
        "url": "/about-us",
        "name": "about-us",
        "meta_description": "About Us Page",
        "active": True
    },
    {
        "title": "Contact Us",
        "url": "/contact-us",
        "name": "contact-us",
        "meta_description": "Contact Us Page",
        "active": True
    },
    {
        "title": "Blog",
        "url": "/blog",
        "name": "blog",
        "meta_description": "Blog Page",
        "active": True
    },
    {
        "title": "Documentation",
        "url": "/documentation",
        "name": "documentation",
        "meta_description": "Documentation Page",
        "active": False
    },
    {
        "title": "Presentation",
        "url": "/presentation",
        "name": "presentation",
        "meta_description": "Presentation Page",
        "active": False
    }
]

# Create your views here.
def homeView(request):
    return render(request, "pages/home.html", {
        "pages": pages,
        "pageData": pages[0],
    })

def aboutView(request):
    return render(request, "pages/about-us.html", {
        "pages": pages,
        "pageData": pages[1],
    })

def contactUsView(request):    
    return render(request, "pages/contact-us.html",{
        "pages": pages,
        "pageData": pages[2],
    })

def documentationView(request):
    return render(request, "docs/documentation.html",{
        "pages": pages,
        "pageData": pages[4],
    })

def presentationView(request):
    return render(request, "presentation.html",{
        "pages": pages,
        "pageData": pages[5],
    })