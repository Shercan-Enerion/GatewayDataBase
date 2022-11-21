from fastapi import APIRouter
from fastapi import Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.bd import BaseData
import csv
from bson.objectid import ObjectId
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

web = APIRouter()
templates = Jinja2Templates(directory='templates')
controller = BaseData()


@web.on_event('startup')
async def startup():
    pass


@web.get('/')
async def index(request: Request):
    getData = controller.readData()
    base = list(getData).copy()
    for data in base:
        data['TimeStamp'] = ObjectId(data['_id']).generation_time
        data.pop('_id')
    keys = list(data.keys())
    keys.reverse()
    with open('data.csv', 'w', newline='') as csvFilefromMongodb:
        tuliscsv = csv.DictWriter(
            csvFilefromMongodb, fieldnames=keys, delimiter=",")
        tuliscsv.writeheader()
        tuliscsv.writerows(base)
        context = {'request': request}
    return templates.TemplateResponse('index.html', context)


@web.get("/get_csv")
async def get_csv():
    return FileResponse('data.csv', filename='data.csv')


@web.get("/get_registers")
async def get_registers():
    getData = controller.readData()
    base = list(getData).copy()
    for data in base:
        data['TimeStamp'] = ObjectId(data['_id']).generation_time
        data.pop('_id')
    base = jsonable_encoder(base)
    return JSONResponse(content=base)


@web.post('/addData')
async def webhook(request: dict):
    controller.sendData(request)
    return ''
