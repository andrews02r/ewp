from django.contrib import admin

# Register your models here.

from .models import Language, StreamTokenType, StreamType, Stream, \
Channel, PhoneBridge, Program, ScheduledProgram, Course
#Person, Group, Membership

class TimeFrameFilter(admin.SimpleListFilter):
    # https://docs.djangoproject.com/en/2.0/ref/contrib/admin/
    pass


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['label', 'stream_type', 'acl']
    ordering = ['label', 'stream_type']

@admin.register(PhoneBridge)
class PhoneBridgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'label','phone_number','participant_pin','host_pin','active']
    ordering = ['active','name']

@admin.register(ScheduledProgram)
class ScheduledProgramAdmin(admin.ModelAdmin):
    list_display = ['program','channel','start_date_and_time','end']
    ordering = ['start_date','start_time','channel']
    date_hierarchy = 'start_date'
    list_filter = ('channel','start_date',)
    search_fields = ['program__name', 'program__abbreviation']


admin.site.register(Language)
admin.site.register(StreamTokenType)
admin.site.register(StreamType)
admin.site.register(Channel)
admin.site.register(Program)
admin.site.register(Course)

#admin.site.register(Person)
#admin.site.register(Group)
#admin.site.register(Membership)

# admin.site.register(Stream, StreamAdmin)
# admin.site.register(PhoneBridge, PhoneBridgeAdmin)
# admin.site.register(ScheduledProgram, ScheduledProgramAdmin)