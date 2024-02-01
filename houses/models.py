from django.db import models


# Create your models here.
# 모델은 어플리케이션에서 데이터의 모양을 묘사한 것
# Model은 django의 Model 클래스를 상속받아야함
class House(models.Model):
    # 모델에 필요한 데이터를 설정
    """
    House Model Definition for Houses
    """
    name = models.CharField(max_length=140)  # name 필드, 문자열, 최대140자 제한
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price",
        help_text="Positive Numbers Only",
    )  # price 필드, 양수
    description = models.TextField()  # description 필드, 문자열
    address = models.CharField(max_length=140)  # address 필드, 문자열, 최대 140자 제한
    pets_allowed = models.BooleanField(
        default=True,
        verbose_name="Pets Allowed?",
        help_text="Does this house allow pets?",
    )  # pets_allowed, Boolean, 기본값 True

    # owner 필드를 user앱의 User 모델과 CASCADE Relationship 지정
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
