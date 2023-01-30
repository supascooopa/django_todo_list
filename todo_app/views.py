from django.shortcuts import render
from .models import ToDoList, ToDoItems
from django.views.generic import ListView


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"


class ItemListView(ListView):
    model = ToDoItems
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItems.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

