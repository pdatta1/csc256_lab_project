
import uuid
from typing import * 
from uuid import UUID
from datetime import datetime

from django.db import models
from django.db.models import ( 
    CharField,
    BooleanField,
    UUIDField,
    DateTimeField,
    ForeignKey
)

from users.models import TodoAppUser


class Tasks(models.Model):

    task_id: UUIDField[UUID] = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name: CharField[str] = CharField(max_length=64, blank=False, null=False, unique=False)
    task_description: CharField[str] = CharField(max_length=500, blank=False, null=False, unique=False)
    created_by: DateTimeField[datetime] = DateTimeField(auto_now_add=True)
    task_completed: BooleanField[bool] = BooleanField(default=False)

    task_user = ForeignKey(to=TodoAppUser, on_delete=models.CASCADE, related_name='user_tasks')

    
    def __str__(self) -> str:
        return f"{self.task_name} by "