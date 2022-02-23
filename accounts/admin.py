from django.contrib import admin

from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin


from .models import Submissions, User, Judgement

# Register your models here.

class SubmissionsResource(resources.ModelResource):

    total = Field()

    class Meta:
        model = Submissions
        export_order = (
            'id',
            'title',
            'description',
            'devfolio_link',
            'codebase_link',
            'team_name',
            'member_name',
            'member_email',
            'member_phone',
            'judges_assigned',
            'total'
        )

    def dehydrate_total(self, submission):
        return submission.total()

class SubmissionsAdmin(ImportExportModelAdmin):
    resource_class = SubmissionsResource

admin.site.register(User)
admin.site.register(Judgement)
admin.site.register(Submissions, SubmissionsAdmin)