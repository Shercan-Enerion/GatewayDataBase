# -------------------------------------modules-----------------------------
import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.main import web
from config.var_env import mode


app = FastAPI(title='Server Enerion',
              description='Server Enerion data', version='0.0.1')
templates = Jinja2Templates(directory='templates')
app.include_router(web)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    if mode == 'TEST':
        uvicorn.run('app:app', log_level='info', access_log=False, reload=True)
    else:
        uvicorn.run(app='app:app', host='0.0.0.0', port=80,
                    log_level='info', access_log=False)
