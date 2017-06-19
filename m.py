#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""自定义工具类
@Created on 2017-4-5
@See
"""

import urllib
import json


class m:
    """
    @工具类，实现各种值设置及提取
    """

    def __init__(self):
        pass

    @staticmethod
    def _p_t(o):
        print(type(o))

    @staticmethod
    def get_value_from_json_str(json_str, key_str):
        """
        :rtype str

        :return the key's value from the json_str

        :param
        """
        json_dict = json.loads(json_str)
        assert not m.__get_value_from_dict(json_dict, 'errorCode'), 'errorCode is not 0'
        value = m.__get_value_from_dict(json_dict, key_str)
        return value

    @staticmethod
    def __get_value_from_dict(json_dict, key_str):
        """
        :rtype str

        :return the key's value from the json_dict

        :param
        """
        for (k, v) in json_dict.items():
            if isinstance(v, dict):
                value = m.__get_value_from_dict(v, key_str)
                if value:
                    return value
            if isinstance(v, list):
                for l in v:
                    value = m.__get_value_from_dict(l, key_str)
                    if value:
                        return value
            if key_str == k:
                value = v
                return value

    @staticmethod
    def set_url_value(url_str=None, args_dic=None):
        """
        :rtype json_str

        :return the new json_str that had replace the parameter from the args_dic

        :param
        """
        url_str = urllib.unquote(url_str)
        para_url_dic = json.loads(url_str[url_str.index('=') + 1:])
        for key, value in args_dic.items():
            new_dic = m.__set_dic_value(para_url_dic, key, value)
        return json.dumps(new_dic)

    @staticmethod
    def set_post_value(post_str=None, args_dict=None):
        """
        :rtype new_dic

        :return the new_dic had replace the parameter in the args_dict from the post_str

        :param
        """
        assert (post_str and args_dict), 'post_str or args_dict is none.'
        post_str_dict = json.loads(post_str)
        for k, v in args_dict.items():
            new_dic = m.__set_dic_value(post_str_dict, k, v)
        return new_dic

    @staticmethod
    def set_list_value(pending_dic=None, key_str=None, args_dict=None, list_index=0):
        """
        :rtype dict

        :return the new_dic that had replace the key's value from the args_dict by which is a list in a dic

        :param
        """
        assert (pending_dic and key_str and args_dict), "pending_dic or key or args_dict is none."
        list_u = pending_dic[key_str]
        for k, v in args_dict.items():
            new_dic = m.__set_dic_value(list_u[list_index], k, v)
            new_list = [list_index + 1]
            new_list[list_index] = new_dic
        return m.__set_dic_value(pending_dic, key_str, new_list)

    @staticmethod
    def __set_dic_value(dic=None, key_str=None, value_str=None):
        """
        :rtype dic

        :return the new_dic that had replace the key's value with the new value

        :param
        """
        assert (dic and key_str and value_str), 'dic or key or value is none.'
        for (k, v) in dic.items():
            if key_str == k:
                dic[k] = value_str
                return dic
            if isinstance(v, dict):
                res = m.__set_dic_value(v, key_str, value_str)
                if not res:
                    continue
                dic[k] = res
                return dic


if __name__ == '__main__':
    pass
