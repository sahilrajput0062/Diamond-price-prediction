from fastapi import FastAPI,Form
from fastapi.responses import JSONResponse
import util
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def load_artifacts():
    util.load_saved_artifacts()

app.add_event_handler("startup", load_artifacts)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_cut_values")
async def get_cut_values():
    response = JSONResponse(content={'cut': util.__cut_values})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.get("/get_color_values")
async def get_color_values():
    response = JSONResponse(content={'color': util.__color_values})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.get("/get_clarity_values")
async def get_clarity_values():
    response = JSONResponse(content={'clarity': util.__clarity_values})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.post("/predict_price")
async def predict_price(
    carat: float = Form(...),
    cut: str = Form(...),
    color: str = Form(...),
    clarity: str = Form(...),
    depth: float = Form(...),
    table: float = Form(...),
    x: float = Form(...),
    y: float = Form(...),
    z: float = Form(...),
):

    predicted_price = util.predict_price(carat, depth, table, x, y, z, cut, color, clarity)

    if predicted_price is not None:
        return JSONResponse(content={"predicted_price": predicted_price})
    else:
        return JSONResponse(content={"error": "Error during prediction"})
