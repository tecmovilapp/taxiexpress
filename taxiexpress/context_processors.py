from django.conf import settings # import the settings file

def admin_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'APP_VERSION': settings.APP_VERSION}