import os
import json

from aiohttp import web
import aiohttp_jinja2


async def redirect(request, router_name):
    url = request.app.router[router_name].url_for()
    raise web.HTTPFound(url)


class Tune(web.View):

    @aiohttp_jinja2.template('tune.html')
    async def get(self):
        pass

    async def post(self):
        path = '/allocating'
        response = web.HTTPFound(path)
        data = await self.request.post()
        response.set_cookie(name='buttons', value=json.dumps(dict(data), ensure_ascii=False), path=path)
        return response


class Allocate(web.View):

    @aiohttp_jinja2.template('allocate.html')
    async def get(self):
        buttons = json.loads(self.request.cookies.get('buttons', '{"1": "No", "2": "Yes"}'))
        # update the list of media files every time
        self.request.app['media_files'] = ['media{}/{}'.format(
            path.split('media')[-1] if path.split('media')[-1] != '/' else '', name)
            for path, subdirs, files in os.walk(self.request.app['base_dir']) for name in files]

        return {'images': self.request.app['media_files'], 'buttons': buttons}

    async def post(self):
        router_name = 'save'
        response = web.HTTPFound(self.request.app.router[router_name].url_for())
        data = await self.request.post()

        with open('result.json', 'w+', encoding='utf8') as file:
            json.dump(dict(data), file, ensure_ascii=False)

        return response


class Save(web.View):

    @aiohttp_jinja2.template('save.html')
    async def get(self):
        pass

    async def post(self):
        response = web.HTTPFound('/')
        response.del_cookie('buttons', path='/allocating')

        with open('result.json', 'r', encoding='utf8') as file:
            data = json.loads(file.readline())

        base_dir = os.path.abspath(os.path.join(self.request.app['base_dir'], '..'))

        for path, prefix in data.items():
            destination_path = '{base}/{media_dir}/results/{prefix}/{file}'.format(
                base=base_dir, media_dir='media', prefix=prefix, file=os.path.basename(path))
            if not os.path.exists(os.path.dirname(destination_path)):
                os.makedirs(os.path.dirname(destination_path))
            os.rename('{base}/{in_media}'.format(base=base_dir, in_media=path), destination_path)
        # TODO: delete all empty dirs

        return response
