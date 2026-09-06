from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

from .models import (
    Profile,
    Education,
    WorkExperience,
    Skill,
    Project,
    Certificate,
    Research,
    License,
    
)

from .forms import (
    ProfileForm,
    EducationForm,
    WorkExperienceForm,
    SkillForm,
    ProjectForm,
    CertificateForm,
    ResearchForm,
    LicenseForm,
)

def portfolio_home(request):
    host = request.get_host().split(':')[0].lower()
    base_domain = settings.PORTFOLIO_BASE_DOMAIN.lower()

    suffix = f".{base_domain}"

    if not host.endswith(suffix):
        raise Http404("Portfolio not found.")

    portfolio_slug = host[:-len(suffix)]

    if not portfolio_slug:
        raise Http404("Portfolio not found.")

    try:
        profile = Profile.objects.get(
            portfolio_slug=portfolio_slug
        )
    except Profile.DoesNotExist:
        raise Http404("Portfolio not found.")

    context = {
        'profile': profile,
        'education': profile.education.all(),
        'experience': profile.work_experience.all(),
        'skills': profile.skills.all(),
        'projects': profile.projects.all(),
        'platform_login_url': get_platform_url(
            request,
            '/login/'
        ),
    }
    return render(
        request,
        'portfolio/home.html',
        context
    )
def verify_current_tenant(request):
    host = request.get_host().split(':')[0].lower()
    base_domain = settings.PORTFOLIO_BASE_DOMAIN.lower()

    suffix = f".{base_domain}"

    if not host.endswith(suffix):
        raise Http404("Portfolio not found.")

    portfolio_slug = host[:-len(suffix)]

    try:
        profile = Profile.objects.select_related(
            'user'
        ).get(
            portfolio_slug=portfolio_slug
        )

    except Profile.DoesNotExist:
        raise Http404("Portfolio not found.")

    if not request.user.is_authenticated:
        return profile

    if profile.user != request.user:
        raise Http404("Portfolio not found.")

    return profile

@login_required
def dashboard(request):
    profile = verify_current_tenant(request)

    portfolio_host = (
        f"{profile.portfolio_slug}."
        f"{settings.PORTFOLIO_BASE_DOMAIN}"
    )

    portfolio_url = (
        f"{request.scheme}://{portfolio_host}"
    )

    if settings.DEBUG:
        portfolio_url += f":{request.get_port()}"

    context = {
        'profile': profile,
        'education': profile.education.all(),
        'experience': profile.work_experience.all(),
        'skills': profile.skills.all(),
        'projects': profile.projects.all(),
        'portfolio_url': portfolio_url,
    }

    return render(
        request,
        'portfolio/dashboard.html',
        context
    )

@login_required
def profile_edit(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return redirect('profile_edit')

    else:

        form = ProfileForm(
            instance=profile
        )

    context = {
        'profile': profile,
        'form': form,
    }

    return render(
        request,
        'portfolio/profile_edit.html',
        context
    )

# =========================================================
# EDUCATION MANAGEMENT
# =========================================================

@login_required
def education_list(request):

    profile = verify_current_tenant(request)

    education = profile.education.all().order_by(
        '-start_year'
    )

    portfolio_host = (
        f"{profile.portfolio_slug}."
        f"{settings.PORTFOLIO_BASE_DOMAIN}"
    )

    portfolio_url = (
        f"{request.scheme}://{portfolio_host}"
    )

    if settings.DEBUG:
        portfolio_url += f":{request.get_port()}"

    context = {
        'profile': profile,
        'education': education,
        'portfolio_url': portfolio_url,
    }

    return render(
        request,
        'portfolio/education_list.html',
        context
    )


@login_required
def education_add(request):

    profile = verify_current_tenant(request)

    if request.method == 'POST':

        form = EducationForm(
            request.POST
        )

        if form.is_valid():

            education = form.save(
                commit=False
            )

            # IMPORTANT:
            # Never accept the profile from the browser.
            # Always assign it from the authenticated
            # tenant/profile.

            education.profile = profile

            education.save()

            messages.success(
                request,
                'Education added successfully.'
            )

            return redirect(
                'education_list'
            )

    else:

        form = EducationForm()

    context = {
        'profile': profile,
        'form': form,
        'page_title': 'Add Education',
    }

    return render(
        request,
        'portfolio/education_form.html',
        context
    )


@login_required
def education_edit(
    request,
    education_id
):

    profile = verify_current_tenant(request)

    try:

        education = profile.education.get(
            id=education_id
        )

    except Education.DoesNotExist:

        raise Http404(
            "Education record not found."
        )

    if request.method == 'POST':

        form = EducationForm(
            request.POST,
            instance=education
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Education updated successfully.'
            )

            return redirect(
                'education_list'
            )

    else:

        form = EducationForm(
            instance=education
        )

    context = {
        'profile': profile,
        'form': form,
        'education': education,
        'page_title': 'Edit Education',
    }

    return render(
        request,
        'portfolio/education_form.html',
        context
    )


@login_required
def education_delete(
    request,
    education_id
):

    profile = verify_current_tenant(request)

    try:

        education = profile.education.get(
            id=education_id
        )

    except Education.DoesNotExist:

        raise Http404(
            "Education record not found."
        )

    if request.method == 'POST':

        education.delete()

        messages.success(
            request,
            'Education deleted successfully.'
        )

        return redirect(
            'education_list'
        )

    context = {
        'profile': profile,
        'education': education,
    }

    return render(
        request,
        'portfolio/education_confirm_delete.html',
        context
    )
@login_required
def work_experience_list(request):

    profile = request.user.profile

    experience = profile.work_experience.all().order_by(
        '-is_current',
        '-start_date'
    )

    context = {
        'profile': profile,
        'experience': experience,
    }

    return render(
        request,
        'portfolio/work_experience_list.html',
        context
    )


@login_required
def work_experience_add(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = WorkExperienceForm(
            request.POST
        )

        if form.is_valid():

            experience = form.save(
                commit=False
            )

            experience.profile = profile

            experience.save()

            return redirect(
                'work_experience_list'
            )

    else:

        form = WorkExperienceForm()

    context = {
        'profile': profile,
        'form': form,
        'page_title': 'Add Work Experience',
        'submit_label': 'Add Experience',
    }

    return render(
        request,
        'portfolio/work_experience_form.html',
        context
    )


@login_required
def work_experience_edit(request, pk):

    profile = request.user.profile

    experience = profile.work_experience.get(
        pk=pk
    )

    if request.method == 'POST':

        form = WorkExperienceForm(
            request.POST,
            instance=experience
        )

        if form.is_valid():

            form.save()

            return redirect(
                'work_experience_list'
            )

    else:

        form = WorkExperienceForm(
            instance=experience
        )

    context = {
        'profile': profile,
        'form': form,
        'experience': experience,
        'page_title': 'Edit Work Experience',
        'submit_label': 'Save Changes',
    }

    return render(
        request,
        'portfolio/work_experience_form.html',
        context
    )


@login_required
def work_experience_delete(request, pk):

    profile = request.user.profile

    experience = profile.work_experience.get(
        pk=pk
    )

    if request.method == 'POST':

        experience.delete()

        return redirect(
            'work_experience_list'
        )

    context = {
        'profile': profile,
        'experience': experience,
    }

    return render(
        request,
        'portfolio/work_experience_confirm_delete.html',
        context
    )

@login_required
def skill_list(request):
    profile = request.user.profile

    skills = profile.skills.all().order_by(
        'category',
        'name'
    )

    context = {
        'profile': profile,
        'skills': skills,
    }

    return render(
        request,
        'portfolio/skill_list.html',
        context
    )


@login_required
def skill_add(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = profile
            skill.save()

            return redirect('skill_list')

    else:
        form = SkillForm()

    context = {
        'profile': profile,
        'form': form,
        'page_title': 'Add Skill',
        'submit_label': 'Add Skill',
    }

    return render(
        request,
        'portfolio/skill_form.html',
        context
    )


@login_required
def skill_edit(request, pk):
    profile = request.user.profile

    skill = profile.skills.get(pk=pk)

    if request.method == 'POST':
        form = SkillForm(
            request.POST,
            instance=skill
        )

        if form.is_valid():
            form.save()

            return redirect('skill_list')

    else:
        form = SkillForm(instance=skill)

    context = {
        'profile': profile,
        'form': form,
        'skill': skill,
        'page_title': 'Edit Skill',
        'submit_label': 'Save Changes',
    }

    return render(
        request,
        'portfolio/skill_form.html',
        context
    )


@login_required
def skill_delete(request, pk):
    profile = request.user.profile

    skill = profile.skills.get(pk=pk)

    if request.method == 'POST':
        skill.delete()

        return redirect('skill_list')

    context = {
        'profile': profile,
        'skill': skill,
    }

    return render(
        request,
        'portfolio/skill_confirm_delete.html',
        context
    )

@login_required
def project_list(request):
    profile = request.user.profile

    projects = profile.projects.all().order_by(
        '-date_completed',
        'title'
    )

    context = {
        'profile': profile,
        'projects': projects,
    }

    return render(
        request,
        'portfolio/project_list.html',
        context
    )


@login_required
def project_add(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.profile = profile

            # Generate a URL-friendly slug from the project title.
            base_slug = slugify(project.title)
            slug = base_slug
            counter = 2

            while profile.projects.filter(
                slug=slug
            ).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            project.slug = slug
            project.save()

            return redirect('project_list')

    else:
        form = ProjectForm()

    context = {
        'profile': profile,
        'form': form,
        'page_title': 'Add Project',
        'submit_label': 'Add Project',
    }

    return render(
        request,
        'portfolio/project_form.html',
        context
    )


@login_required
def project_edit(request, pk):
    profile = request.user.profile

    project = profile.projects.get(pk=pk)

    if request.method == 'POST':
        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            project = form.save(commit=False)

            # Keep the existing slug when editing.
            project.save()

            return redirect('project_list')

    else:
        form = ProjectForm(instance=project)

    context = {
        'profile': profile,
        'form': form,
        'project': project,
        'page_title': 'Edit Project',
        'submit_label': 'Save Changes',
    }

    return render(
        request,
        'portfolio/project_form.html',
        context
    )


@login_required
def project_delete(request, pk):
    profile = request.user.profile

    project = profile.projects.get(pk=pk)

    if request.method == 'POST':
        project.delete()

        return redirect('project_list')

    context = {
        'profile': profile,
        'project': project,
    }

    return render(
        request,
        'portfolio/project_confirm_delete.html',
        context
    )

@login_required
def certificate_list(request):

    profile = verify_current_tenant(request)

    certificates = profile.certificates.all().order_by(
        '-issue_date'
    )

    portfolio_host = (
        f"{profile.portfolio_slug}."
        f"{settings.PORTFOLIO_BASE_DOMAIN}"
    )

    portfolio_url = (
        f"{request.scheme}://{portfolio_host}"
    )

    if settings.DEBUG:
        portfolio_url += f":{request.get_port()}"

    context = {
        'profile': profile,
        'certificates': certificates,
        'portfolio_url': portfolio_url,
    }

    return render(
        request,
        'portfolio/certificate_list.html',
        context
    )


@login_required
def certificate_add(request):

    profile = verify_current_tenant(request)

    if request.method == 'POST':

        form = CertificateForm(
            request.POST
        )

        if form.is_valid():

            certificate = form.save(
                commit=False
            )

            # IMPORTANT:
            # Never accept the profile from the browser.
            # Always assign it from the authenticated
            # tenant/profile.

            certificate.profile = profile

            certificate.save()

            messages.success(
                request,
                'Certificate added successfully.'
            )

            return redirect(
                'certificate_list'
            )

    else:

        form = CertificateForm()

    context = {
        'profile': profile,
        'form': form,
        'page_title': 'Add Certificate',
    }

    return render(
        request,
        'portfolio/certificate_form.html',
        context
    )


@login_required
def certificate_edit(
    request,
    certificate_id
):

    profile = verify_current_tenant(request)

    try:

        certificate = profile.certificates.get(
            id=certificate_id
        )

    except Certificate.DoesNotExist:

        raise Http404(
            "Certificate record not found."
        )

    if request.method == 'POST':

        form = CertificateForm(
            request.POST,
            instance=certificate
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Certificate updated successfully.'
            )

            return redirect(
                'certificate_list'
            )

    else:

        form = CertificateForm(
            instance=certificate
        )

    context = {
        'profile': profile,
        'form': form,
        'certificate': certificate,
        'page_title': 'Edit Certificate',
    }

    return render(
        request,
        'portfolio/certificate_form.html',
        context
    )


@login_required
def certificate_delete(
    request,
    certificate_id
):

    profile = verify_current_tenant(request)

    try:

        certificate = profile.certificates.get(
            id=certificate_id
        )

    except Certificate.DoesNotExist:

        raise Http404(
            "Certificate record not found."
        )

    if request.method == 'POST':

        certificate.delete()

        messages.success(
            request,
            'Certificate deleted successfully.'
        )

        return redirect(
            'certificate_list'
        )

    context = {
        'profile': profile,
        'certificate': certificate,
    }

    return render(
        request,
        'portfolio/certificate_confirm_delete.html',
        context
    )

@login_required
def research_list(request):
    profile = verify_current_tenant(request)

    research = profile.research.all()

    return render(
        request,
        'portfolio/research_list.html',
        {
            'profile': profile,
            'research': research,
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )


@login_required
def research_add(request):
    profile = verify_current_tenant(request)

    if request.method == 'POST':
        form = ResearchForm(request.POST)

        if form.is_valid():
            research = form.save(commit=False)
            research.profile = profile
            research.save()

            messages.success(
                request,
                'Research record added successfully.'
            )

            return redirect('research_list')

    else:
        form = ResearchForm()

    return render(
        request,
        'portfolio/research_form.html',
        {
            'profile': profile,
            'form': form,
            'page_title': 'Add Research',
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )


@login_required
def research_edit(request, research_id):
    profile = verify_current_tenant(request)

    research = profile.research.get(id=research_id)

    if request.method == 'POST':
        form = ResearchForm(
            request.POST,
            instance=research
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Research record updated successfully.'
            )

            return redirect('research_list')

    else:
        form = ResearchForm(instance=research)

    return render(
        request,
        'portfolio/research_form.html',
        {
            'profile': profile,
            'form': form,
            'research': research,
            'page_title': 'Edit Research',
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )


@login_required
def research_delete(request, research_id):
    profile = verify_current_tenant(request)

    research = profile.research.get(id=research_id)

    if request.method == 'POST':
        research.delete()

        messages.success(
            request,
            'Research record deleted successfully.'
        )

        return redirect('research_list')

    return render(
        request,
        'portfolio/research_confirm_delete.html',
        {
            'profile': profile,
            'research': research,
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )


def redirect_owner_to_portfolio(request):

    profile = request.user.profile

    portfolio_host = (
        f"{profile.portfolio_slug}."
        f"{settings.PORTFOLIO_BASE_DOMAIN}"
    )

    portfolio_url = (
        f"{request.scheme}://{portfolio_host}"
    )

    if settings.DEBUG:
        portfolio_url += f":{request.get_port()}"

    return redirect(portfolio_url)

def owner_login(request):

    host = request.get_host().split(':')[0].lower()
    base_domain = settings.PORTFOLIO_BASE_DOMAIN.lower()

    # Only the platform may process authentication.
    is_platform = host in [
        '127.0.0.1',
        'localhost',
        base_domain,
    ]

    if not is_platform:
        return redirect(
            get_platform_url(
                request,
                '/login/'
            )
        )

    if request.user.is_authenticated:
        return redirect_owner_to_portfolio(request)

    if request.method == 'POST':

        username = request.POST.get(
            'username',
            ''
        ).strip()

        password = request.POST.get(
            'password',
            ''
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            try:
                profile = user.profile

            except Profile.DoesNotExist:

                messages.error(
                    request,
                    'Your account does not have a portfolio.'
                )

            else:

                login(request, user)

                return redirect_owner_to_portfolio(
                    request
                )

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(
        request,
        'portfolio/login.html'
    )

def platform_home(request):
    return render(
        request,
        'portfolio/platform_home.html'
    )

def site_home(request):
    host = request.get_host().split(':')[0].lower()
    base_domain = settings.PORTFOLIO_BASE_DOMAIN.lower()

    suffix = f".{base_domain}"

    # Local development / platform domain
    if host in ['127.0.0.1', 'localhost', base_domain]:
        return platform_home(request)

    # Tenant subdomain
    if host.endswith(suffix):
        return portfolio_home(request)

    raise Http404("Site not found.")

def owner_logout(request):
    logout(request)

    platform_url = (
        f"{request.scheme}://"
        f"{settings.PORTFOLIO_BASE_DOMAIN}"
    )

    if settings.DEBUG:
        platform_url += f":{request.get_port()}"

    return redirect(platform_url)

def get_platform_url(request, path='/'):
    platform_url = (
        f"{request.scheme}://"
        f"{settings.PORTFOLIO_BASE_DOMAIN}"
    )

    if settings.DEBUG:
        platform_url += f":{request.get_port()}"

    return f"{platform_url}{path}"

def owner_signup(request):

    host = request.get_host().split(':')[0].lower()
    base_domain = settings.PORTFOLIO_BASE_DOMAIN.lower()

    is_platform = host in [
        '127.0.0.1',
        'localhost',
        base_domain,
    ]

    if not is_platform:
        return redirect(
            get_platform_url(
                request,
                '/signup/'
            )
        )

    return redirect('/accounts/signup/')

@login_required
def license_list(request):
    profile = verify_current_tenant(request)

    licenses = profile.licenses.all()

    return render(
        request,
        'portfolio/license_list.html',
        {
            'profile': profile,
            'licenses': licenses,
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )

@login_required
def license_add(request):
    profile = verify_current_tenant(request)

    if request.method == 'POST':
        form = LicenseForm(request.POST)

        if form.is_valid():
            license_record = form.save(commit=False)

            license_record.profile = profile

            license_record.save()

            messages.success(
                request,
                'License record added successfully.'
            )

            return redirect('license_list')

    else:
        form = LicenseForm()

    return render(
        request,
        'portfolio/license_form.html',
        {
            'profile': profile,
            'form': form,
            'page_title': 'Add License',
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )

@login_required
def license_edit(request, license_id):
    profile = verify_current_tenant(request)

    license_record = profile.licenses.get(
        id=license_id
    )

    if request.method == 'POST':
        form = LicenseForm(
            request.POST,
            instance=license_record
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'License record updated successfully.'
            )

            return redirect('license_list')

    else:
        form = LicenseForm(
            instance=license_record
        )

    return render(
        request,
        'portfolio/license_form.html',
        {
            'profile': profile,
            'form': form,
            'license': license_record,
            'page_title': 'Edit License',
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )

@login_required
def license_delete(request, license_id):
    profile = verify_current_tenant(request)

    license_record = profile.licenses.get(
        id=license_id
    )

    if request.method == 'POST':
        license_record.delete()

        messages.success(
            request,
            'License record deleted successfully.'
        )

        return redirect('license_list')

    return render(
        request,
        'portfolio/license_confirm_delete.html',
        {
            'profile': profile,
            'license': license_record,
            'portfolio_url': request.build_absolute_uri(
                f'/portfolio/{profile.portfolio_slug}/'
            ),
        }
    )