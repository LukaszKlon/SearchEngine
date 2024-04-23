from django.apps import AppConfig
from files import data_loader


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        AppConfig.dict,AppConfig.articles,AppConfig.Matrix,AppConfig.US,AppConfig.VT = data_loader.load_files()
        
        return super().ready()
