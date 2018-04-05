import os
import json

from aiohttp import web
import aiohttp_jinja2


async def redirect(request, router_name):
    url = request.app.router[router_name].url_for()
    raise web.HTTPFound(url)


class Allocate(web.View):

    @aiohttp_jinja2.template('allocate.html')
    async def get(self):
        # update the list of media files every time
        self.request.app['media_files'] = ['media{}/{}'.format(
            path.split('media')[-1] if path.split('media')[-1] != '/' else '', name)
            for path, subdirs, files in os.walk(self.request.app['base_dir']) for name in files]

        return {'images': self.request.app['media_files']}

    @aiohttp_jinja2.template('allocate.html')
    async def post(self):
        data = await self.request.post()
        with open('result.json', 'w+', encoding='utf8') as file:
            json.dump(dict(data), file, ensure_ascii=False)

        await redirect(self.request, 'save')


class Save(web.View):

    @aiohttp_jinja2.template('save.html')
    async def get(self):
        pass

    @aiohttp_jinja2.template('save.html')
    async def post(self):
        with open('result.json', 'r', encoding='utf8') as file:
            data = json.loads(file.readline())

        base_dir = os.path.abspath(os.path.join(self.request.app['base_dir'], '..'))

        for path, prefix in data.items():
            destination_path = '{base}/{media_dir}/res_{prefix}/{file}'.format(
                base=base_dir, media_dir='media', prefix=prefix, file=os.path.basename(path))
            if not os.path.exists(os.path.dirname(destination_path)):
                os.makedirs(os.path.dirname(destination_path))
            os.rename('{base}/{in_media}'.format(base=base_dir, in_media=path), destination_path)

        await redirect(self.request, 'allocate')
