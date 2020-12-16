from django.shortcuts import render
from todo_item.models import ItemModel


# data_list = {
#     'lists': [
#         {'name': 'Написать в деканат', 'is_done': False},
#         {'name': 'Распечать документы', 'is_done': True, 'date': '01.12.2020'},
#         {'name': 'Сделать ДЗ', 'is_done': True},
#         {'name': 'Создать папку templatetags', 'is_done': False}
#     ],
#     'user_name': 'Admin',
#     'list_name': 'По работе'
# }


def todo_item_view(request):
    lists = ItemModel.objects.all(
        # user=request.user,
        # id=1
    )
    # new_list = [
    #     ListModel.objects.create(
    #         name=f'Новый список{i}',
    #         user=request.user
    #     )
    #     for i in [5, 6, 7]
    # ]

    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)

