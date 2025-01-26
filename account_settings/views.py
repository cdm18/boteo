from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from account_settings.models import UserProfile
from account_settings.forms import UserProfileForm
from reservations.models import Reservation
from datetime import datetime


@login_required
def profile_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    # Obtener las reservas del usuario
    reservations = Reservation.objects.filter(user=request.user)
    total_reservations = len(reservations)

    total_hours = 0
    for reservation in reservations:
        start = datetime.combine(datetime.today(), reservation.start_time)
        end = datetime.combine(datetime.today(), reservation.end_time)

        delta = end - start
        total_hours += delta.total_seconds() / 3600


    context = {
        'profile': profile,
        'reservations': reservations,
        'total_hours': total_hours,
        'total_reservations': total_reservations,
    }

    return render(request, 'account_settings/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=request.user)

        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'profile_picture_url': profile.profile_picture.url if profile.profile_picture else None
            })
        return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})
