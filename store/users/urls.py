from django.urls import path
<<<<<<< HEAD
from users.views import login, registration, profile

app_name = 'users'
=======
from users.views import login, registration, profile, logout

app_name = "users"
>>>>>>> after_pause

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
<<<<<<< HEAD
]

=======
    path('logit/', logout, name='logout')
]
>>>>>>> after_pause
