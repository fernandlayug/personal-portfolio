from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_professionalmembership'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngagementRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engagement_roles', to='portfolio.profile')),
            ],
            options={
                'ordering': ['name'],
                'constraints': [
                    models.UniqueConstraint(fields=('profile', 'name'), name='unique_engagement_role_per_profile'),
                ],
            },
        ),
        migrations.CreateModel(
            name='EngagementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engagement_types', to='portfolio.profile')),
            ],
            options={
                'ordering': ['name'],
                'constraints': [
                    models.UniqueConstraint(fields=('profile', 'name'), name='unique_engagement_type_per_profile'),
                ],
            },
        ),
        migrations.CreateModel(
            name='OrganizationClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_classifications', to='portfolio.profile')),
            ],
            options={
                'ordering': ['name'],
                'constraints': [
                    models.UniqueConstraint(fields=('profile', 'name'), name='unique_org_classification_per_profile'),
                ],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='portfolio.profile')),
            ],
            options={
                'ordering': ['name'],
                'constraints': [
                    models.UniqueConstraint(fields=('profile', 'name'), name='unique_tag_per_profile'),
                ],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('unlisted', 'Unlisted')], default='private', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='portfolio.profile')),
            ],
            options={
                'ordering': ['name'],
                'indexes': [
                    models.Index(fields=['profile', 'visibility'], name='org_profile_visibility_idx'),
                ],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('event_type', models.CharField(blank=True, choices=[('conference', 'Conference'), ('workshop', 'Workshop'), ('seminar', 'Seminar'), ('summit', 'Summit'), ('competition', 'Competition'), ('symposium', 'Symposium'), ('training', 'Training'), ('forum', 'Forum'), ('other', 'Other')], max_length=30)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('mode', models.CharField(blank=True, choices=[('in_person', 'In Person'), ('online', 'Online'), ('hybrid', 'Hybrid'), ('other', 'Other')], max_length=20)),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('unlisted', 'Unlisted')], default='private', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='portfolio.profile')),
            ],
            options={
                'ordering': ['-start_date', 'name'],
                'indexes': [
                    models.Index(fields=['profile', 'start_date'], name='event_profile_start_idx'),
                    models.Index(fields=['profile', 'visibility'], name='event_profile_visibility_idx'),
                ],
            },
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('evidence_type', models.CharField(choices=[('certificate', 'Certificate'), ('letter', 'Letter'), ('attendance_record', 'Attendance Record'), ('evaluation_report', 'Evaluation Report'), ('official_announcement', 'Official Announcement'), ('email_correspondence', 'Email Correspondence'), ('meeting_record', 'Meeting Record'), ('photo', 'Photo'), ('published_article', 'Published Article'), ('review_record', 'Review Record'), ('participant_output', 'Participant Output'), ('external_reference', 'External Reference'), ('other', 'Other')], max_length=40)),
                ('external_url', models.URLField(blank=True)),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('unlisted', 'Unlisted')], default='private', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidence', to='portfolio.profile')),
            ],
            options={
                'ordering': ['title'],
                'indexes': [
                    models.Index(fields=['profile', 'visibility'], name='evidence_profile_visibility_idx'),
                ],
            },
        ),
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('planned', 'Planned'), ('ongoing', 'Ongoing'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('postponed', 'Postponed')], default='draft', max_length=20)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('purpose', models.TextField(blank=True)),
                ('outcome', models.TextField(blank=True)),
                ('impact', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('mode', models.CharField(blank=True, choices=[('in_person', 'In Person'), ('online', 'Online'), ('hybrid', 'Hybrid'), ('other', 'Other')], max_length=20)),
                ('featured', models.BooleanField(default=False)),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('unlisted', 'Unlisted')], default='private', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('engagement_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='engagements', to='portfolio.engagementtype')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='engagements', to='portfolio.event')),
                ('primary_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='primary_engagements', to='portfolio.engagementrole')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engagements', to='portfolio.profile')),
            ],
            options={
                'ordering': ['-start_date', '-created_at', 'title'],
                'indexes': [
                    models.Index(fields=['profile', 'status'], name='eng_profile_status_idx'),
                    models.Index(fields=['profile', 'visibility'], name='eng_profile_visibility_idx'),
                    models.Index(fields=['profile', 'start_date'], name='eng_profile_start_idx'),
                    models.Index(fields=['profile', 'featured'], name='eng_profile_featured_idx'),
                    models.Index(fields=['profile', 'engagement_type'], name='eng_profile_type_idx'),
                ],
            },
        ),
        migrations.CreateModel(
            name='EngagementOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_role', models.CharField(choices=[('partner', 'Partner'), ('host', 'Host'), ('organizer', 'Organizer'), ('appointing_organization', 'Appointing Organization'), ('collaborating_organization', 'Collaborating Organization'), ('sponsor', 'Sponsor'), ('client', 'Client'), ('beneficiary_organization', 'Beneficiary Organization'), ('supporting_organization', 'Supporting Organization'), ('other', 'Other')], max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('engagement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_relationships', to='portfolio.engagement')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='engagement_relationships', to='portfolio.organization')),
            ],
            options={
                'ordering': ['organization__name'],
                'constraints': [
                    models.UniqueConstraint(fields=('engagement', 'organization', 'relationship_role'), name='unique_engagement_org_role'),
                ],
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='classifications',
            field=models.ManyToManyField(blank=True, related_name='organizations', to='portfolio.organizationclassification'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='awards',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.award'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='certificates',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.certificate'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='education',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.education'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='evidence',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.evidence'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='professional_memberships',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.professionalmembership'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.project'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='research',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.research'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.engagementrole'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.skill'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.tag'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='work_experiences',
            field=models.ManyToManyField(blank=True, related_name='engagements', to='portfolio.workexperience'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='organizations',
            field=models.ManyToManyField(blank=True, related_name='engagements', through='portfolio.EngagementOrganization', to='portfolio.organization'),
        ),
    ]
