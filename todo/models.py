from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # Explicit primary key
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)  # update only when obj created


class Task(models.Model):
    PRIORITY = [
        (0, "low"),
        (1, "mid"),
        (2, "high"),
    ]
    task_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY, default=1)
    description = models.CharField(max_length=100)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30, null=True, blank=True)


# To create
# 2. Tasks Table
# Column Name	Data Type	Constraints	Description
# task_id	INTEGER	Primary Key, Auto-increment	Unique identifier for each task.
# user_id	INTEGER	Foreign Key (Users.user_id)	Links the task to a specific user.
# title	VARCHAR(100)	Not Null	Title of the task.
# description	TEXT	Nullable	Detailed description of the task.
# is_completed	BOOLEAN	Default False	Whether the task is completed.
# priority	VARCHAR(10)	Default 'medium'	Task priority (e.g., low, medium, high).
# due_date	DATE	Nullable	Deadline for completing the task.
# created_at	TIMESTAMP	Default CURRENT_TIMESTAMP	Timestamp when the task was created.
# updated_at	TIMESTAMP	Default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	Last updated timestamp.
# 3. Categories Table (Optional)
# Column Name	Data Type	Constraints	Description
# category_id	INTEGER	Primary Key, Auto-increment	Unique identifier for each category.
# name	VARCHAR(50)	Unique, Not Null	Name of the category (e.g., Work, Personal).
# user_id	INTEGER	Foreign Key (Users.user_id)	Links category to a specific user.
# 4. Task Categories Table (Optional, for many-to-many relationship)
# Column Name	Data Type	Constraints	Description
# task_category_id	INTEGER	Primary Key, Auto-increment	Unique identifier for each mapping.
# task_id	INTEGER	Foreign Key (Tasks.task_id)	Links to the task.
# category_id	INTEGER	Foreign Key (Categories.category_id)	Links to the category.
# Relationships:
# Users → Tasks: A one-to-many relationship (each user can have multiple tasks).
# Users → Categories: A one-to-many relationship (each user can have multiple categories).
# Tasks → Categories: A many-to-many relationship (a task can belong to multiple categories, and a category can include multiple tasks).
