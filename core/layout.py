"""core/layout.py"""
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    """Suit Layout."""

    layout = 'vertical'

    menu_show_home = False

    menu = (
        ParentItem('General', children=[
            ChildItem('Carreras', url='/admin/taxiadmin/rides'),
            ChildItem(model='taxiadmin.driver'),
            ChildItem(model='taxiadmin.passenger'),            
            ChildItem(model='taxiadmin.vehicle'), 
            ChildItem(model='core.documents'),          
        ], icon='fa fa-home'),
        ParentItem('Configuraciones', children=[
            ChildItem(model='taxiadmin.vehiclemaker'),
            ChildItem(model='taxiadmin.vehiclemodel'), 
            ChildItem(model='core.documenttypes'), 
        ], icon='fa fa-cog'),
        ParentItem('Users', children=[
            ChildItem('Usuarios', 'auth.user'),
        ], icon='fa fa-users'),
        #ParentItem('Right Side Menu', children=[
        #    ChildItem('Password change', url='admin:password_change'),
        #    ChildItem('Open Google', url='http://google.com', target_blank=True),
        #], align_right=True, icon='fa fa-cog'),
    )
    
    def ready(self):
        super(SuitConfig, self).ready()
    
    def prevent_user_last_login(self):
        """
        Disconnect last login signal
        """
        from django.contrib.auth import user_logged_in
        from django.contrib.auth.models import update_last_login
        user_logged_in.disconnect(update_last_login)
