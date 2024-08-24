from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import PostReport, UserProfileReport
from .forms import ReportForm
from posts.models import Post
from userprofile.models import UserProfile

@login_required
def report_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.post = post
            report.save()
            return redirect('report_success')  # Redirect to the success page
    else:
        form = ReportForm()
    return render(request, 'templates/report_post.html', {'form': form, 'post_id': post_id})

@login_required
def report_user_profile(request, user_profile_id):
    user_profile = get_object_or_404(UserProfile, id=user_profile_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = UserProfileReport(
                user=request.user,
                user_profile=user_profile,
                reason=form.cleaned_data['reason'],
            )
            report.save()
            return redirect('report_success')  # Redirect to the success page
    else:
        form = ReportForm()
    return render(request, 'templates/report_user_profile.html', {'form': form, 'user_profile': user_profile})

@login_required
def render_success(request):
    post_reports = PostReport.objects.select_related('post__user').all().order_by('-created_at')
    user_profile_reports = UserProfileReport.objects.select_related('user_profile__user').all().order_by('-created_at')
    
    # Combine both reports into a single context variable if needed
    reports = list(post_reports) + list(user_profile_reports)
    
    context = {
        'post_reports': post_reports,
        'user_profile_reports': user_profile_reports,
        'reports': reports,  # This combines both types of reports
    }
    
    return render(request, 'templates/success.html', context)

@login_required
def accept_report(request, report_id):
        report = get_object_or_404(PostReport, id=report_id)
        report.post.delete()  # Delete the post
        report.delete()  # Delete the report
        messages.success(request, f"The post report has been accepted, and the related content has been deleted.")
        return redirect('report_success')  # Redirect to the success page

@login_required
def reject_report(request, report_id):
    report = get_object_or_404(PostReport, id=report_id)
    
    report.delete()  # Delete the report only
    messages.success(request, f"The post report has been rejected.")
    return redirect('report_success')  # Redirect to the success page

@login_required
def accept_user_profile_report(request, report_id):
    report = get_object_or_404(UserProfileReport, id=report_id)
    user_profile = report.user_profile

    # Ban the user profile if the report count reaches 3
    user_profile.report_count += 1
    user_profile.save()
    user_profile.check_and_ban()
    messages.success(request, "The user profile report has been accepted. The user profile has been reviewed.")
    return redirect('report_success')

@login_required
def reject_user_profile_report(request, report_id):
    report = get_object_or_404(UserProfileReport, id=report_id)
    report.delete()  # Delete the report only
    messages.success(request, "The user profile report has been rejected.")
    return redirect('report_success')
