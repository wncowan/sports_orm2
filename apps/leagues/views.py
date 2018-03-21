from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray"),
		"players": Player.objects.filter(all_teams__location="Wichita").filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings")
		}	
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")