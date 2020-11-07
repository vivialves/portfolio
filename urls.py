from company.api.views import get_company_data
from company.api.viewsets import PaymentTermViewSet, CompanyDetailsViewSet, DepartmentViewSet, CompanyViewSet
from django.conf.urls import include, url

from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

company_router = routers.DefaultRouter()
company_router.register('paymentterm', PaymentTermViewSet, 
                        basename='paymentterm')

company_router.register('department', DepartmentViewSet,
                        basename='department')

company_router.register('company', CompanyViewSet,
                        basename='company')

company_router.register('companydetails', CompanyDetailsViewSet, 
                        basename='companydetails')

urlpatterns = [
    #Controle de token JWT
    url(r'^token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #internas
    url(r'^company/get_company_data$', get_company_data, name='get_company_data'),
    
    #externas
    url(r'^v1/company/', include((company_router.urls, 'company'), namespace='v1')),
]
