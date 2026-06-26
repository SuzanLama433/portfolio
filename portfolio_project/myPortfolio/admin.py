from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Journey)
admin.site.register(Education)
admin.site.register(MyContact)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order",)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "order")
    ordering = ("category", "order")