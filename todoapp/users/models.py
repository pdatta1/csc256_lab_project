
from typing import * 

from django.db import models
from django.db.models import ( 
    CharField,
    BooleanField,

)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.manager import TodoUserManager

class TodoUser(AbstractBaseUser, PermissionsMixin): 
    """"
        Here is the Todo App User Model, which has the username field and some
        core fields.
    """

    username = CharField(max_length=24, blank=False, null=False, unique=True)

    # account_status 

    is_active = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    # core 
    REQUIRED_FIELDS: List[str] = [] 
    USERNAME_FIELD: Literal['username'] = 'username'
    objects: TodoUserManager = TodoUserManager() 

    def __str__(self) -> str:
        return f"[{self.username}] Account"
    



