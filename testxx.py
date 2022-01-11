
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import copy
import json
import math
import re
import six
import tensorflow as tf

class BertConfig(object):
    """Configuration for `BertModel`."""
    @classmethod
    def from_dict(cls, json_object):
        """Constructs a `BertConfig` from a Python dictionary of parameters."""
        config = BertConfig(vocab_size=21128)
        for (key, value) in six.iteritems(json_object):
            config.__dict__[key] = value
        return config

    @classmethod
    def from_json_file(cls, json_file):
        """Constructs a `BertConfig` from a json file of parameters."""
        with tf.compat.v1.gfile.GFile(json_file) as reader:#r改为rb，二进制模式
            text = reader.read()
            t1=json.loads(text)
            print(type(t1))
            print(t1)
        return cls.from_dict(t1)#更改为汉字编码格式gbk/gb2312/gb18030

bert_config = BertConfig.from_json_file("bert_config.json")
print(bert_config)
