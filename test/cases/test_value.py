import pytest
import requests
import yaml
from config.config import ServerInfo

class TestValue():
    '''
    价值管理
    '''
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_ruleadd(self):
        '''
        价值规则-添加
        :return:
        '''
        u=ServerInfo.get_url('/value/rule')
        d={
            "day_by": 1,
            "id": "string",
            "month": 10,
            "name": "test_test",
            "period_list": [
                 {
                    "end_at": 5,
                    "growth_rate": 10,
                    "start_at": 1
                }
                            ],
            "salvage_rate": 0,
            "trigger_by": 0,
            "type": 1,
            "value_from": "1"
                }
        res=requests.post(url=u,json=d)
        assert res.status_code==200
        assert res.json()['code']==200
        return res.json()['data']['id']


    def test_ruleupdate(self):
        '''
        价值规则-编辑
        :return:
        '''
        A=self.test_ruleadd()
        d = {
            "day_by": 2,
            "id": "string",
            "month": 10,
            "name": "testandtest",
            "period_list": [
                {
                    "end_at": 5,
                    "growth_rate": 10,
                    "start_at": 1
                }
            ],
            "salvage_rate": 10,
            "trigger_by": 0,
            "type": 2,
            "value_from": "2"
                }
        u=ServerInfo.get_url('/value/rule/'+A)
        # print(u)
        res=requests.put(url=u,json=d)
        assert res.status_code==200
        assert res.json()['data']['name']=='testandtest'

    def test_ruledelete(self):
        '''
        价值规则-删除
        :return:
        '''
        A=self.test_ruleadd()
        u=ServerInfo.get_url('/value/rule/'+A)
        res=requests.delete(url=u)
        assert res.status_code==200
        assert res.json()['data']==A


    def test_rule_basicdata(self):
        '''
        基础数据获取
        :return:
        '''
        u=ServerInfo.get_url('/value/rule/basic-data')
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_rule_detail(self):
        '''
        价值规则-详情
        :return:
        '''
        A=self.test_ruleadd()
        u=ServerInfo.get_url('/value/rule/detail/'+A)
        res=requests.get(url=u)
        assert res.status_code==200
        assert res.json()['code']==200

    def test_rule_simulate(self):
        '''
        价值规则模拟
        :return:
        '''
        u=ServerInfo.get_url('/value/rule/simulate?num=100')
        d={
            "day_by": 1,
            "id": "string",
            "month": 0,
            "name": "",
            "period_list": [
                            {
                                "end_at": 3,
                                "growth_rate": 10,
                                "start_at": 1
                            }
                            ],
            "salvage_rate": 0,
            "trigger_by": 0,
            "type": 1,
            "value_from": "1"
            }
        res=requests.post(url=u,json=d)
        assert res.status_code==200
        assert res.json()['data']['Items'][2]['value']==120