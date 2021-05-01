from django.shortcuts import render

# Utilities
from datetime import datetime


posts = [
    {
        'title': 'Whatsapp 2',
        'user': {
            'name': 'Alexis Loya',
            'nickname': '@LasterLG117',
            'picture': 'https://pbs.twimg.com/profile_images/1107499827917656064/OotAmKIk_400x400.png',

        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EseKu3PW8AApkdC?format=png&name=360x360',
    },
    {
        'title': 'SuperLiga Mx',
        'user': {
            'name': 'Ayanami',
            'nickname': '@asuukkka',
            'picture': 'https://pbs.twimg.com/profile_images/1285349343860580352/DBkB35Pn_400x400.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EzhGcdFWEAIryC2?format=jpg&name=large',
    },
    {
        'title': 'he volvido a tuiter',
        'user': {
            'name': 'eoto002',
            'nickname': '@eoto002',
            'picture': 'https://pbs.twimg.com/profile_images/1366519767310467072/uWNnFGYh_400x400.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EzilSBiUUAE0D_X?format=jpg&name=900x900',
    },
    {
        'title': 'Cocina cocina',
        'user': {
            'name': 'Asuka Daily',
            'nickname': '@asuka_dailycl',
            'picture': 'https://pbs.twimg.com/profile_images/1011999448971579392/wFuXbWyE_400x400.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo': 'https://pbs.twimg.com/media/EziHKetXoAA2vai?format=png&name=900x900',
    }
]


def list_post(request):
    return render(request, 'posts/feed.html', {'posts': posts})
