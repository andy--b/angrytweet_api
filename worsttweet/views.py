from django.shortcuts import render, redirect
from find_extreme_tweets import extreme_tweets
import re

def home_page(request):
	return render(request, 'home.html')
	
def new_search(request):
	search_term = request.POST['search_text']
	formatted_url = re.sub(r'\W', '', search_term.replace(' ', '_'))
	return redirect('/mean/search/%s/' % (formatted_url,))
	
def search_result(request, formatted_url):
	search_term = formatted_url.replace('_', ' ')
	extreme_ids = extreme_tweets(search_term)
	if 0 in extreme_ids:
		return redirect('/insufficient/')
	return render(request, 'results.html', {'extreme_ids': extreme_ids})

def insufficient(request):
	return render('insufficient.html')