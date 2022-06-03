from aiohttp import web 
import asyncio
import json
from config import *
from random import choice
from pymongo import MongoClient


db = MongoClient(DB)['logo']['Logo']


routes = web.RouteTableDef()

async def _get_iamges():
    list = choice([m['url'] for m in db.find()])
    return list
   


    
@routes.get("/")
async def base_page(r):
    response_obj = { 'HEY' : 'WELCUM' }
    return web.Response(text=json.dumps(response_obj))

@routes.get("/images")
async def images(r):
    response_obj = { 'status' : 'success' }
    response_obj['images'] = await _get_iamges()
    return web.Response(text=json.dumps(response_obj))

async def start_server():
    port = PORT
    app = web.Application()
    app.add_routes(routes)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", port).start()



asyncio.get_event_loop().run_until_complete(start_server())

