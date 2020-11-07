
from core.api.permissions import CustomDjangoObjectPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, response, status, viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import PaymentTermSerializer, CompanyDetailsSerializer, CompanySerializer, DepartmentSerializer
from ..utils import get_office_group, payment_term_list, department_list, company_list
from ..models import Company, PaymentTerm, Department, Address


class PaymentTermViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite condições de pagamento serem mantidas
    pelos Compradores
    """
    permission_classes = [CustomDjangoObjectPermissions]
    filterset_fields = ['description', 'erp_code']
    ordering_fields = '__all__'
    search_fields = ['^description', 'erp_code']

    def get_queryset(self):
        """ Filtro de objs """
        return payment_term_list(user=self.request.user)

    def get_serializer_class(self):
        """ para controlar versionamentos """
        if self.request.version == 'v1':
            return PaymentTermSerializer

    # Alterando o create para enviar o office group
    def create(self, request, *args, **kwargs):
        data = request.data

        user_office_group = get_office_group(user=request.user)
        data['office_group'] = user_office_group.pk

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        description = request.data['description']
        erp_code = request.data['erp_code']
        obj = PaymentTerm.objects.get(id_payment_term=kwargs['pk'])
        obj.description = description
        obj.erp_code = erp_code
        obj.save()
        return response.Response(status=status.HTTP_200_OK)

# ---- Ajax customizado

class CompanyDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Ajax para modal com dados de Empresa
    """
    serializer_class = CompanyDetailsSerializer

    def get_queryset(self):
        """ Filtro de objs """
        company_pk = self.request.query_params.get('company_pk')

        if company_pk:
            return Company.objects.filter(pk=company_pk)
        else:
            return Company.objects.none()

# ----


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que departamento seja mantido
    pelos Compradores
    """
    permission_classes = [CustomDjangoObjectPermissions]
    filterset_fields = ['description', 'erp_code']
    ordering_fields = '__all__'
    search_fields = ['^description', 'erp_code']

    def get_queryset(self):
        """ Filtro de objs """
        return department_list(user=self.request.user)

    def get_serializer_class(self):
        """ para controlar versionamentos """
        if self.request.version == 'v1':
            return DepartmentSerializer

    # Alterando o create para enviar o office group
    def create(self, request, *args, **kwargs):
        data = request.data

        user_office_group = get_office_group(user=request.user)
        data['office_group'] = user_office_group.pk

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        description = request.data['description']
        erp_code = request.data['erp_code']
        obj = Department.objects.get(id_department=kwargs['pk'])
        obj.description = description
        obj.erp_code = erp_code
        obj.save()
        return response.Response(status=status.HTTP_200_OK)


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que os dados das empresas sejam mantidas
    pelos Compradores
    """
    permission_classes = [CustomDjangoObjectPermissions]
    filterset_fields = ['kind', 'cpf', 'cnpj', 'state_registration']
    ordering_fields = '__all__'
    search_fields = ['^kind', 'cpf', 'cnpj', 'state_registration']

    def get_queryset(self):
        """ Filtro de objs """
        return company_list(user=self.request.user)

    def get_serializer_class(self):
        """ para controlar versionamentos """
        if self.request.version == 'v1':
            return CompanySerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        user_office_group = get_office_group(user=request.user)
        data['office_group'] = user_office_group.pk

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Faz a atualização do company, porém não faz do address.
    def update(self, request, *args, **kwargs):
        fantasy_name = request.data['fantasy_name']
        state_registration = request.data['state_registration']
        financial_email = request.data['financial_email']
        financial_email_2 = request.data['financial_email_2']
        comercial_email = request.data['comercial_email']
        comercial_email_2 = request.data['comercial_email_2']
        financial_phone = request.data['financial_phone']
        comercial_phone = request.data['comercial_phone']
        obj = Company.objects.get(id_company=kwargs['pk'])
        obj.fantasy_name = fantasy_name
        obj.state_registration = state_registration
        obj.financial_email = financial_email
        obj.financial_email_2 = financial_email_2
        obj.comercial_email = comercial_email
        obj.comercial_email_2 = comercial_email_2
        obj.financial_phone = financial_phone
        obj.comercial_phone = comercial_phone
        obj.save()

        return response.Response(status=status.HTTP_200_OK)
