import requests

from config.config import ServerInfo

import pytest


class TestDataCenter():
    """
    数据中心
    """
    def test_aircraft_civil_op(self):
        """
        通用飞机管理—详情-运营信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/civil/detail/{id}/op'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_civil_property(self):
        """
        通用飞机管理—详情-权限信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/civil/detail/{id}/property'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_civil_value(self):
        """
        通用飞机管理—详情-价值信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/civil/detail/{id}/value'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_civil_warning(self):
        """
        通用飞机管理—详情-预警信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/civil/detail/{id}/warning'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_pagesize(self):
        """
        通用飞机管理分页获取
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/civil/page/{page}/size/{size}'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_commercial_op(self):
        """
        商用飞机管理-详情-运营信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/commercial/detail/{id}/op'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_commercial_property(self):
        """
        商用飞机管理-详情-权限信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/commercial/detail/{id}/property'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_commercial_value(self):
        """
        商用飞机管理-详情-价值信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/commercial/detail/{id}/value'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_aircraft_commercial_warning(self):
        """
        商用飞机管理-详情-预警信息
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/commercial/detail/{id}/warning'))
        assert res.status_code ==
        assert res['msg'] ==

    @pytest.mark.p0
    def test_aircraft_commercial_pagesizi(self):
        """
        商用飞机管理-分页获取
        """
        res = requests.get(ServerInfo.get_url('/data/aircraft/commercial/page/1/size/30'))
        print(res.text)
        # assert res.status_code ==
        # assert res['msg'] ==

    def test_newenergy_op(self):
        """
        新能源管理详情-运营信息
        """
        res = requests.get(ServerInfo.get_url('/data/new-energy/detail/{id}/op'))
        assert res.status_code ==
        assert res['msg'] ==

    def test_newenergy_property(self):
        """
            新能源管理详情-权限信息
        """
        res = requests.get(ServerInfo.get_url('/data/new-energy/detail/{id}/property'))
        assert res.status_code ==
        assert res['msg'] ==


    def test_mark(self):
        assert True

