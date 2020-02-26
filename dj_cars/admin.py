from django.contrib import admin

from .models import Car, Make

admin.site.site_header = 'Коли'
admin.site.site_title = 'Админ част'
admin.site.index_title = 'Добре дошли в админ частта'


class CarInline(admin.TabularInline):
    model = Car
    extra = 3


class CarAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['car_make']}),
                 ('Date info', {'fields': ['pub_date'], 'classes':
                     ['collapse']}), ]
    inlines = [CarInline]


'''
admin.site.register(Car)
admin.site.register(Make)
'''
admin.site.register(Car)
admin.site.register(Make, CarAdmin)
