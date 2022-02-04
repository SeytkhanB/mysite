
from django.contrib import admin
from .models import Rubric, Article

from mptt.admin import DraggableMPTTAdmin
# from mptt.admin import MPTTModelAdmin


# the order is important here use MPTTModelAdmin after Rubric
# admin.site.register(Rubric, MPTTModelAdmin)

admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Article)


