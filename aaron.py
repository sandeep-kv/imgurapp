import web
import requests
from random import randint
render = web.template.render('templates/')

urls = (
    '/', 'index'
)

class index:
    def GET(self):
    	i = web.input(name=0)
    	rand_number = randint(0,25) #Inclusive
    	headers = {"Authorization": "Client-ID e8913e738ba0511"}
    	r = requests.get('https://api.imgur.com/3/gallery/r/%s/'%i.name,headers = headers)
    	jj=r.json()
    	link = jj['data'][int(rand_number)]['link']
    	title = jj['data'][int(rand_number)]['title']
    	dic = {'link':link,'title':title}
        return render.index(dic)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()