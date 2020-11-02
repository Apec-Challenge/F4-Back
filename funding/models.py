from django.db import models


class Funding(models.Model):
    thumbnail_image = models.ImageField(default="",blank=True, null=True, upload_to="blog/%Y/%m/%d")
    place = models.ForeignKey("place.Place", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    owner_user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, blank=True, related_name="related_owner_user")
    backed_list = models.ManyToManyField("accounts.User", blank=True)
    content_image = models.ImageField(models.ImageField(default="",blank=True, null=True, upload_to="blog/%Y/%m/%d"))
    content_text = models.TextField(blank=True)
    cheering_comment = models.TextField(blank=True)
    funding_goal_amount = models.PositiveIntegerField(null=False,default=0)
    funding_amount = models.PositiveIntegerField(null=False,default=0)
    created_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # like = models.ManyToManyField(User, related_name='funding_likes',blank=True)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.user_likes.count()


class MainFunding(models.Model):
    main_funding = models.ManyToManyField(Funding, blank=True)


class FundingComment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, blank=False)
    funding = models.ForeignKey(Funding, related_name="comment_list", on_delete=models.CASCADE, blank=False)
    content = models.TextField(blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user.email
