from django.contrib import admin
from .models import BooksTable, MembersTable, PublicationsTable, StaffsTable
from django.db import models

class BooksTableAdmin(admin.ModelAdmin):
    list_display = ('books_id','isbn','book_title','author','published_date','language','short_description','genere','status','borrowed_by','staffs','borrowed_date')
    list_display_links = ('books_id','isbn','book_title','author','published_date','language','short_description','genere','status','borrowed_by','staffs','borrowed_date')
    list_filter = ('publication','language','genere')
    search_fields = ('book_title',)
    sortable_by = ('language',)
    ordering =('books_id',)
    date_hierarchy = 'published_date'
    
class MembersTableAdmin(admin.ModelAdmin):
    list_display = ('members_id','national_id','name','address','membership_date','end_membership')
    list_display_links = ('members_id','national_id','name','address','membership_date','end_membership')
    list_filter = ('address',)
    search_fields = ('name',)
    sortable_by = ('address',)
    ordering =('members_id',)
    date_hierarchy = 'membership_date'

class PublicationsTableAdmin(admin.ModelAdmin):
    list_display = ('publication_id','publication_national_id','publication_name','address')
    list_display_links = ('publication_id','publication_national_id','publication_name','address')
    list_filter = ('address',)
    search_fields = ('publication_name',)
    sortable_by = ('publication_id',)
    ordering =('publication_id',)

class StaffsTableAdmin(admin.ModelAdmin):
    list_display = ('staffs_id','staffs_no','staffs_name')
    list_display_links = ('staffs_id','staffs_no','staffs_name')
    list_filter = ('staffs_name',)
    search_fields = ('staffs_name',)
    sortable_by = ('staffs_id',)
    ordering =('staffs_id',)

admin.site.register(BooksTable, BooksTableAdmin)
admin.site.register(MembersTable, MembersTableAdmin)
admin.site.register(PublicationsTable, PublicationsTableAdmin)
admin.site.register(StaffsTable, StaffsTableAdmin)