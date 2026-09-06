from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
       
    )

    portfolio_slug = models.SlugField(
        max_length=80,
        unique=True
    )

    full_name = models.CharField(max_length=150)
    professional_title = models.CharField(max_length=150)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=150, blank=True)

    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    linkedin_url = models.URLField(
        blank=True,
        help_text="Your LinkedIn profile URL."
    )

    github_url = models.URLField(
        blank=True,
        help_text="Your GitHub profile URL."
    )

    resume = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True,
        help_text="Upload your PDF resume."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Education(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='education'
    )

    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class WorkExperience(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='work_experience'
    )

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True
    )
    is_current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} - {self.company}"


class Skill(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='skills'
    )

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=100,
        blank=True
    )
    proficiency = models.PositiveIntegerField(
        default=50,
        help_text="Enter proficiency from 0 to 100."
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        blank=True
    )

    description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        help_text="Example: Django, Python, MySQL"
    )

    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    date_completed = models.DateField(
        blank=True,
        null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profile', 'slug'],
                name='unique_project_slug_per_profile'
            )
        ]

    def __str__(self):
        return self.title

class Certificate(models.Model):

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='certificates',
  
    )

    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(
        blank=True,
        null=True
    )
    credential_id = models.CharField(
        max_length=200,
        blank=True
    )
    credential_url = models.URLField(
        blank=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-issue_date']


class Research(models.Model):

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='research'
    )

    title = models.CharField(max_length=250)

    research_type = models.CharField(
        max_length=100,
        help_text="Example: Thesis, Journal Article, Conference Paper"
    )

    role = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Researcher, Author, Adviser"
    )

    institution = models.CharField(
        max_length=200,
        blank=True
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    completion_date = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=50,
        default='Completed'
    )

    abstract = models.TextField(
        blank=True
    )

    research_url = models.URLField(
        blank=True
    )

    publication_url = models.URLField(
        blank=True
    )

    collaborators = models.TextField(
        blank=True,
        help_text="List co-researchers or authors."
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            '-completion_date',
            'title'
        ]