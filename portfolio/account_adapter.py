from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class PortfolioAccountAdapter(DefaultAccountAdapter):

    def get_signup_redirect_url(self, request):
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

        return portfolio_url

    def get_login_redirect_url(self, request):
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

        return portfolio_url