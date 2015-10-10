from django.db import models


class Content(models.Model):
	title = models.CharField(max_length=500)
	subtitle = models.CharField(max_length=500)
	contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
	pub_date = models.DateTimeField('date published')


class Article(Content):
	text = models.TextField()

	def show(self):
		return "\"" + str(self.title) + ": " + str(self.subtitle) + \
		       ",\" by " + ''.join(str(e) for e in self.contributors) + \
		       ". Article published on " + str(self.pub_date) + ".\n"


class Image(Content):
	path = models.FilePathField()

	def info(self):
		return "\"" + str(self.title) + ": " + str(self.subtitle) + \
		       ",\" by " + ''.join(str(e) for e in self.contributors) + \
		       ". Image published on " + str(self.pub_date) + ".\n"


class Contributor(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	contents = models.ManyToManyField('Content', related_name='contributor')

	def die(self):
		Contributor.objects.get(first_name = self.first_name,
		                        last_name = self.last_name).delete()