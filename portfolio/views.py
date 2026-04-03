from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Education, ContactMessage


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    context = {'profile': profile, 'active': 'home'}
    return render(request, 'portfolio/home.html', context)


def about(request):
    profile = get_profile()
    context = {'profile': profile, 'active': 'about'}
    return render(request, 'portfolio/about.html', context)


def skills(request):
    profile = get_profile()
    all_skills = Skill.objects.all()
    languages = all_skills.filter(category='language')
    frameworks = all_skills.filter(category='framework')
    tools = all_skills.filter(category='tool')
    others = all_skills.filter(category='other')
    context = {
        'profile': profile,
        'languages': languages,
        'frameworks': frameworks,
        'tools': tools,
        'others': others,
        'active': 'skills',
    }
    return render(request, 'portfolio/skills.html', context)


def projects(request):
    profile = get_profile()
    all_projects = Project.objects.all()
    context = {'profile': profile, 'projects': all_projects, 'active': 'projects'}
    return render(request, 'portfolio/projects.html', context)


def education(request):
    profile = get_profile()
    edu_list = Education.objects.all()
    context = {'profile': profile, 'education_list': edu_list, 'active': 'education'}
    return render(request, 'portfolio/education.html', context)


def contact(request):
    profile = get_profile()
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()
        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    context = {'profile': profile, 'active': 'contact'}
    return render(request, 'portfolio/contact.html', context)
