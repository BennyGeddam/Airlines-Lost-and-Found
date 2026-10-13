from django.db import models
from django.contrib.auth.models import User

#  Model for TheLostItems
    # ItemID is a auto generated unique identification for each lost item.
        # Differen field for discriptiveness

class TheLostItems(models.Model):
    ItemID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name="Name of Item")
    description = models.TextField(verbose_name="Describe your Item")
    found = models.BooleanField(default=False, verbose_name="Found!")
    location = models.TextField(verbose_name="Lost Location")
    lost_date = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=17, verbose_name="Phone Number")
    email = models.EmailField(default="your@yahoo.com", verbose_name="Email Id")
    image = models.ImageField(upload_to='spot_items/images', default="", verbose_name="Image")
    found_location = models.TextField(verbose_name="Found Location")
    item_found_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_found_user", verbose_name="Found By", null=True, blank=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_reported_user", verbose_name="Reported By", null=True, blank=True)

    def __str__(self):
        return self.title
