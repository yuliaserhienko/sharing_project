from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from files_sharing import forms
from files_sharing.models import File


@login_required
def file_upload_page(request):
    form = forms.FileUploadForm()
    return render(request, 'files_sharing/index.html', context={'form': form})


@login_required
def user_files_page(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'main/index.html', context={'files': files})


@login_required
def save_file(request):
    result = {'file_uploaded': False, 'errors': None}
    if request.method == 'POST':
        form = forms.FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            result = {'file_uploaded': True}
        if form.errors:
            result['errors'] = form.errors
    else:
        result['errors'] = 'Request method not allowed'
    return JsonResponse(result)



