from django.contrib import admin
from .models import Profile, Skill, Project, Education, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'github']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['order', 'proficiency']
    list_filter = ['category']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'featured', 'order']
    list_editable = ['featured', 'order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'degree', 'year_start', 'year_end']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sent_at', 'is_read']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'message', 'sent_at']
