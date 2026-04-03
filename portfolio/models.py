from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    career_goals = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework / Library'),
        ('tool', 'Tool / Software'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(default=80, help_text='Percentage 0-100')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text='Comma-separated list of tools/technologies')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def get_tech_list(self):
        return [t.strip() for t in self.technologies.split(',')]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField(null=True, blank=True, help_text='Leave blank if currently enrolled')
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def year_range(self):
        if self.year_end:
            return f"{self.year_start} – {self.year_end}"
        return f"{self.year_start} – Present"

    def __str__(self):
        return f"{self.degree} at {self.school}"

    class Meta:
        ordering = ['-year_start']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} ({self.sent_at.strftime('%Y-%m-%d')})"

    class Meta:
        ordering = ['-sent_at']
