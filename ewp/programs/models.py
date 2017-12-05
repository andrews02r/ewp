from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class Language(models.Model):
    """
    Language
    """
    name = models.CharField(
        max_length = 10, 
        help_text = "Enter the lange name",
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name    

#################################
#            Bridges
#################################
class PhoneBridge(models.Model):
    """
    Language
    """
    name = models.CharField(
        max_length = 100, 
        help_text = "Enter the phone bridge name",
    )
    label = models.CharField(
        max_length = 100, 
        help_text = "Enter the phone bridge label",
    )    
    phone_number = models.CharField(
        max_length = 30, 
        help_text = "Enter the phone bridge number",
    )
    participant_pin = models.CharField(
        max_length = 10, 
        help_text = "Enter the phone bridge participant access code",
    )
    host_pin = models.CharField(
        max_length = 10, 
        help_text = "Enter the phone bridge host code",
    )
    active = models.BooleanField(
        default = True,
    )
    #channels = models.ManyToManyField(Channel)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name     


#################################
#           FLAGS
#################################


#################################
#      Business Warehouse
#################################
class Course(models.Model):
    name = models.CharField(
        max_length = 100,
        blank = True,
        null = True,
    )
    abbreviation = models.CharField(
        max_length = 10,
        blank = True,
        null = True,
    )
    number = models.IntegerField(
        blank = True,
        null = True,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name  

#################################
#            STREAMS
#################################
class StreamTokenType(models.Model):
    """
    Language
    """
    name = models.CharField(
        max_length = 10, 
        help_text = "Enter the token type name",
    )
    active = models.BooleanField(
        default = True,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name    

class StreamType(models.Model):
    """
    Model representing a stream type
    """
    name = models.CharField(
        max_length = 10, 
        help_text = "Enter the stream type name",
    )
    description = models.CharField(
        max_length = 200, 
        help_text = "Enter a short description",
    ) 
    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name    

class Stream(models.Model):
    """
    Model representing a stream
    """
    label = models.CharField(
        max_length = 200, 
        help_text = "Enter the stream name",
    )
    description = models.CharField(
        max_length = 200, 
        help_text = "Enter a short description.", 
        null = True, 
        blank = True,
    ) 
    uri = models.CharField(
        max_length = 200, 
        help_text = "Enter the stream's uri",
    ) 
    alternate_uri = models.CharField(
        max_length = 200, 
        help_text = "enter the streams alternate uri.", 
        null = True, 
        blank = True,
    )
    stream_type = models.ForeignKey(
        'StreamType', 
        on_delete = models.CASCADE,
    )
    stream_language = models.ForeignKey(
        'Language', 
        on_delete = models.SET_NULL, 
        null = True,
    )    
    acl = models.CharField(
        max_length=200, 
        help_text = "Enter the stream name", 
        null = True, 
        blank = True,
    )
    token_config = models.ForeignKey(
        'StreamTokenType', 
        on_delete = models.SET_NULL, 
        null = True, 
        blank = True,
    )
    internal_only = models.BooleanField(
        default=False,
    )
    active = models.BooleanField(
        default = True,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.label

#################################
#           CHANNEL        
#################################

class Channel(models.Model):
    LIVE = 'live'
    ON_AIR = 'on-air'
    OFF_AIR = 'off-air'
    CHANNEL_STATUS_CHOICES = (
        (LIVE,'Live'),
        (ON_AIR,'On Air'),
        (OFF_AIR, 'Off Air'),
    )

    active = models.BooleanField(
        default = True,
    )
    name = models.CharField(
        max_length = 10, 
        help_text = "Enter the channel name",
    )
    abbreviation = models.CharField(
        max_length = 10, 
        help_text = "Enter the abbreviation here",
    )
    private = models.BooleanField(
        default = False,
    )
    description = models.TextField(
        null = True, 
        blank = True,
    )
    status = models.CharField(
        max_length = 10,
        choices = CHANNEL_STATUS_CHOICES,
        default = ON_AIR,
    )
    streams = models.ManyToManyField(
        Stream,
    )

    phone_bridges = models.ManyToManyField(
        PhoneBridge,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name  

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'

#################################
#           Programs        
#################################
class Program(models.Model):
    name = models.CharField(
        max_length = 250, 
        help_text = "Enter the program name",
    )
    abbreviation = models.CharField(
        max_length = 100,
        help_text = "Program abbreviation",
    )
    description = models.TextField(
        blank = True,
        null = True,
    )
    this_program_is_a_course = models.BooleanField(
        default = False,
    )
    associated_course = models.ForeignKey(
        Course,
        null = True,
        blank = True,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name  

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'


class ScheduledProgram(models.Model):
    program = models.ForeignKey(
        Program,
    )
    channel = models.ForeignKey(
        Channel,
        on_delete = models.PROTECT,
    )
    start_date = models.DateField(

    )
    start_time = models.TimeField(

    )
    duration = models.DurationField(
        default = timedelta(minutes=60),
        help_text = '(minutes)',
    )
    
    @property
    def start_date_and_time(self):
        start_date_and_time = datetime.combine(self.start_date, self.start_time)
        return start_date_and_time

    @property
    def end(self):
        start_date_and_time = datetime.combine(self.start_date, self.start_time)
        return start_date_and_time + self.duration

    @property
    def name(self):
        # Any expensive calculation on instance data
        return self.program.name

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name  

    # class Meta:
    #     verbose_name = 'Scheduled Program'
    #     verbose_name_plural = 'Scheduled Programs'

