import pytest
import requests
import yaml
from config.config import ServerInfo
with open (r'C:\Users\admin\Desktop\xiangmu\data\test_assets.yaml','r',encoding='utf-8') as f:
    data=yaml.safe_load(f)

class  TestAssets():
    def setup(self):
        pass
    def teardown(self):
        pass

    @pytest.mark.parametrize("id,expect1,expect2",data['设备管理详情-获取'])
    def test_get_device_details(self,id,expect1,expect2):
        """
        设备管理详情-获取
        """
        u=ServerInfo.get_url(f'/assets/device/detail/{id}')
        res=requests.get(url=u)
        assert res.status_code==expect1
        assert res.json()['code']==expect2


    # @pytest.mark.parametrize("id,expect1,expect2", [('96cd96c50b12c10de05013ac0c881b04new', 200, 200),
    #                                                 ('1111111111', 200, 500), (None, 200,500)])
    # @pytest.skip
    # def test_get_device_details_op(self, id, expect1, expect2):
    #     """
    #     设备管理详情-运营信息
    #     """
    #     u = ServerInfo.get_url(f'/assets/device/detail/{id}/op')
    #     res = requests.get(url=u)
    #     assert res.status_code == expect1
    #     assert res.json()['code'] == expect2
    #
    @pytest.mark.parametrize("id,expect1,expect2",data['设备管理详情-权限'])
    def test_get_device_details_property(self, id, expect1, expect2):
        """
        设备管理详情-权限
        """
        u = ServerInfo.get_url(f'/assets/device/detail/{id}/property')
        res = requests.get(url=u)
        assert res.status_code == expect1
        assert res.json()['code'] == expect2

    @pytest.mark.parametrize("id,expect1,expect2", data['设备管理详情-价值信息'])
    def test_get_device_details_vaule(self, id, expect1, expect2):
        """
        设备管理详情-价值信息
        """
        u = ServerInfo.get_url(f'/assets/device/detail/{id}/value')
        res = requests.get(url=u)
        assert res.status_code == expect1
        assert res.json()['code'] == expect2
    # @
    # def test_get_device_details_warning(self, id, expect1, expect2):
    #     """
    #     设备管理详情-预警信息
    #     """
    #     u = ServerInfo.get_url(f'/assets/device/detail/{id}/warning')
    #     res = requests.get(url=u)
    #     assert res.status_code == expect1
    #     assert res.json()['code'] == expect2


    def test_get_device_pagesize(self):
        """
        设备管理-分页查询
        """
        u = ServerInfo.get_url('/assets/device/page/1/size/20')
        res = requests.get(url=u)
        assert res.status_code == 200
        assert (len(res.json()['data']['list']))==20

    def test_get_device_typelist(self):
        """
        设备类型列表获取
        """
        u = ServerInfo.get_url('/assets/device/type/list')
        res = requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200


    def test_get_device_typetree(self):
        """
        设备类型树获取
        """
        u = ServerInfo.get_url('/assets/device/type/tree')
        res = requests.get(url=u)
        assert res.status_code == 200
        assert res.json()['code'] == 200

    # def test_get_device_write(self):
    #     """
    #     设备管理-编辑
    #     """
    #     u = ServerInfo.get_url('/assets/device/{ip}')
    #     res = requests.put(url=u)
    #     assert res.status_code == 200
    #     assert res.json()['code'] == 200

