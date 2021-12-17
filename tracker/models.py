from django.db import models
from django_fsm import FSMField, transition

LOCATION = (
    ('with-retailer', 'with-retailer'),
    ('with-dispatch', 'with-dispatch'),
    ('with-user', 'with-user')
)


class Cylinder(models.Model):
    cylinder_number = models.CharField(max_length=20)
    assigned_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    state = FSMField(
        choices=LOCATION, default='with-retailer', protected=True)

    def __str__(self):
        return self.cylinder_number

    @transition(field=state, source='with-retailer', target='with-dispatch', custom=({'button_name': 'Dispatch'}))
    def issue_cylinder_for_delivery(self):
        return "Cylinder has been issued for delivery to user"

    @transition(field=state, source='with-dispatch', target='with-user', custom=({'button_name': 'Close'}))
    def issue_cylinder_to_final_user(self):
        return "Cylinder has been delivered to the final user"

    @transition(field=state, source='with-user', target='with-dispatch', custom=({'button_name': 'Return'}))
    def return_cylinder_from_final_user(self):
        return "Cylinder has been retrieved from final user for return"

    @transition(field=state, source='with-dispatch', target='with-retailer', custom=({'button_name': 'Back to retailer'}))
    def return_cylinder_to_retailer_store(self):
        return "Cylinder has been returned to the retailer"
