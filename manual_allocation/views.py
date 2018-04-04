from aiohttp import web
import aiohttp_jinja2


def redirect(request, router_name):
    url = request.app.router[router_name].url_for()
    raise web.HTTPFound(url)


class Allocate(web.View):

    @aiohttp_jinja2.template('allocate.html')
    async def get(self):
        return {'images': self.request.app['media_files']}

    @aiohttp_jinja2.template('allocate.html')
    async def post(self):
        pass
