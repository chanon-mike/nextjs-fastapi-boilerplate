from fastapi import APIRouter

router = APIRouter(
    prefix="/debug",
    tags=["debug"],
)


@router.get("/")
def test():
    return {"message": "test"}
