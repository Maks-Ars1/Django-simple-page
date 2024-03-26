from django.shortcuts import render
from .forms import MyUserForm
import requests
from back.models import Task


# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'back/index.html', context)

def post_data(request):
    if request.method == 'POST':
        api_url = 'http://jsonplaceholder.typicode.com/posts'
        try:
            response = requests.post(api_url)
            print(response.json())
            idval = ''
            if 'id' in response.json():
                idval = response.json()['id']
            title = ''
            if 'title' in response.json():
                title = response.json()['title']
            bd = ''
            if 'body' in response.json():
                bd = response.json()['body']
            userId = 0
            if 'userId' in response.json():
                userId = response.json()['userId']
            new_db = Task(id=idval, title=title, body=bd, userId=userId)
        except Exception as e:
            print("error")
        user_form = MyUserForm()
        context = {
            'success': '1',
            'id': idval,
            'title': title,
            'body': bd,
            'userId': userId
        }
        return render(request, 'back/success.html', context)
    else:
        user_form = MyUserForm()
        context = {
            'success': '0'
        }
        return render(request, 'back/index.html', context)