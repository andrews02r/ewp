from django.db import models

# Create your models here.

class SoftwareVendor(models.Model):
    vendor = models.CharField(
        max_length = 75,
        help_text = "Microsoft"
    )
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.vendor

class SoftwareProduct(models.Model):    
    name = models.CharField(
        max_length = 75,
        help_text = "Windows Server Standard Edition"
    )
    version = models.CharField(
        max_length = 20,
        help_text = "2017"
    )
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class HardwareVendor(models.Model):
    name = models.CharField(
        max_length = 75,
        help_text = "Cisco"
    )
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class WebcastEncoder(models.Model):
    """
    Model representing a stream type
    """
    name = models.CharField(
        max_length = 100, 
        help_text = "Enter the stream type name",
    )
    description = models.CharField(
        max_length = 200, 
        help_text = "Enter a short description",
    )
    vendor = models.ForeignKey(
        HardwareVendor,
    )
    ip_address = models.CharField(
        max_length = 12,
        help_text = "ex. 192.168.0.1",
        blank = True,
        null = True,
    )
    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name     