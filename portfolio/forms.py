from allauth.account.forms import SignupForm
from django import forms
from django.utils import timezone

from .models import Profile, Education, WorkExperience, Skill, Project, Certificate, Research

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'full_name',
            'professional_title',
            'bio',
            'email',
            'phone',
            'location',
            'profile_image',
            'linkedin_url',
            'github_url',
            'resume',
        ]

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Your full name'
                }
            ),

            'professional_title': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Full-Stack Developer'
                }
            ),

            'bio': forms.Textarea(
                attrs={
                    'rows': 6,
                    'placeholder': 'Tell visitors about yourself'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'you@example.com'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Your phone number'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Your location'
                }
            ),

            'linkedin_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://linkedin.com/in/yourname'
                }
            ),

            'github_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://github.com/yourname'
                }
            ),
        }

class CustomSignupForm(SignupForm):

    full_name = forms.CharField(
        max_length=150,
        label='Full Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your full name'
            }
        )
    )

    def save(self, request):

        user = super().save(request)

        profile = user.profile

        profile.full_name = self.cleaned_data[
            'full_name'
        ]

        profile.email = user.email

        profile.save()

        return user



class EducationForm(forms.ModelForm):

    class Meta:
        model = Education

        fields = [
            'institution',
            'degree',
            'field_of_study',
            'start_year',
            'end_year',
            'description',
        ]

        widgets = {
            'institution': forms.TextInput(attrs={
                'placeholder': 'e.g. Santa Rita College of Pampanga',
            }),

            'degree': forms.TextInput(attrs={
                'placeholder': 'e.g. Bachelor of Science in Information Technology',
            }),

            'field_of_study': forms.TextInput(attrs={
                'placeholder': 'e.g. Information Technology',
            }),

            'start_year': forms.NumberInput(attrs={
                'placeholder': 'e.g. 2020',
                'min': '1900',
                'max': '2100',
            }),

            'end_year': forms.NumberInput(attrs={
                'placeholder': 'e.g. 2024',
                'min': '1900',
                'max': '2100',
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your education, achievements, or relevant activities...',
                'rows': 5,
            }),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
            model = WorkExperience
            fields = [
                'company',
                'position',
                'start_date',
                'end_date',
                'is_current',
                'description',
            ]

            widgets = {
                'company': forms.TextInput(attrs={
                    'placeholder': 'e.g. Santa Rita College of Pampanga',
                }),

                'position': forms.TextInput(attrs={
                    'placeholder': 'e.g. IT Instructor',
                }),

                'start_date': forms.DateInput(attrs={
                    'type': 'date',
                }),

                'end_date': forms.DateInput(attrs={
                    'type': 'date',
                }),

                'is_current': forms.CheckboxInput(),

                'description': forms.Textarea(attrs={
                    'placeholder': (
                        'Describe your responsibilities, '
                        'achievements, and relevant experience...'
                    ),
                    'rows': 6,
                }),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = [
            'name',
            'category',
            'proficiency',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Python',
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'e.g. Programming Languages',
            }),
            'proficiency': forms.NumberInput(attrs={
                'min': 0,
                'max': 100,
                'placeholder': 'e.g. 85',
            }),
        }

    def clean_proficiency(self):
        proficiency = self.cleaned_data['proficiency']

        if proficiency < 0 or proficiency > 100:
            raise forms.ValidationError(
                'Proficiency must be between 0 and 100.'
            )

        return proficiency

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'technologies',
            'project_url',
            'github_url',
            'date_completed',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Personal Portfolio Assistant',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': (
                    'Describe the project, its purpose, '
                    'features, and your contribution...'
                ),
                'rows': 7,
            }),
            'technologies': forms.TextInput(attrs={
                'placeholder': 'e.g. Django, Python, MySQL',
            }),
            'project_url': forms.URLInput(attrs={
                'placeholder': 'https://example.com',
            }),
            'github_url': forms.URLInput(attrs={
                'placeholder': 'https://github.com/username/project',
            }),
            'date_completed': forms.DateInput(attrs={
                'type': 'date',
            }),
        }

    def clean_date_completed(self):
        date_completed = self.cleaned_data.get('date_completed')

        if date_completed:
            from django.utils import timezone

            if date_completed > timezone.localdate():
                raise forms.ValidationError(
                    'Completion date cannot be in the future.'
                )

        return date_completed

    def clean_project_url(self):
        url = self.cleaned_data.get('project_url')

        if url and not (
            url.startswith('http://')
            or url.startswith('https://')
        ):
            raise forms.ValidationError(
                'Project URL must start with http:// or https://.'
            )

        return url

    def clean_github_url(self):
        url = self.cleaned_data.get('github_url')

        if url and not (
            url.startswith('http://')
            or url.startswith('https://')
        ):
            raise forms.ValidationError(
                'GitHub URL must start with http:// or https://.'
            )

        return url

class CertificateForm(forms.ModelForm):

    class Meta:

        model = Certificate

        fields = [
            'name',
            'issuing_organization',
            'issue_date',
            'expiration_date',
            'credential_id',
            'credential_url',
            'description',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. AWS Certified Cloud Practitioner'
                }
            ),

            'issuing_organization': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Amazon Web Services'
                }
            ),

            'issue_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'expiration_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'credential_id': forms.TextInput(
                attrs={
                    'placeholder': 'Optional'
                }
            ),

            'credential_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://...'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Optional description'
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        issue_date = cleaned_data.get(
            'issue_date'
        )

        expiration_date = cleaned_data.get(
            'expiration_date'
        )

        today = timezone.localdate()

        if issue_date and issue_date > today:

            raise forms.ValidationError(
                'Issue date cannot be in the future.'
            )

        if (
            issue_date
            and expiration_date
            and expiration_date < issue_date
        ):

            raise forms.ValidationError(
                'Expiration date cannot be earlier than the issue date.'
            )

        return cleaned_data

class ResearchForm(forms.ModelForm):

    class Meta:
        model = Research

        fields = [
            'title',
            'research_type',
            'role',
            'institution',
            'start_date',
            'completion_date',
            'status',
            'abstract',
            'research_url',
            'publication_url',
            'collaborators',
        ]

        widgets = {
            'start_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'completion_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'abstract': forms.Textarea(
                attrs={
                    'rows': 5
                }
            ),

            'collaborators': forms.Textarea(
                attrs={
                    'rows': 3
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        start_date = cleaned_data.get(
            'start_date'
        )

        completion_date = cleaned_data.get(
            'completion_date'
        )

        today = timezone.localdate()

        if start_date and start_date > today:

            self.add_error(
                'start_date',
                'Start date cannot be in the future.'
            )

        if completion_date and completion_date > today:

            self.add_error(
                'completion_date',
                'Completion date cannot be in the future.'
            )

        if (
            start_date
            and completion_date
            and completion_date < start_date
        ):

            self.add_error(
                'completion_date',
                'Completion date cannot be earlier than the start date.'
            )

        return cleaned_data