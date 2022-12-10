from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView

from base.models import Room, Message
from base.templates.forms import RoomForm, LOGGER


def hello(request):
    s = request.GET.get('s','')
    return HttpResponse(f'Ahoj{s}!!!')
 ##buď def rooms nebo class rooms
# def rooms(request):
#     rooms = Room.objects.all()
#     context = {'rooms': rooms}
#     return render(request, template_name='base/rooms.html', context=context)

class RoomsView(ListView):
    template_name = 'base/rooms.html'
    model = Room

def room(reguest, pk):
    LOGGER.info(reguest.method)
    room = Room.objects.get(id=pk)
    if reguest.method == "POST":
        Message.objects.create(
            user=reguest.user,
            room=room,
            body=reguest.POST.get('body')
        )
        room.participants.add(reguest.user)
        room.save()
        return redirect('room', pk=room.id)
    messages = room.message_set.all()
    context = {'messages':messages, 'room':room}
    return render(reguest, template_name='base/room.html', context=context)

class RoomCreateView(CreateView):
    template_name = 'base/room_form.html'
    form_class = RoomForm
    success_url = reverse_lazy('rooms')

    # def form_valid(self, form):
    #     cleaned_data = form.cleaned_data
    #     Room.objects.create(
    #      name=cleaned_data['name'],
    #      description=cleaned_data['description']
    #  )
    #     return super().form_valid(form)

class RoomUpdateView(UpdateView):
    template_name = 'base/room_form.html'
    form_class = RoomForm
    success_url = reverse_lazy('rooms')
    model =Room

class RoomDeleteView(DeleteView):
    template_name = 'base/room_confirm_delete.html'
    model = Room
    success_url = reverse_lazy('rooms')


