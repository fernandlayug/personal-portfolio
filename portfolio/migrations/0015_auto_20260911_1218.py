from django.db import migrations, models
import django.db.models.deletion


DEFAULT_RELATIONSHIP_ROLES = [
    ("partner", "Partner"),
    ("host", "Host"),
    ("organizer", "Organizer"),
    ("appointing_organization", "Appointing Organization"),
    ("collaborating_organization", "Collaborating Organization"),
    ("sponsor", "Sponsor"),
    ("client", "Client"),
    ("beneficiary_organization", "Beneficiary Organization"),
    ("supporting_organization", "Supporting Organization"),
    ("other", "Other"),
]


def create_default_relationship_roles(apps, schema_editor):
    Profile = apps.get_model("portfolio", "Profile")
    OrganizationRelationshipRole = apps.get_model(
        "portfolio",
        "OrganizationRelationshipRole",
    )

    for profile in Profile.objects.all():
        for _, role_name in DEFAULT_RELATIONSHIP_ROLES:
            OrganizationRelationshipRole.objects.get_or_create(
                profile=profile,
                name=role_name,
            )


def migrate_relationship_roles(apps, schema_editor):
    EngagementOrganization = apps.get_model(
        "portfolio",
        "EngagementOrganization",
    )
    OrganizationRelationshipRole = apps.get_model(
        "portfolio",
        "OrganizationRelationshipRole",
    )

    role_lookup = {}

    for role in OrganizationRelationshipRole.objects.all():
        role_lookup[(role.profile_id, role.name)] = role.id

    value_to_name = {
        "partner": "Partner",
        "host": "Host",
        "organizer": "Organizer",
        "appointing_organization": "Appointing Organization",
        "collaborating_organization": "Collaborating Organization",
        "sponsor": "Sponsor",
        "client": "Client",
        "beneficiary_organization": "Beneficiary Organization",
        "supporting_organization": "Supporting Organization",
        "other": "Other",
    }

    for relationship in EngagementOrganization.objects.all().iterator():
        role_name = value_to_name.get(
            relationship.relationship_role,
            "Other",
        )

        role_id = role_lookup.get(
            (
                relationship.engagement.profile_id,
                role_name,
            )
        )

        if role_id is None:
            raise RuntimeError(
                "Could not find OrganizationRelationshipRole "
                f"'{role_name}' for profile "
                f"{relationship.engagement.profile_id}."
            )

        relationship.relationship_role_fk_id = role_id
        relationship.save(
            update_fields=["relationship_role_fk"]
        )


class Migration(migrations.Migration):

    dependencies = [
        (
            "portfolio",
            "0014_rename_evidence_profile_visibility_idx_evidence_visibility_idx_and_more",
        ),
    ]

    operations = [

        migrations.CreateModel(
            name="OrganizationRelationshipRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100),
                ),
                (
                    "description",
                    models.TextField(blank=True),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_relationship_roles",
                        to="portfolio.profile",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("profile", "name"),
                        name="unique_org_relationship_role_per_profile",
                    ),
                ],
            },
        ),

        migrations.AddField(
            model_name="engagementorganization",
            name="relationship_role_fk",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="engagement_relationships",
                to="portfolio.organizationrelationshiprole",
            ),
        ),

        migrations.RunPython(
            create_default_relationship_roles,
            migrations.RunPython.noop,
        ),

        migrations.RunPython(
            migrate_relationship_roles,
            migrations.RunPython.noop,
        ),

        migrations.RemoveConstraint(
            model_name="engagementorganization",
            name="unique_engagement_org_role",
        ),

        migrations.RemoveField(
            model_name="engagementorganization",
            name="relationship_role",
        ),

        migrations.RenameField(
            model_name="engagementorganization",
            old_name="relationship_role_fk",
            new_name="relationship_role",
        ),

        migrations.AlterField(
            model_name="engagementorganization",
            name="relationship_role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="engagement_relationships",
                to="portfolio.organizationrelationshiprole",
            ),
        ),

        migrations.AddConstraint(
            model_name="engagementorganization",
            constraint=models.UniqueConstraint(
                fields=(
                    "engagement",
                    "organization",
                    "relationship_role",
                ),
                name="unique_engagement_org_role",
            ),
        ),
    ]