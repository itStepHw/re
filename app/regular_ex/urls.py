from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^index', index, name='index'),
    re_path(r'^about', about, name='about'),
    re_path(r'^contacts', contacts, name='contacts'),
]



# ^(начало адреса)
# $(конец адреса)
# +(1 и более символов)
# ?(0 или 1 символ)
# {n}(n символов)
# {n, m}(от n до m символов)
# .(любой символ)
# \d+(одна или несколько цифр)
# \D+(одна или несколько НЕ цифр)
# \w+(один или несколько буквенных символов)