from django.contrib import admin
from rango.models import Tapa,Bar,UserProfile

class TapasAdmin(admin.ModelAdmin):
	list_display = ('nombre_tapa','descripcion','imagen')
	search_fields = ("nombre_tapa",)
	list_editable = ('descripcion','imagen')

class BaresAdmin(admin.ModelAdmin):
	list_display = ('nombre_bar','slug','direccion','descripcion_bar')
	list_editable = ('descripcion_bar','direccion')
	search_fields = ('nombre_bar',)
	filter_horizontal = ('tapas',)
	list_filter = ('tapas',)


class UserAdmin(admin.ModelAdmin):
	list_display = ('user', 'picture')


admin.site.register(Tapa, TapasAdmin)
admin.site.register(Bar, BaresAdmin)
admin.site.register(UserProfile,UserAdmin)

