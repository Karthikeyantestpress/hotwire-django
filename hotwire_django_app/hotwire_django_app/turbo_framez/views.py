import http

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from hotwire_django_app.tasks.models import Task
from hotwire_django_app.tasks.forms import TaskForm
from django.http import HttpResponse
from turbo_response import TurboFrame

def index_view(request):
    return render(request, 'turbo_framez/index.html')


def list_view(request):
    object_list = Task.objects.all().order_by('-pk')

    context = {
        "object_list": object_list,
    }

    return render(request, 'turbo_framez/list_page.html', context)


def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save()

            messages.success(request, 'Task created successfully')
            if request.turbo.frame:
                # if the request comes within Turbo Frame
                response = TurboFrame(
                    request.turbo.frame
                ).template('turbo_framez/message.html', {}).response(request)
                return response
            else:
                return redirect(reverse('turbo-frame:task-detail', kwargs={'pk': instance.pk}))

        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm()

    return render(request, 'turbo_framez/create_page.html', {'form': form}, status=status)


def update_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()

            if request.turbo.frame:
                # if request come from Turbo Frame
                return redirect(reverse('turbo-frame:task-detail', kwargs={'pk': instance.pk}))
            else:
                # if request come from standard page
                messages.success(request, 'Task update successfully')
                return redirect(reverse('turbo-frame:task-detail', kwargs={'pk': instance.pk}))

        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm(instance=instance)

    return render(request, 'turbo_framez/update_page.html', {'form': form}, status=status)


def delete_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        instance.delete()

        if request.turbo.frame:
            # if request come from Turbo Frame
            response = TurboFrame(f"task-detail-{pk}").response('')
            return response
        else:
            # if request come from standard page
            messages.success(request, 'Task deleted successfully')
            return redirect('turbo-frame:task-list')

    return render(request, 'turbo_framez/delete_page.html', {'instance': instance})


def detail_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    return render(request, 'turbo_framez/detail_page.html', {'instance': instance})