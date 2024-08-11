from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
            summary = data.describe(include='all').to_html()
            return render(request, 'summary.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
