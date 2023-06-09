# Generated by Django 4.2.1 on 2023-05-17 09:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BooksTable",
            fields=[
                (
                    "borrowed_date",
                    models.DateField(
                        auto_created=True, null=True, verbose_name="Borrowed Date"
                    ),
                ),
                (
                    "published_date",
                    models.DateField(
                        auto_created=True, help_text="Date Book Published", null=True
                    ),
                ),
                (
                    "books_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        default="xxx-xxxxxx",
                        max_length=10,
                        null=True,
                        validators=[product.models.BooksTable.validate_isbn],
                        verbose_name="ISBN Number",
                    ),
                ),
                (
                    "book_title",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Book Title"
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Book Author"
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("Farsi", "Farsi"),
                            ("English", "English"),
                            ("French", "French"),
                            ("Russian", "Russian"),
                            ("Spanish", "Spanish"),
                            ("Arabic", "Arabic"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "short_description",
                    models.TextField(
                        max_length=200, null=True, verbose_name="Short Description"
                    ),
                ),
                (
                    "genere",
                    models.CharField(
                        choices=[
                            ("Fiction", "Fiction"),
                            ("Mystery", "Mystery"),
                            ("Romance", "Romance"),
                            ("Science Fiction", "Science Fiction"),
                            ("Fantasy", "Fantasy"),
                            ("Thriller", "Thriller"),
                            ("Horror", "Horror"),
                            ("Biography", "Biography"),
                            ("History", "History"),
                            ("Poetry", "Poetry"),
                            ("Self-Help", "Self-Help"),
                            ("Business", "Business"),
                            ("Travel", "Travel"),
                            ("Children's", ""),
                            ("Young Adult", "Young Adult"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        default=False, null=True, verbose_name="Availablity"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StaffsTable",
            fields=[
                (
                    "staffs_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Id"
                    ),
                ),
                (
                    "staffs_no",
                    models.CharField(max_length=10, verbose_name="Staffs Number"),
                ),
                (
                    "staffs_name",
                    models.CharField(max_length=50, verbose_name="Full Name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PublicationsTable",
            fields=[
                (
                    "publication_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                (
                    "publication_national_id",
                    models.CharField(
                        max_length=30,
                        null=True,
                        unique=True,
                        verbose_name="Publication National Id",
                    ),
                ),
                (
                    "publication_name",
                    models.CharField(
                        max_length=30,
                        null=True,
                        unique=True,
                        verbose_name="Publication name",
                    ),
                ),
                (
                    "address",
                    models.CharField(max_length=50, null=True, verbose_name="Address"),
                ),
                (
                    "books_list",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.bookstable",
                        verbose_name="Books List",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MembersTable",
            fields=[
                (
                    "members_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                (
                    "national_id",
                    models.CharField(max_length=10, verbose_name="National ID"),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Full Name"
                    ),
                ),
                (
                    "address",
                    models.CharField(max_length=50, null=True, verbose_name="City"),
                ),
                (
                    "membership_date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Membership Date",
                    ),
                ),
                (
                    "end_membership",
                    models.DateField(
                        blank=True, null=True, verbose_name="End Membership Date"
                    ),
                ),
                (
                    "books_borrowed",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.bookstable",
                        verbose_name="Books Borrowed",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bookstable",
            name="borrowed_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.memberstable",
                verbose_name="Borrowed By",
            ),
        ),
        migrations.AddField(
            model_name="bookstable",
            name="publication",
            field=models.ManyToManyField(to="product.publicationstable"),
        ),
        migrations.AddField(
            model_name="bookstable",
            name="staffs",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.staffstable",
                verbose_name="Staffs",
            ),
        ),
    ]
