from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import role_required

@login_required
@role_required('Librarian')
def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html')

