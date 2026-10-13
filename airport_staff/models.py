from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group, Permission

#  AbstractUser is used to include seperate fields for airport-staff
    # Indicates if the user is an airport staff member
        # which status the staff user belongs
                # special Permission for staff users
class AirportStaffUser(AbstractUser):
    is_airport_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='airport_staff_users',
        verbose_name="Assigned Groups"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='airport_staff_permissions',
        verbose_name="User Permissions"
    )

    def __str__(self):
        return self.get_full_name() or self.username

# Storing feedbacks from users
    #which user submitted the feedback
        # feedbak text
                # Rating from user
                    # getting time when feedback was submitted
                            # showing the feedback submitted by user
class Feedbacks(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="feedbacks", verbose_name="Submitted By"
    )
    feedback_text = models.TextField(verbose_name="Feedback")
    rating = models.IntegerField(default=0, verbose_name="Rating (1-5)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")
    def __str__(self):
        return f"Feedback by {self.user.username}: {self.feedback_text[:25]}..."
