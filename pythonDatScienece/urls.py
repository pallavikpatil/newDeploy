from rest_framework.routers import DefaultRouter
from pythonDatScienece.views import *

from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
# router.register(r'etcStudents',StudentsVset,basename='etcStudents')
router.register(r'etcFaculty',FacultyVset)

urlpatterns = router.urls
