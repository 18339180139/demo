from django.contrib import admin

# Register your models here.
from payment.models import User, Trade, Accout
class TradeInfoAdmin(admin.ModelAdmin):
    list_display = ['accout','user','trade_amount','trade_date','status','is_exceed_200']
    def is_exceed_200(self,obj):
        if obj.trade_amount>=200:
            return 'yes'
        elif obj.trade_amount<=200:
            return 'no'
    is_exceed_200.short_description = '交易额的大小情况'  # 这里可写可不写，题目没要求

    def trade_amount(self,obj):
        trade_amount=obj.trade_amount

        return trade_amount+'RMB'

    trade_amount.short_description='交易金额' #加了RMB之后的



admin.site.register(User)
admin.site.register(Trade,TradeInfoAdmin)
admin.site.register(Accout)

