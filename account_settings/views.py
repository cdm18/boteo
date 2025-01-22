from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from account_settings.models import UserProfile
from account_settings.forms import UserProfileForm

@login_required
def profile_view(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    # Datos quemados para las reservas
    mock_reservations = [
        {
            'facility': 'Centro Deportivo "Planeta Fútbol"',
            'date': '2024-07-10',
            'time': '15:00',
            'status': 'Confirmada'
        },
        {
            'facility': 'Complejo Deportivo Tenis Club',
            'date': '2024-07-12',
            'time': '10:00',
            'status': 'Confirmada'
        },
        {
            'facility': 'Piscina Olímpica Concentración',
            'date': '2024-08-05',
            'time': '14:00',
            'status': 'Confirmada'
        }
    ]

    context = {
        'profile': profile,
        'reservations': mock_reservations
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