from core.utils import include_mask
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

from integration.utils import has_rest_integration
from participant_function.data_validators.br_identifiers.cnpj import validate_cnpj
from participant_function.data_validators.br_identifiers.cpf import validate_cpf

from ..models import Address, Company, Department, PaymentTerm
from ..utils import get_office_group, payment_term_list, get_office_group_profile
from django.shortcuts import get_object_or_404


class PaymentTermSerializer(ModelSerializer):
    """ Serializer para as condições de pagamento permitidas pelo cliente """

    class Meta:
        model = PaymentTerm
        fields = ("id_payment_term", "office_group", "description", "erp_code")
        required_fields = ("description",)

    def validate(self, attrs):
        request = self.context["request"]
        office_group = get_office_group(user=request.user)
        if not office_group.id_office_group == self.initial_data.get("office_group"):
            raise ValidationError(
                "Not permitted create or update or delete office group different of user office groups"
            )

        has_integration = has_rest_integration(office_group)
        if not has_integration:
            raise ValidationError(
                "Integration not permitted"
            )
        return attrs


class CompanySerializer(serializers.ModelSerializer):
    """ Serializer para manter Empresas """
    address = serializers.SerializerMethodField('get_address')

    # trazendo address para o get do company
    def get_address(self, obj):
        address_instances = Address.objects.filter(
            company=obj.pk
        )
        serializer = AddressSerializer(instance=address_instances,
                                       many=True,
                                       allow_null=True)
        return serializer.data

    # if we need to edit a field that is a nested serializer,
    # we must override to_internal_value method
    def to_internal_value(self, data):
        if data.get('id'):
            return get_object_or_404(CompanySerializer, pk=data['pk'])
        return super(CompanySerializer, self).to_internal_value(data)

    # Configurando o POST com Address
    def create(self, validated_data):
        addresses_data = self.initial_data.pop('address')
        company = Company.objects.create(**validated_data)
        for address_data in addresses_data:
            Address.objects.create(company=company, **address_data)
        return company

    # altera o PUT mas é barrado pelas validações
    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('address')
        addresses = instance.address_company.all()
        addresses = list(addresses)
        instance.fantasy_name = validated_data.get('fantasy_name', instance.fantasy_name)
        instance.state_registration = validated_data.get('state_registration', instance.state_registration)
        instance.financial_email = validated_data.get('financial_email', instance.financial_email)
        instance.financial_email_2 = validated_data.get('financial_email_2', instance.financial_email_2)
        instance.comercial_email = validated_data.get('comercial_email', instance.comercial_email)
        instance.comercial_email_2 = validated_data.get('comercial_email_2', instance.comercial_email_2)
        instance.financial_phone = validated_data.get('financial_phone', instance.financial_phone)
        instance.comercial_phone = validated_data.get('comercial_phone', instance.comercial_phone)
        instance.logo_url = validated_data.get('logo_url', instance.logo_url)
        instance.save()
        for address_data in addresses_data:
            address = addresses.pop(0)
            address.description = address_data.get('description', address.description)
            address.municipal_registration = address_data.get('municipal_registration', address.municipal_registration)
            address.zip_code = address_data.get('zip_code', address.zip_code)
            address.address = address_data.get('address', address.address)
            address.number = address_data.get('number', address.number)
            address.complement = address_data.get('complement', address.complement)
            address.neighborhood = address_data.get('neighborhood', address.neighborhood)
            address.city = address_data.get('city', address.city)
            address.federated_unit = address_data.get('federated_unit', address.federated_unit)
            address.save()
        return instance

    class Meta:
        model = Company
        fields = '__all__'
        # required_fields = ("description",)

    def validate(self, attrs):
        request = self.context["request"]
        office_group = get_office_group(user=request.user)
        if not office_group.id_office_group == self.initial_data.get("office_group"):
            raise ValidationError(
                "Not permitted create or update or delete office group different of user office groups"
            )

        # Item 1 -- Verificando o profile do office Group
        office_group_profile = get_office_group_profile(user=request.user)
        if 'profile' in request.data:
            if office_group_profile == request.data['profile'] or office_group_profile == 'BOTH':
                pass
            else:
                raise ValidationError(
                    "Not permitted create or update office group profile different of user office groups"
                )
        # Item 2, 3 e 4 --- Validação CPF e CNPJ
        if request.data['kind'] == 'PF' and validate_cpf(request.data['cpf']) == True \
                or request.data['kind'] == 'PJ' and validate_cnpj(request.data['cnpj']) == True:
            pass
        else:
            raise ValidationError(
                "CNPJ or CPF has been inapropriated"
            )

        if request.data['kind'] == 'PF' and Company.objects.filter(cpf=request.data['cpf']).exists() or \
                request.data['kind'] =='PJ' and Company.objects.filter(cnpj=request.data['cnpj']).exists:
            raise ValidationError(
                "CNPJ or CPF has been used"
            )

        # Item 5 --- Impedindo envio do Status
        if 'status' not in request.data:
            pass
        else:
            raise ValidationError(
                "Not permitted send field: 'status = ACTIVE'"
            )

        # Item 6 e 7 --- is_billing_address = True
        if request.data['address'][0]['zip_code'] is None and \
                request.data['address'][0]['address'] is None and \
                request.data['address'][0]['number'] is None and \
                request.data['address'][0]['neighborhood'] is None and \
                request.data['address'][0]['city'] is None and \
                request.data['address'][0]['federated_unit'] is None:
            raise ValidationError(
                "Not permitted send field: 'address = empty'"
            )

        if request.data['address'][0]['is_billing_address'] != True:
            request.data['address'][0]['is_billing_address'] = True

        has_integration = has_rest_integration(office_group)
        if not has_integration:
            raise ValidationError(
                "Integration not permitted"
            )

        return attrs


class DepartmentSerializer(ModelSerializer):
    """ Serializer para manter Departamentos """

    class Meta:
        model = Department
        fields = '__all__'
        required_fields = ("description",)

    def validate(self, attrs):
        request = self.context["request"]
        office_group = get_office_group(user=request.user)
        if not office_group.id_office_group == self.initial_data.get("office_group"):
            raise ValidationError(
                "Not permitted create or update or delete office group different of user office groups"
            )

        has_integration = has_rest_integration(office_group)
        if not has_integration:
            raise ValidationError(
                "Integration not permitted"
            )

        return attrs


class AddressSerializer(ModelSerializer):
    """ Serializer para manter Endereços """

    class Meta:
        model = Address
        fields = '__all__'
        # required_fields = ("description",)

    def validate(self, attrs):
        request = self.context["request"]
        office_group = get_office_group(user=request.user)
        if not office_group.id_office_group == self.initial_data.get("office_group"):
            raise ValidationError(
                "Not permitted create or update or delete office group different of user office groups"
            )
        return attrs


# --- Ajax customizado

class CompanyDetailsSerializer(ModelSerializer):
    """ Serializer para exibir popup com detalhes das Companies """
    company_render = serializers.SerializerMethodField()

    def get_company_render(self, company):
        ''' HTML para o modal de empresa. Monta o dict com as informações para o contexto e manda para o template '''
        if company:
            # TODO: Montar essa dict com o método da company.utils
            context = {
                'logo_url': company.logo_url.url if company.logo_url else '',
                'id_company': company.id_company,
                'cnpj': include_mask(company.cnpj, "CNPJ") if company.cnpj else '',
                'cpf': include_mask(company.cpf, "CPF") if company.cpf else '',
                'state_registration': company.state_registration,
                'fantasy_name': company.fantasy_name,
                'name': company.name,
                'comercial_email': company.comercial_email if company.comercial_email else '',
                'comercial_email_2': company.comercial_email_2 if company.comercial_email_2 else '',
                'comercial_phone': include_mask(company.comercial_phone, "PHONE") if company.comercial_phone else '',
                'financial_phone': include_mask(company.financial_phone, "PHONE") if company.financial_phone else '',
                'city': company.city,
                'main_zip_code': company.main_zip_code,
                'main_address': company.main_address
            }
            return [
                render_to_string(
                    'company/includes/company_details.html',
                    context
                )
            ]
        return ''

    class Meta:
        model = Company
        fields = ['company_render', ]
