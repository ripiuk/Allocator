import os
import json

from aiohttp import web
import aiohttp_jinja2


def redirect(request, router_name):
    url = request.app.router[router_name].url_for()
    raise web.HTTPFound(url)


class Allocate(web.View):

    @aiohttp_jinja2.template('allocate.html')
    async def get(self):
        # update the list of media files every time
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'media'))

        self.request.app['media_files'] = ['media{}/{}'.format(
            path.split('media')[-1] if path.split('media')[-1] != '/' else '', name)
            for path, subdirs, files in os.walk(base_dir) for name in files]

        return {'images': self.request.app['media_files']}

    @aiohttp_jinja2.template('allocate.html')
    async def post(self):
        data = await self.request.post()
        with open('result.json', 'w+', encoding='utf8') as file:
            json.dump(dict(data), file, ensure_ascii=False)

        redirect(self.request, 'save')


class Save(web.View):

    @aiohttp_jinja2.template('save.html')
    async def get(self):
        pass

    @aiohttp_jinja2.template('save.html')
    async def post(self):
        with open('result.json', 'r', encoding='utf8') as file:
            data = file.readline()
            print(json.loads(data))
