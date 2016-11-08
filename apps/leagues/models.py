from django.db import models

class League(models.Model):
	name = models.CharField(max_length=50)
	sport = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Team(models.Model):
	location = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)
	league = models.ForeignKey(League, related_name="teams")

	def past_players(self):
		return Player.objects.filter(all_teams=self).exclude(curr_team=self)

	def __str__(self):
		return "{} {}".format(self.location, self.team_name)

class Player(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	curr_team = models.ForeignKey(Team, related_name="curr_players")
	all_teams = models.ManyToManyField(Team, related_name="all_players")

	def past_teams(self):
		return self.all_teams.exclude(id=self.curr_team.id)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)
