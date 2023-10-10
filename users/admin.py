from django.contrib import admin

# Register your models here.

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)