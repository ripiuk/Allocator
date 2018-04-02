import csv
from aiohttp import web
import aiohttp_jinja2


def redirect(request, router_name):
    # TODO: Check this
    url = request.app.router[router_name].url()
    raise web.HTTPFound(url)


class Allocate(web.View):

    @aiohttp_jinja2.template('allocate.html')
    async def get(self):
        self.request.app['image_number'] = 0
        image_number = self.request.app['image_number']
        return {'img_paths': self.request.app['media_files'][image_number]}

    @aiohttp_jinja2.template('allocate.html')
    async def post(self):
        self.request.app['image_number'] += 1
        image_number = self.request.app['image_number']
        if image_number >= len(self.request.app['media_files']):
            redirect(self.request, 'save')
        # TODO: save is it hotel ot not in dict
        return {'img_paths': self.request.app['media_files'][image_number]}


class SaveAllocation(web.View):

    @aiohttp_jinja2.template('save.html')
    async def get(self):
        with open('result.csv', 'w+') as file:
            writer = csv.writer(file)
            # TODO: write dict to the file here
