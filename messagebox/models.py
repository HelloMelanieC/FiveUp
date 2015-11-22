from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Message(models.Model):

	recipient = models.ForeignKey('fuauth.User', related_name='messages')
	sender_name = models.CharField(
		max_length = 35
	)
	message_text = models.TextField(
		max_length=125
	)
	created_date = models.DateTimeField(auto_now=True)
	message_sent = models.BooleanField(default=False)

	def __str__(self):
		''' Gets a readable string of sender name and created_date
		to refer to the message by '''
		return '_'.join([
			self.sender_name,
			str(self.created_date)
		])

#This *may* be used to list the messages in detail. 
	def get_absolute_url(self):
		''' returns a reference for the message'''
		# TODO Create message detail view
		return reverse('add-message-success') #, kwargs={'pk': self.id} ?



