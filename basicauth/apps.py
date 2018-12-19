from django.apps import AppConfig


class BasicauthConfig(AppConfig):
    name = 'basicauth'

    def ready(self):
        import basicauth.signals
