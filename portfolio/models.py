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
    institution = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Completed')
    abstract = models.TextField(blank=True)
    research_url = models.URLField(blank=True)
    publication_url = models.URLField(blank=True)
    collaborators = models.TextField(
        blank=True,
        help_text="List co-researchers or authors."
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-completion_date', 'title']


class License(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='licenses'
    )
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    license_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Professional License, Academic License, Teaching License"
    )
    license_number = models.CharField(max_length=200, blank=True)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Active')
    license_url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-issue_date', 'name']


class Award(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='awards'
    )
    name = models.CharField(max_length=200)
    awarding_organization = models.CharField(max_length=200)
    award_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Academic, Professional, Research, Leadership"
    )
    award_date = models.DateField()
    level = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Institutional, Local, Regional, National, International"
    )
    description = models.TextField(blank=True)
    award_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-award_date', 'name']


class ProfessionalMembership(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='professional_memberships'
    )
    organization_name = models.CharField(max_length=200)
    membership_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Regular Member, Associate Member, Fellow, Student Member"
    )
    membership_number = models.CharField(max_length=200, blank=True)
    role = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Member, Officer, Board Member, Chapter President"
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Active')
    description = models.TextField(blank=True)
    membership_url = models.URLField(blank=True)

    def __str__(self):
        return self.organization_name

    class Meta:
        ordering = ['-start_date', 'organization_name']


class EngagementType(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='engagement_types'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profile', 'name'],
                name='unique_engagement_type_per_profile'
            )
        ]
        ordering = ['name']

    def __str__(self):
        return self.name


class EngagementRole(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='engagement_roles'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profile', 'name'],
                name='unique_engagement_role_per_profile'
            )
        ]
        ordering = ['name']

    def __str__(self):
        return self.name


class OrganizationClassification(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='organization_classifications'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profile', 'name'],
                name='unique_org_classification_per_profile'
            )
        ]
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='tags'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profile', 'name'],
                name='unique_tag_per_profile'
            )
        ]
        ordering = ['name']

    def __str__(self):
        return self.name


class Organization(models.Model):
    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_UNLISTED = 'unlisted'
    VISIBILITY_CHOICES = [
        (VISIBILITY_PRIVATE, 'Private'),
        (VISIBILITY_PUBLIC, 'Public'),
        (VISIBILITY_UNLISTED, 'Unlisted'),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='organizations'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    classifications = models.ManyToManyField(
        OrganizationClassification,
        related_name='organizations',
        blank=True
    )
    visibility = models.CharField(
        max_length=20,
        choices=VISIBILITY_CHOICES,
        default=VISIBILITY_PRIVATE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['profile', 'visibility'], name='org_profile_visibility_idx'),
        ]

    def __str__(self):
        return self.name


class Event(models.Model):
    EVENT_CONFERENCE = 'conference'
    EVENT_WORKSHOP = 'workshop'
    EVENT_SEMINAR = 'seminar'
    EVENT_SUMMIT = 'summit'
    EVENT_COMPETITION = 'competition'
    EVENT_SYMPOSIUM = 'symposium'
    EVENT_TRAINING = 'training'
    EVENT_FORUM = 'forum'
    EVENT_OTHER = 'other'
    EVENT_TYPE_CHOICES = [
        (EVENT_CONFERENCE, 'Conference'),
        (EVENT_WORKSHOP, 'Workshop'),
        (EVENT_SEMINAR, 'Seminar'),
        (EVENT_SUMMIT, 'Summit'),
        (EVENT_COMPETITION, 'Competition'),
        (EVENT_SYMPOSIUM, 'Symposium'),
        (EVENT_TRAINING, 'Training'),
        (EVENT_FORUM, 'Forum'),
        (EVENT_OTHER, 'Other'),
    ]

    MODE_IN_PERSON = 'in_person'
    MODE_ONLINE = 'online'
    MODE_HYBRID = 'hybrid'
    MODE_OTHER = 'other'
    MODE_CHOICES = [
        (MODE_IN_PERSON, 'In Person'),
        (MODE_ONLINE, 'Online'),
        (MODE_HYBRID, 'Hybrid'),
        (MODE_OTHER, 'Other'),
    ]

    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_UNLISTED = 'unlisted'
    VISIBILITY_CHOICES = [
        (VISIBILITY_PRIVATE, 'Private'),
        (VISIBILITY_PUBLIC, 'Public'),
        (VISIBILITY_UNLISTED, 'Unlisted'),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='events'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_type = models.CharField(
        max_length=30,
        choices=EVENT_TYPE_CHOICES,
        blank=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    mode = models.CharField(
        max_length=20,
        choices=MODE_CHOICES,
        blank=True
    )
    visibility = models.CharField(
        max_length=20,
        choices=VISIBILITY_CHOICES,
        default=VISIBILITY_PRIVATE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', 'name']
        indexes = [
            models.Index(fields=['profile', 'start_date'], name='event_profile_start_idx'),
            models.Index(fields=['profile', 'visibility'], name='event_profile_visibility_idx'),
        ]

    def __str__(self):
        return self.name


class Evidence(models.Model):
    EVIDENCE_CERTIFICATE = 'certificate'
    EVIDENCE_LETTER = 'letter'
    EVIDENCE_ATTENDANCE = 'attendance_record'
    EVIDENCE_EVALUATION = 'evaluation_report'
    EVIDENCE_ANNOUNCEMENT = 'official_announcement'
    EVIDENCE_EMAIL = 'email_correspondence'
    EVIDENCE_MEETING = 'meeting_record'
    EVIDENCE_PHOTO = 'photo'
    EVIDENCE_ARTICLE = 'published_article'
    EVIDENCE_REVIEW = 'review_record'
    EVIDENCE_PARTICIPANT_OUTPUT = 'participant_output'
    EVIDENCE_EXTERNAL_REFERENCE = 'external_reference'
    EVIDENCE_OTHER = 'other'
    EVIDENCE_TYPE_CHOICES = [
        (EVIDENCE_CERTIFICATE, 'Certificate'),
        (EVIDENCE_LETTER, 'Letter'),
        (EVIDENCE_ATTENDANCE, 'Attendance Record'),
        (EVIDENCE_EVALUATION, 'Evaluation Report'),
        (EVIDENCE_ANNOUNCEMENT, 'Official Announcement'),
        (EVIDENCE_EMAIL, 'Email Correspondence'),
        (EVIDENCE_MEETING, 'Meeting Record'),
        (EVIDENCE_PHOTO, 'Photo'),
        (EVIDENCE_ARTICLE, 'Published Article'),
        (EVIDENCE_REVIEW, 'Review Record'),
        (EVIDENCE_PARTICIPANT_OUTPUT, 'Participant Output'),
        (EVIDENCE_EXTERNAL_REFERENCE, 'External Reference'),
        (EVIDENCE_OTHER, 'Other'),
    ]

    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_UNLISTED = 'unlisted'
    VISIBILITY_CHOICES = [
        (VISIBILITY_PRIVATE, 'Private'),
        (VISIBILITY_PUBLIC, 'Public'),
        (VISIBILITY_UNLISTED, 'Unlisted'),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='evidence'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    evidence_type = models.CharField(
        max_length=40,
        choices=EVIDENCE_TYPE_CHOICES
    )
    external_url = models.URLField(blank=True)
    visibility = models.CharField(
        max_length=20,
        choices=VISIBILITY_CHOICES,
        default=VISIBILITY_PRIVATE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['profile', 'visibility'], name='evidence_visibility_idx'),
        ]

    def __str__(self):
        return self.title


class Engagement(models.Model):
    STATUS_DRAFT = 'draft'
    STATUS_PLANNED = 'planned'
    STATUS_ONGOING = 'ongoing'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_POSTPONED = 'postponed'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PLANNED, 'Planned'),
        (STATUS_ONGOING, 'Ongoing'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_POSTPONED, 'Postponed'),
    ]

    MODE_IN_PERSON = 'in_person'
    MODE_ONLINE = 'online'
    MODE_HYBRID = 'hybrid'
    MODE_OTHER = 'other'
    MODE_CHOICES = [
        (MODE_IN_PERSON, 'In Person'),
        (MODE_ONLINE, 'Online'),
        (MODE_HYBRID, 'Hybrid'),
        (MODE_OTHER, 'Other'),
    ]

    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_UNLISTED = 'unlisted'
    VISIBILITY_CHOICES = [
        (VISIBILITY_PRIVATE, 'Private'),
        (VISIBILITY_PUBLIC, 'Public'),
        (VISIBILITY_UNLISTED, 'Unlisted'),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='engagements'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    engagement_type = models.ForeignKey(
        EngagementType,
        on_delete=models.PROTECT,
        related_name='engagements'
    )
    roles = models.ManyToManyField(
        EngagementRole,
        related_name='engagements',
        blank=True
    )
    primary_role = models.ForeignKey(
        EngagementRole,
        on_delete=models.PROTECT,
        related_name='primary_engagements'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    purpose = models.TextField(blank=True)
    outcome = models.TextField(blank=True)
    impact = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    mode = models.CharField(
        max_length=20,
        choices=MODE_CHOICES,
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='engagements',
        blank=True
    )
    featured = models.BooleanField(default=False)
    visibility = models.CharField(
        max_length=20,
        choices=VISIBILITY_CHOICES,
        default=VISIBILITY_PRIVATE
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name='engagements',
        blank=True,
        null=True
    )
    projects = models.ManyToManyField(
        Project,
        related_name='engagements',
        blank=True
    )
    research = models.ManyToManyField(
        Research,
        related_name='engagements',
        blank=True
    )
    professional_memberships = models.ManyToManyField(
        ProfessionalMembership,
        related_name='engagements',
        blank=True
    )
    work_experiences = models.ManyToManyField(
        WorkExperience,
        related_name='engagements',
        blank=True
    )
    skills = models.ManyToManyField(
        Skill,
        related_name='engagements',
        blank=True
    )
    education = models.ManyToManyField(
        Education,
        related_name='engagements',
        blank=True
    )
    certificates = models.ManyToManyField(
        Certificate,
        related_name='engagements',
        blank=True
    )
    awards = models.ManyToManyField(
        Award,
        related_name='engagements',
        blank=True
    )
    evidence = models.ManyToManyField(
        Evidence,
        related_name='engagements',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', '-created_at', 'title']
        indexes = [
            models.Index(fields=['profile', 'status'], name='eng_profile_status_idx'),
            models.Index(fields=['profile', 'visibility'], name='eng_profile_visibility_idx'),
            models.Index(fields=['profile', 'start_date'], name='eng_profile_start_idx'),
            models.Index(fields=['profile', 'featured'], name='eng_profile_featured_idx'),
            models.Index(fields=['profile', 'engagement_type'], name='eng_profile_type_idx'),
        ]

    def __str__(self):
        return self.title


class EngagementOrganization(models.Model):
    ROLE_PARTNER = 'partner'
    ROLE_HOST = 'host'
    ROLE_ORGANIZER = 'organizer'
    ROLE_APPOINTING = 'appointing_organization'
    ROLE_COLLABORATING = 'collaborating_organization'
    ROLE_SPONSOR = 'sponsor'
    ROLE_CLIENT = 'client'
    ROLE_BENEFICIARY = 'beneficiary_organization'
    ROLE_SUPPORTING = 'supporting_organization'
    ROLE_OTHER = 'other'
    RELATIONSHIP_ROLE_CHOICES = [
        (ROLE_PARTNER, 'Partner'),
        (ROLE_HOST, 'Host'),
        (ROLE_ORGANIZER, 'Organizer'),
        (ROLE_APPOINTING, 'Appointing Organization'),
        (ROLE_COLLABORATING, 'Collaborating Organization'),
        (ROLE_SPONSOR, 'Sponsor'),
        (ROLE_CLIENT, 'Client'),
        (ROLE_BENEFICIARY, 'Beneficiary Organization'),
        (ROLE_SUPPORTING, 'Supporting Organization'),
        (ROLE_OTHER, 'Other'),
    ]

    engagement = models.ForeignKey(
        Engagement,
        on_delete=models.CASCADE,
        related_name='organization_relationships'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name='engagement_relationships'
    )
    relationship_role = models.CharField(
        max_length=40,
        choices=RELATIONSHIP_ROLE_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['engagement', 'organization', 'relationship_role'],
                name='unique_engagement_org_role'
            )
        ]
        ordering = ['organization__name']

    def __str__(self):
        return f"{self.organization} - {self.get_relationship_role_display()}"
