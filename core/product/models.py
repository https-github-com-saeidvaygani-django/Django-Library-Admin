from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import timedelta
import re

class BooksTable(models.Model):
    language_choices = (
        ('Farsi','Farsi'),
        ('English','English'),
        ('French','French'),
        ('Russian','Russian'),
        ('Spanish','Spanish'),
        ('Arabic','Arabic'),
    )
    genere_choices = (
        ('Fiction','Fiction'),('Mystery','Mystery'),('Romance','Romance'),('Science Fiction','Science Fiction'),('Fantasy','Fantasy'),('Thriller','Thriller'),
('Horror','Horror'),('Biography','Biography'),('History','History'),('Poetry','Poetry'),('Self-Help','Self-Help'),('Business','Business'),
('Travel','Travel'),("Children's",""),('Young Adult','Young Adult'))
    def validate_isbn(value):
        pattern = r'^\d{3}-\d{6}$'
        if not re.match(pattern, value):
            raise ValidationError('Invalid ISBN format. The ISBN should be in the format xxx-xxxxxx.')
        
    books_id = models.AutoField(primary_key=True, verbose_name="id")
    isbn = models.CharField(null=True, default='xxx-xxxxxx', verbose_name='ISBN Number',max_length=10,validators=[validate_isbn])
    book_title = models.CharField(max_length=50, null=True, verbose_name='Book Title')
    author = models.CharField(max_length=50, null=True, verbose_name='Book Author')
    publication = models.ManyToManyField('PublicationsTable')
    published_date = models.DateField(auto_created=True, help_text='Date Book Published', null=True)
    language = models.CharField(max_length=50, choices=language_choices, null=True)
    short_description = models.TextField(max_length=200, verbose_name='Short Description', null=True)
    genere = models.CharField(max_length=50, choices=genere_choices, null=True)
    status = models.BooleanField(default=False, null=True, verbose_name="Availablity")
    borrowed_by = models.ForeignKey('MembersTable', verbose_name='Borrowed By', on_delete=models.CASCADE, null=True)
    staffs = models.ForeignKey('StaffsTable', verbose_name="Staffs", null=True, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_created=True, verbose_name="Borrowed Date", null=True)
    
    def __str__(self):
        return self.name

def get_end_membership_default():
    return timezone.now() + timedelta(days=180)

class MembersTable(models.Model):
    members_id = models.AutoField(primary_key=True, verbose_name="id")
    national_id = models.CharField(max_length=10, verbose_name="National ID")
    name = models.CharField(max_length=50, verbose_name="Full Name", null=True)
    address = models.CharField(max_length=50, verbose_name="City", null=True)
    membership_date = models.DateField(default=timezone.now, verbose_name="Membership Date", null=True)
    end_membership = models.DateField(verbose_name="End Membership Date", null=True, blank=True)
    books_borrowed = models.ForeignKey('BooksTable', verbose_name="Books Borrowed", on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.end_membership:
            self.end_membership = self.membership_date + timedelta(days=180)
        super().save(*args, **kwargs)
    
class PublicationsTable(models.Model):
    publication_id = models.AutoField(primary_key=True, verbose_name='id')
    publication_national_id = models.CharField(verbose_name="Publication National Id", unique=True, null=True, max_length=30)
    publication_name = models.CharField(verbose_name="Publication name", max_length=30, null=True, unique=True)
    address = models.CharField(verbose_name="Address", max_length=50, null=True)
    books_list = models.ForeignKey('BooksTable', verbose_name="Books List",on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.publication_name
    
    
class StaffsTable(models.Model):
    staffs_id = models.AutoField(primary_key=True, verbose_name="Id")
    staffs_no = models.CharField(verbose_name="Staffs Number", max_length=10)
    staffs_name = models.CharField(verbose_name="Full Name", max_length=50)
    
    def __str__(self):
        return self.staffs_name