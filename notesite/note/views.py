from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import NoteForm
from .models import Note

###############################################


def index(request):

    item_list = Note.objects.order_by("-date")
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Note')
    form = NoteForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "Note LIST",
    }
    return render(request, 'Note/index.html', page)


### function to remove item, it recive Note item id from url ##
def remove(request, item_id):
    item = Note.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('note')
