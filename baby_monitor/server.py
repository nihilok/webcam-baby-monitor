from fastapi import FastAPI
from starlette.responses import StreamingResponse, HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

from .camera import gen_frames, switch_on_off

app = FastAPI()


# @app.get("/")
# async def index():
#     return HTMLResponse(
#         '''
# <html>
# <head>
# <script crossorigin src="https://unpkg.com/react@16/umd/react.development.js"></script>
# <script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
# <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
# </head><body>
# <center>
#     <img src="/video">
# </center>
# <center>
#     <a href="/cam">ON/OFF</a>
# </center>
# <div id='root'></div>
# <script>
# const elem = <h1>Hello World!</h1>
# ReactDOM.render(elem, document.getElementById('root'))
# </script>
# </body></html>
#         '''
#     )


@app.get("/cam")
async def switch_cam():
    switch_on_off()
    return RedirectResponse("/")


@app.get("/video")
async def video():
    return StreamingResponse(
        gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame"
    )

app.mount(
    "/", StaticFiles(directory="./baby-monitor-react/build", html=True), name="app"
)
