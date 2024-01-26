from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_confirmed')
	search_fields = ('email', 'username', 'first_name', 'last_name')
	readonly_fields = ('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter=()
	fieldsets=()
	
admin.site.register(Account, AccountAdmin)
admin.site.register(PrincipalProfile)
admin.site.register(School)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(MinisterProfile)
admin.site.register(CommissionerProfile)
admin.site.register(FedralDistrictHeadProfile)
admin.site.register(StateDistrictHeadProfile)
admin.site.register(Ministeroffice)
admin.site.register(Commisioneroffice)
admin.site.register(FedralDistrictoffice)
admin.site.register(StateDistrictoffice)
admin.site.register(OfficeofMinisterstaffProfile)
admin.site.register(OfficeofCommisionerstaffProfile)
admin.site.register(OfficeofFedDistrictstaffProfile)
admin.site.register(OfficeofStateDistrictstaffProfile)
admin.site.register(Post)