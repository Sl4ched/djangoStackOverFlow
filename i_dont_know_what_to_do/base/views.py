from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Discuss, Tag, Answer

from .forms import DiscussForm

from django.db.models import Q


def logout_page(request):
    logout(request)
    return redirect('home')


def login_page(request):
    if request.method == 'POST':

        mail = request.POST['mail']
        password = request.POST['password']

        user = authenticate(username=mail, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password or mail incorrect')

    context = {
        'title': 'login',
    }

    return render(request, 'base/login.html', context=context)


def register_page(request):
    context = {
        'title': 'register',
    }

    if request.method == 'POST':
        username = request.POST['mail']
        password = request.POST['password']
        password_confirmation = request.POST['password2']

        if password_confirmation == password:
            user = User.objects.create_user(
                username=username,
                password=password)

            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'Passwords must be the same')

    return render(request, 'base/register.html', context=context)


def home(request):
    context = {
        'title': 'Home',
        'whichSelected': 'home'
    }

    return render(request, 'base/home.html', context=context)


def questions(request):
    filter_query = request.GET.get('filter') if request.GET.get('filter') is not None else "newest"

    if filter_query == 'newest':
        discuss = Discuss.objects.all().order_by('-created')
    else:
        discuss = Discuss.objects.all()

    context = {
        'title': 'Questions',
        'discuss': discuss,
        'whichSelected': 'questions'
    }

    return render(request, 'base/questions.html', context=context)


def tags(request):
    discuss = Discuss.objects.all()

    def count_tag_amount_and_update():
        temp_dict = {tpc.tags: 0 for ds in discuss for tpc in ds.topics.all()}

        for i in discuss:
            for j in i.topics.all():
                temp_dict[j.tags] += 1

        for key, value in temp_dict.items():
            altered_topic = Tag.objects.get(tags=key)
            altered_topic.tag_count = value
            altered_topic.save()

    count_tag_amount_and_update()  # this is for update the amount of tag

    filter_tag = request.GET.get('filter') if request.GET.get('filter') is not None else "popular"

    if filter_tag == 'popular':
        whole_tags = Tag.objects.all().order_by('-tag_count')
    elif filter_tag == 'name':
        whole_tags = Tag.objects.all().order_by('tags')
    elif filter_tag == 'new':
        whole_tags = Tag.objects.all().order_by('-created')
    else:
        whole_tags = Tag.objects.filter(
            Q(tags__startswith=filter_tag)

        )
    context = {
        'title': 'Tags',
        'tags': whole_tags,
        'whichSelected': 'Tags'

    }
    return render(request, 'base/tags.html', context=context)


def users(request):
    users = User.objects.all()
    discuss = Discuss.objects.all()

    temp_dict = {}

    for item in discuss:
        temp_dict[str(item.user)] = 0

    for item in discuss:
        temp_dict[str(item.user)] += 1

    context = {
        'title': 'Users',
        'whichSelected': 'Users',
        'users': users,
        'amountOfQuestions': temp_dict

    }
    return render(request, 'base/users.html', context=context)


@login_required(login_url='home')
def discuss_room(request, id):
    specified_discuss = Discuss.objects.get(id=id)
    specified_discuss.views.add(request.user)  # added new user to views section

    context = {
        'specified_discuss': specified_discuss,
    }

    return render(request, 'base/discuss_room.html', context=context)


@login_required(login_url="home")
def create_discuss(request):
    template = 'base/create_discuss.html'

    form = DiscussForm()

    if request.method == 'POST':
        form = DiscussForm(request.POST)

        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user

            new_author.save()
            form.save_m2m()

            return redirect('questions')

    context = {
        'title': 'Create Discuss',
        'form': form
    }
    return render(request, template, context=context)
