from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from orderable.models import Orderable


# STATUS_CHOICES = (
# 	('NEW', 'NEW'),
# 	('TODO', 'TODO'),
# 	('IN PROGRESS', 'IN PROGRESS'),
# 	('WAITING', 'WAITING'),
# 	('COMPLETE', 'COMPLETE'),
# 	)

class Status(Orderable):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class System(Orderable):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Priority(Orderable):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Ticket(models.Model):
	system = models.ForeignKey(System, on_delete=models.CASCADE, 
		null=True,
		blank=True)
	priority = models.ForeignKey(Priority, on_delete=models.CASCADE, 
		null=True,
		blank=True)
	title = models.CharField('Title', max_length=255)
	owner = models.ForeignKey(User,
		related_name='owner',
		blank=True,
		null=True,
		verbose_name='Owner',
		on_delete=models.CASCADE)
	description = models.TextField('Description', blank=True, null=True)
	status = models.ForeignKey(Status, on_delete=models.CASCADE)
	waiting_for = models.ForeignKey(User,
		related_name='waiting_for',
		blank=True,
		null=True,
		verbose_name='Waiting For',
		on_delete=models.CASCADE)
	# set in view when status changed to "DONE"
	assigned_to = models.ForeignKey(User,
		related_name='assigned_to',
		blank=True,
		null=True,
		verbose_name='Assigned to',
		on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	due = models.DateField(blank=True, null=True)
	closed = models.DateField(blank=True, null=True)
	def __unicode__(self):
		return str(self.id)


class FollowUp(models.Model):
	"""
	A FollowUp is a comment to a ticket.
	"""
	ticket = models.ForeignKey(Ticket, verbose_name='Ticket',
		on_delete=models.CASCADE)
	date = models.DateTimeField('Date', default=timezone.now)
	title = models.CharField('Title', max_length=200,)
	text = models.TextField('Text', blank=True, null=True,)
	user = models.ForeignKey(User, blank=True, null=True, verbose_name='User',
		on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	# comments = models.TextField(null=True, blank=True)	
	attachment = models.FileField(null=True, 
		blank=True, 
		upload_to='ticketing/attachments/')
	class Meta:
		ordering = ['-modified', ]

