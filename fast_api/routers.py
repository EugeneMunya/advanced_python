from fastapi import APIRouter

user_router=APIRouter(prefix="/user",tags=['User'])

@user_router.get("/detail")
def user_info():
    return "user details"