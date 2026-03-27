from django.db import models
from accounts.models import User

class Issue(models.Model):
    MISSING_MARKS = 'missing_marks'
    APPEAL = 'appeal'
    CORRECTION = 'correction'

    CATEGORY_CHOICES = [
        (MISSING_MARKS, 'Missing Marks'),
        (APPEAL, 'Appeal'),
        (CORRECTION, 'Correction'),
    ]

    OPEN = 'open'
    ASSIGNED = 'assigned'
    RESOLVED = 'resolved'

    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (ASSIGNED, 'Assigned'),
        (RESOLVED, 'Resolved'),
    ]

    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_issues')
    course_code = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AuditLog(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='logs')
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)