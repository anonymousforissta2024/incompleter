#Source: https://stackoverflow.com/questions/71058823/typeerror-unsupported-operand-types-for-set-and-set-returning-multiple
from fastapi import FastAPI
from riplir import generate_ad


app = FastAPI()


@app.get("/generate_snippet")
async def creative_ad_api(product_type: str, product_name: str , platform: str, audience: str):
    snippet = generate_ad({product_type} + {product_name} + {platform} + {audience})
    
    return {
        "message": snippet,
        }

# uvicorn riplir_api:app --reload