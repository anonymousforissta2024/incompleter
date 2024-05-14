#Source: https://stackoverflow.com/questions/73841032/fastapi-router-type-error-untyped-decorator-males-function-untyped
router = APIRouter()

@router.post("/overview/{location_id}")
async def get_overview(location_id: str) -> object:
    if 4 not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return overview