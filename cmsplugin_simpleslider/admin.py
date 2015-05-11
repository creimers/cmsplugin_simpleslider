from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import (Image, Slider)

admin.site.register(Image, SortableAdmin)
