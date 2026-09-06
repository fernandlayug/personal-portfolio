from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    # Platform
    path(
        '',
        views.site_home,
        name='site_home'
    ),

    # Owner login
    path(
        'login/',
        views.owner_login,
        name='login'
    ),

    # Owner logout
    path(
        'logout/',
        views.owner_logout,
        name='logout'
    ),

    # Owner dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # Profile management
    path(
        'dashboard/profile/',
        views.profile_edit,
        name='profile_edit'
    ),

    path(
        'signup/',
        views.owner_signup,
        name='signup'
    ),

    # Education Management
    path(
        'dashboard/education/',
        views.education_list,
        name='education_list'
    ),

    path(
        'dashboard/education/add/',
        views.education_add,
        name='education_add'
    ),

    path(
        'dashboard/education/<int:education_id>/edit/',
        views.education_edit,
        name='education_edit'
    ),

    path(
        'dashboard/education/<int:education_id>/delete/',
        views.education_delete,
        name='education_delete'
    ),

    # Work Experience Management
    path(
        'dashboard/experience/',
        views.work_experience_list,
        name='work_experience_list'
    ),

    path(
        'dashboard/experience/add/',
        views.work_experience_add,
        name='work_experience_add'
    ),

    path(
        'dashboard/experience/edit/<int:pk>/',
        views.work_experience_edit,
        name='work_experience_edit'
    ),

    path(
        'dashboard/experience/delete/<int:pk>/',
        views.work_experience_delete,
        name='work_experience_delete'
    ),

    # Skills Management
    path(
        'dashboard/skills/',
        views.skill_list,
        name='skill_list'
    ),

    path(
        'dashboard/skills/add/',
        views.skill_add,
        name='skill_add'
    ),

    path(
        'dashboard/skills/edit/<int:pk>/',
        views.skill_edit,
        name='skill_edit'
    ),

    path(
        'dashboard/skills/delete/<int:pk>/',
        views.skill_delete,
        name='skill_delete'
    ),

    # Project Management
    path(
        'dashboard/projects/',
        views.project_list,
        name='project_list'
    ),

    path(
        'dashboard/projects/add/',
        views.project_add,
        name='project_add'
    ),

    path(
        'dashboard/projects/edit/<int:pk>/',
        views.project_edit,
        name='project_edit'
    ),

    path(
        'dashboard/projects/delete/<int:pk>/',
        views.project_delete,
        name='project_delete'
    ),

    # Certificate Management
    path(
        'dashboard/certificates/',
        views.certificate_list,
        name='certificate_list'
    ),

    path(
        'dashboard/certificates/add/',
        views.certificate_add,
        name='certificate_add'
    ),

    path(
        'dashboard/certificates/<int:certificate_id>/edit/',
        views.certificate_edit,
        name='certificate_edit'
    ),

    path(
        'dashboard/certificates/<int:certificate_id>/delete/',
        views.certificate_delete,
        name='certificate_delete'
    ),

    path(
    'dashboard/research/',
    views.research_list,
    name='research_list'
    ),

    path(
        'dashboard/research/add/',
        views.research_add,
        name='research_add'
    ),

    path(
        'dashboard/research/<int:research_id>/edit/',
        views.research_edit,
        name='research_edit'
    ),

    path(
        'dashboard/research/<int:research_id>/delete/',
        views.research_delete,
        name='research_delete'
    ),

    path(
    'dashboard/licenses/',
    views.license_list,
    name='license_list'
    ),

    path(
        'dashboard/licenses/add/',
        views.license_add,
        name='license_add'
    ),

    path(
        'dashboard/licenses/<int:license_id>/edit/',
        views.license_edit,
        name='license_edit'
    ),

    path(
        'dashboard/licenses/<int:license_id>/delete/',
        views.license_delete,
        name='license_delete'
    ),

]