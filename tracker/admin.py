from django.contrib import admin

from tracker.models import Cylinder
from fsm_admin.mixins import FSMTransitionMixin

admin.site.site_header = "VENZOSCF ADMIN DASHBOARD"


@admin.register(Cylinder)
class CylinderAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = (
        '__str__',
    )

    fields = (
        'id',
        'cylinder_number',
        'state'
    )

    readonly_fields = (
        'id',
        'state'
    )
