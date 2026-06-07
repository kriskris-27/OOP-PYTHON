from fastapi import APIRouter


router = APIRouter() # Router object

@router.get("/health")

def health_check():
    return {"status":"healthy"}

def get_user_service():
    return UserService()  # Returns an object

@router.get("/users")
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()