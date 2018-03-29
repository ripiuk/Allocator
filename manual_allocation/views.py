from aiohttp import web
import aiohttp_jinja2


class Allocate(web.View):

    @aiohttp_jinja2.template('allocate.html')
    async def get(self):
        pass

    @aiohttp_jinja2.template('allocate.html')
    async def post(self):
        pass
