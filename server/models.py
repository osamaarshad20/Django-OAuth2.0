from django.db import models

# Create your models here.
from oauth2_provider.models import AbstractApplication

class MyApplication(AbstractApplication):
    def allows_grant_type(self, *grant_types):
        # Assume, for this example, that self.authorization_grant_type is set to self.GRANT_AUTHORIZATION_CODE
        return bool( set([self.authorization_grant_type, self.GRANT_PASSWORD]) & set(grant_types) )
