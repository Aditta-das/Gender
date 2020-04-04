from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorProfForm
from .models import Author, computer
from django.views.generic import View, ListView, DetailView
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

def include(request):
    return render(request, 'include.html')

def index(request):
    hot = get_object_or_404(Author, user=request.user.id)
    if Author.objects.filter(gender='Male'):
        count = Author.objects.filter(gender='Female').count()
        com = Author.objects.filter(gender='Female')[randint(0, count - 1)]
        print(com.user)
    if Author.objects.filter(gender='Female'):
        count = Author.objects.filter(gender='Male').count()
        com2 = Author.objects.filter(gender='Male')[randint(0, count - 1)]
        print(com2.user)

    context = {
        'hot': hot,
        'com': com,
        'com2': com2,
    }

    return render(request, 'index.html', context)


class AuthorProfileView(View):
    def get(self, *args, **kwargs):
        form = AuthorProfForm()
        return render(self.request, 'author.html', {'form': form})

    def post(self, *args, **kwargs):
        form = AuthorProfForm(self.request.POST, self.request.FILES or None)
        if form.is_valid():
            image = form.cleaned_data['image']
            gender = form.cleaned_data['gender']
            pro = Author(
                image=image,
                gender=gender,
                user=self.request.user,
            )
            pro.save()
            return redirect('index')
        return render(self.request, 'author.html')

class ProfileView(DetailView):
    def get(self, *args, **kwargs):
        try:
            prof = Author.objects.get(user=self.request.user)
            context = {
                'prof': prof,
            }
            return render(self.request, 'profile.html', context)
        except ObjectDoesNotExist:
            return redirect('author')