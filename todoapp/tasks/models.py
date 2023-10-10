
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

from users.models import TodoUser


class Tasks(models.Model):

    task_id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name = CharField(max_length=64, blank=False, null=False, unique=False)
    task_description = CharField(max_length=500, blank=False, null=False, unique=False)
    created_by = DateTimeField(auto_now_add=True)
    task_completed = BooleanField(default=False)

    task_user = ForeignKey(to=TodoUser, on_delete=models.CASCADE, related_name='todo_user_tasks')

    
    def __str__(self) -> str:
        return f"{self.task_name} by "