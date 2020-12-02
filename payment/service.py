from django.shortcuts import HttpResponse
from django.db import transaction

from payment.models import Trade, Accout, User


def get_info(request):
    '''返回交易总额最多的前三个用户id和金额'''
    starttime = request.GET['starttime']
    endtime = request.GET['endtime']
    trade=Trade.objects.filter(trade_date__range=(starttime,endtime)).annotate('accout_id').values(sum('trade_amount'))
    trade_1=trade[0]['trade_amount']
    trade_2 = trade[1]['trade_amount']
    trade_3 = trade[2]['trade_amount']
    id_1=trade[0]['accout_id']
    id_2 = trade[0]['accout_id']
    id_3 = trade[0]['accout_id']
    return HttpResponse('交易总额最大的前三名的id是{}、{}、{}，他们各自的交易总额是{}、{}、{}'.format(id_1,id_2,id_3,trade_1,trade_2,trade_3))

def transfer(request):
    '''转账'''
    '''
    money:要转账的金额
    account_A:要转出的账户
    account_B:要转入的账户
    user_A；转出的用户
    user_B:转入的用户
    '''
    money=request.GET['money']
    account_A=request.GET['account_A']
    account_B = request.GET['account_B']
    user_A=request.GET['user_A']
    user_B=request.GET['user_B']
    accout_A = Accout.objects.get(accout_name=account_A)
    accout_B = Accout.objects.get(accout_name=account_B)
    user_A=User.objects.get(user_name=user_A)
    user_B=User.objects.get(user_B)
    try:
        with transaction.atomic():
            '''事务控制，原子操作'''
            accout_A.accout_balance-=money
            accout_B.accout_balance+=money
            trade_A=Trade(accout=accout_A,user=user_A,trade_amount=money,status=1)
            trade_B = Trade(accout=accout_B, user=user_B, trade_amount=money, status=1)
            trade_A.save()
            trade_B.save()

    except:
        return HttpResponse('转账错误')