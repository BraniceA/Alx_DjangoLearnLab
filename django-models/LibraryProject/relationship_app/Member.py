from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import role_required

@login_required
@role_required('Member')
def member_dashboard(request):
    return render(request, 'member_dashboard.html')

