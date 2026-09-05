from django.contrib import admin
from .models import (
    Profile,
    Education,
    WorkExperience,
    Skill,
    Project,
    Certificate,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'professional_title',
        'email',
        'location',
    )
    search_fields = (
        'full_name',
        'professional_title',
        'email',
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'degree',
        'institution',
        'field_of_study',
        'start_year',
        'end_year',
    )
    search_fields = (
        'degree',
        'institution',
        'field_of_study',
    )
    ordering = ('-end_year',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'company',
        'start_date',
        'end_date',
        'is_current',
    )
    search_fields = (
        'position',
        'company',
        'description',
    )
    list_filter = (
        'is_current',
        'company',
    )
    ordering = ('-start_date',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'proficiency',
    )
    search_fields = (
        'name',
        'category',
    )
    list_filter = (
        'category',
    )
    ordering = ('category', 'name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'technologies',
        'date_completed',
    )
    search_fields = (
        'title',
        'description',
        'technologies',
    )
    ordering = ('-date_completed',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'issuing_organization',
        'issue_date',
        'expiration_date',
    )

    search_fields = (
        'name',
        'issuing_organization',
        'credential_id',
    )

    list_filter = (
        'issuing_organization',
        'issue_date',
    )