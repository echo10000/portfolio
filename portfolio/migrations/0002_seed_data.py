from django.db import migrations


def seed_data(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Education = apps.get_model('portfolio', 'Education')

    # Profile
    Profile.objects.create(
        name='Jericho Blando',
        tagline='IT student & aspiring developer building clean, purposeful software.',
        bio=(
            "I'm Jericho Blando, an Information Technology student with a strong passion for "
            "web development, problem-solving, and building applications that make a real difference. "
            "I enjoy turning ideas into working software using clean, maintainable code."
        ),
        career_goals=(
            "My goal is to become a full-stack developer specializing in Django and modern JavaScript "
            "frameworks. I'm driven by curiosity and a desire to keep growing — both technically and "
            "as a collaborator who can work effectively in team environments."
        ),
        email='jericho.blando@example.com',
        github='https://github.com/jericho-blando',
        linkedin='https://linkedin.com/in/jericho-blando',
    )

    # Skills
    skills_data = [
        ('Python', 'language', 85, 1),
        ('HTML & CSS', 'language', 90, 2),
        ('JavaScript', 'language', 75, 3),
        ('SQL', 'language', 70, 4),
        ('Django', 'framework', 80, 1),
        ('Bootstrap', 'framework', 85, 2),
        ('Git & GitHub', 'tool', 80, 1),
        ('MySQL', 'tool', 75, 2),
        ('VS Code', 'tool', 90, 3),
        ('PythonAnywhere', 'tool', 70, 4),
    ]
    for name, cat, prof, order in skills_data:
        Skill.objects.create(name=name, category=cat, proficiency=prof, order=order)

    # Projects
    projects_data = [
        (
            'Personal Portfolio Website',
            'A dynamic personal portfolio website built with Django, showcasing my projects, '
            'skills, education, and contact information. Deployed on PythonAnywhere.',
            'Django, Python, HTML, CSS, MySQL',
            'https://github.com/jericho-blando/portfolio',
            '',
            True,
            1,
        ),
        (
            'Student Information System',
            'A web-based system for managing student records, including enrollment, grading, '
            'and attendance tracking. Built using Django with a MySQL database backend.',
            'Django, Python, MySQL, Bootstrap',
            'https://github.com/jericho-blando/student-info-system',
            '',
            False,
            2,
        ),
        (
            'Library Management System',
            'A simple library management app that lets librarians manage book inventory, '
            'track borrowing history, and manage member accounts.',
            'Python, Django, SQLite, Bootstrap',
            'https://github.com/jericho-blando/library-management',
            '',
            False,
            3,
        ),
    ]
    for title, desc, tech, gh, live, feat, order in projects_data:
        Project.objects.create(
            title=title, description=desc, technologies=tech,
            github_link=gh, live_link=live, featured=feat, order=order,
        )

    # Education
    Education.objects.create(
        school='Your University / College Name',
        degree='Bachelor of Science in Information Technology',
        year_start=2022,
        year_end=None,
        description='Currently enrolled. Relevant coursework: Web Development, Database Management, '
                    'Object-Oriented Programming, Systems Analysis & Design.',
        order=1,
    )


def unseed_data(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Education = apps.get_model('portfolio', 'Education')
    Profile.objects.all().delete()
    Skill.objects.all().delete()
    Project.objects.all().delete()
    Education.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
