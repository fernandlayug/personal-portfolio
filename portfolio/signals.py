from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify

from .models import Profile


def generate_portfolio_slug(username, user_id):
    """
    Generate a DNS-safe portfolio slug.

    Allowed characters:
    - lowercase letters
    - numbers
    - hyphens
    """

    base_slug = slugify(username)

    # Convert underscores to hyphens
    base_slug = base_slug.replace('_', '-')

    # Remove anything that is not a letter, number, or hyphen
    base_slug = ''.join(
        char
        for char in base_slug
        if char.isalnum() or char == '-'
    )

    # Remove duplicate hyphens
    while '--' in base_slug:
        base_slug = base_slug.replace('--', '-')

    # Remove leading/trailing hyphens
    base_slug = base_slug.strip('-')

    # Fallback if username produces no valid slug
    if not base_slug:
        base_slug = f"user-{user_id}"

    # DNS labels have a maximum length of 63 characters
    base_slug = base_slug[:63].rstrip('-')

    slug = base_slug
    counter = 1

    while Profile.objects.filter(
        portfolio_slug=slug
    ).exists():

        suffix = f"-{counter}"

        # Keep total hostname label within 63 characters
        slug = (
            f"{base_slug[:63 - len(suffix)]}"
            f"{suffix}"
        )

        counter += 1

    return slug


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if not created:
        return

    slug = generate_portfolio_slug(
        instance.username,
        instance.id
    )

    Profile.objects.create(
        user=instance,
        portfolio_slug=slug,
        full_name=(
            instance.get_full_name()
            or instance.username
        ),
        professional_title='',
        bio='',
        email=instance.email or '',
    )