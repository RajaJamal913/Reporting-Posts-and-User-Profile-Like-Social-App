from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def view_profile(request):
    profiles = UserProfile.objects.all()# This will use the related_name 'profile' from the OneToOneField
    return render(request, 'templates/view_profile.html', {'profiles': profiles})

@login_required
def edit_profile(request):
    profile = request.user.profile  # This should now work correctly with the related_name
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'templates/edit_profile.html', {'form': form})
