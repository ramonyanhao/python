from django.contrib import admin

from .models import Pizza,Topping
class ToppingAdmin(admin.ModelAdmin):
    fields = ('name', 'weidao')
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('zhishi',)
    fieldsets = (
        ['Main', {
            'fields': ('zhishi',),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('toppings',),
        }]

    )
    filter_horizontal = ('toppings',)#如果遇到ManyToManyField，这里很重要，filter_horizontal就是指定多对多关系的字段函数

admin.site.register(Pizza,PizzaAdmin)
admin.site.register(Topping,ToppingAdmin)
