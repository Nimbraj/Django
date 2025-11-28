from django.contrib import admin
from django.urls import path
from UPI import views as v1
from Insurance import views as v2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bh/", v1.BHIM),          # ✅ Added missing comma
    path("phone/", v1.phonepe),    # ✅ Added missing comma
    path("h1/", v2.HealthIns),     # ✅ Removed extra slash at start and added slash at end
]

