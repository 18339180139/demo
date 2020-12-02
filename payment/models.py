from django.db import models

# Create your models here.

# （1）用户表， 存储用户id，用户名，用户邮箱，用户手机号
class User(models.Model):
    user_name = models.CharField(max_length=32, verbose_name="用户名")
    email = models.CharField(max_length=32, verbose_name="用户邮箱")
    phone = models.CharField(max_length=32, verbose_name="用户手机号")

# （2）用户账户表，存储用户的账号，余额，如用户A的帐号是6225xxxx3344， 余额是500， 用户B的帐号是5525xxxx5555， 余额是5600
class Accout(models.Model):
    accout_name= models.CharField(max_length=32, verbose_name="用户账号")
    accout_balance = models.DecimalField(max_digits=6, decimal_places=2,  verbose_name="用户余额")
    user_id = models.ForeignKey("User", related_name='accout', on_delete=models.CASCADE, verbose_name="用户名")

# （3）用户交易表，存储所有用户的每一笔交易信息，包括关联的账户，关联的用户，交易金额，交易日期，交易状态（交易中，交易成功，交易失败）
#     如：用户A于2020-10-25在账户XXXXX中交易500块
class Trade(models.Model):
    status_choices = (
        (0, '交易中'),
        (1, '交易成功'),
        (2, '交易失败'),
    )
    accout = models.ForeignKey("User", related_name='trade_accout', on_delete=models.CASCADE, verbose_name="关联账户")
    user = models.ForeignKey("Accout", related_name='trade_user', on_delete=models.CASCADE, verbose_name="关联用户")
    trade_amount = models.DecimalField(max_digits=6, decimal_places=2,  verbose_name="交易金额")
    trade_date = models.DateTimeField(verbose_name="交易日期", auto_now_add=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="交易状态")

