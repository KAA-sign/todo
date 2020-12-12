from django.shortcuts import render
from main.models import ListModel

def main_view(request):

    lists = ListModel.objects.filter(user=request.user)

    context = {
        'lists': list,
        'user_name': request.user.usernaame
    }
    return render(request, 'index.html', context)
