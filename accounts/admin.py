from django.contrib import admin

from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin


from .models import Submissions, User, Judgement

# Register your models here.

class SubmissionsResource(resources.ModelResource):

    total = Field()
    Judge1 = Field()
    Judge2 = Field()
    judge_1_marks = Field()
    judge_1_total = Field()
    judge_2_marks = Field()
    judge_2_total = Field()

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
            'Judge1',
            'Judge2',
            'judge_1_marks',
            'judge_1_total',
            'judge_2_marks',
            'judge_2_total',
            'total'

        )

    def dehydrate_total(self, submission):
        return submission.total()
    
    def dehydrate_Judge1(self, submission):
        return submission.Judge1()
    
    def dehydrate_Judge2(self, submission):
        return submission.Judge2()
    
    def dehydrate_judge_1_marks(self, submission):
        return submission.judge_1_marks()
   
    def dehydrate_judge_1_total(self, submission):
        return submission.judge_1_total()
    
    def dehydrate_judge_2_marks(self, submission):
        return submission.judge_2_marks()
   
    def dehydrate_judge_2_total(self, submission):
        return submission.judge_2_total()

class SubmissionsAdmin(ImportExportModelAdmin):
    resource_class = SubmissionsResource

admin.site.register(User)
admin.site.register(Judgement)
admin.site.register(Submissions, SubmissionsAdmin)