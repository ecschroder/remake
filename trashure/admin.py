from django.contrib import admin
from trashure.models import KnickKnack


class KnickKnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'era', 'votes_treasure', 'votes_trash', 'score')
    list_filter = ('era',)
    search_fields = ('name',)


admin.site.register(KnickKnack, KnickKnackAdmin)
