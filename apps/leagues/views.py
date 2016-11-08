from django.shortcuts import render, redirect
from .models import League, Team, Player

from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"special": Team.objects.annotate(Count('all_players'))
	}
	return render(request, "leagues/index.html", context)

def show_team(request, team_id):
	context = {
		"team": Team.objects.get(id=team_id)
	}
	return render(request, "leagues/show_team.html", context)

def show_player(request, player_id):
	context = {
		"player": Player.objects.get(id=player_id)
	}
	return render(request, "leagues/show_player.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")