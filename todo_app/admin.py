from django.contrib import admin
from todo_app.models import ToDoItems, ToDoList

admin.site.register(ToDoItems)
admin.site.register(ToDoList)

