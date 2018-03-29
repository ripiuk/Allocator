import os
from aiohttp import web
import aiohttp_jinja2


class Allocate(web.View):

    @aiohttp_jinja2.template('allocate.html')
    async def get(self):
        return {'img_paths': self.request.app['media_files'][0]}

    @aiohttp_jinja2.template('allocate.html')
    async def post(self):
        pass
