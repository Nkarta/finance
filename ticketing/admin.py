from django.contrib import admin

from .models import *
# Register your models here.

class FollowUpInline(admin.TabularInline):
	model=FollowUp
	fields=['date','title', 'text', 'attachment']
	readonly_fields=['date']
	extra=1

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	inlines=[FollowUpInline]

admin.site.register(Status)
admin.site.register(System)
admin.site.register(Priority)
