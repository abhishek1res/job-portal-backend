from dashboard.models import JobPost, JobApplication
from rest_framework import serializers

class JobPostSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    
    def get_poster(self, obj):
        return obj.poster.email
    class Meta:
        model = JobPost
        exclude = ["date_posted", "last_updated", "slug"]
    def validate(self, data):
        # Check if a job with the same title and company already exists
     if JobPost.objects.filter(job_title=data["job_title"], company=data["company"]).exists():
        raise serializers.ValidationError("A job with this title already exists for this company.")
     return data   

class JobApplicationSerializer(serializers.ModelSerializer):
    job_review = serializers.SerializerMethodField()
    
    def get_job_review(self, obj):
        return obj.review
    class Meta:
        model = JobApplication
        exclude = ["job_post", "review"]
    

class JobApplicationSerializerForPoster(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        exclude = ["job_post"]