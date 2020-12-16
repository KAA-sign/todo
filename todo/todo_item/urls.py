from django.urls import path
from todo_item.views import todo_item_view

app_name = 'item'

urlpatterns = [
    path('', todo_item_view),
    # path('create/', item_view),
    # path('delete/', item_view),
    # path('edit/', item_view),
]
