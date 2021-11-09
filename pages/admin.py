from django.contrib import admin

from pages.models import ContactModel

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']


# @admin.register(DetailModel)
# class DetailModelAdmin(admin.ModelAdmin):
#     list_display = ['name2', 'email2', 'message2', 'phone2', 'created_at']
#     list_filter = ['created_at']
#     search_fields = ['name2', 'email2', 'message2', 'phone2']
