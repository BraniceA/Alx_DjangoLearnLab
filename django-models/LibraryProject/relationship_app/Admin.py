from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import role_required

@login_required
@role_required('Admin')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

