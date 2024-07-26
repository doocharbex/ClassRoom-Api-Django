from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import APICreationForm
from .models import API, APIData

class CreateAPIView(View):
    def get(self, request):
        form = APICreationForm()
        return render(request, 'api_creator/create_api.html', {'form': form})

    def post(self, request):
        form = APICreationForm(request.POST)
        if form.is_valid():
            api = form.save(commit=False)
            api.user = request.user
            api.save()
            return redirect('api_list')
        return render(request, 'api_creator/create_api.html', {'form': form})

@login_required
def api_list(request):
    apis = API.objects.filter(user=request.user)
    return render(request, 'api_creator/api_list.html', {'apis': apis})

@login_required
def add_data(request, api_id):
    api = get_object_or_404(API, id=api_id)
    if api.user != request.user:
        return redirect('api_list')

    if request.method == 'POST':
        data = request.POST.get('data')
        APIData.objects.create(api=api, data=data)
        return redirect('api_data_list', api_id=api_id)
    return render(request, 'api_creator/add_data.html', {'api': api})

@login_required
def api_data_list(request, api_id):
    api = get_object_or_404(API, id=api_id)
    if api.user != request.user:
        return redirect('api_list')

    data = APIData.objects.filter(api=api)
    return render(request, 'api_creator/api_data_list.html', {'api': api, 'data': data})

@login_required
def edit_api(request, api_id):
    api = get_object_or_404(API, id=api_id)
    if api.user != request.user:
        return redirect('api_list')

    if request.method == 'POST':
        form = APICreationForm(request.POST, instance=api)
        if form.is_valid():
            form.save()
            return redirect('api_list')
    else:
        form = APICreationForm(instance=api)
    return render(request, 'api_creator/edit_api.html', {'form': form})
