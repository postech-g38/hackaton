from fastapi import APIRouter

from src.routes.v1.appointment_route import router as appointment_router
from src.routes.v1.record_route import router as record_router
from src.routes.v1.doctor_route import router as doctor_router

router = APIRouter(prefix='/v1')


router.include_router(appointment_router)
router.include_router(record_router)
router.include_router(doctor_router)
