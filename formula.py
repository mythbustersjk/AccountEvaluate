"""
客户指标计算公式
"""


class JcFormula:
    """
    jc_value:基础户年日均门槛值，该值由setting.json设置。
    current_amount:账户现年日均值。使用jc_amount_formula和jc_need_days_formula方法时必须需提供该值。
    current_balance:账户现余额。使用jc_need_days_formula方法时必须提供该值。
    jc_days:客户资金预计留存天数。使用jc_amount_formula方法时必须提供该值。
    """

    def __init__(self, jc_value, current_amount, current_balance=0, jc_days=0):
        self.jc_value = jc_value
        self.current_amount = current_amount
        self.current_balance = current_balance
        self.jc_days = jc_days

    def jc_amount_formula(self):
        jc_need_amount = (float(self.jc_value) - float(self.current_amount)) * 365 / float(self.jc_days)
        return jc_need_amount

    def jc_need_days_formula(self):
        jc_need_days = (float(self.jc_value) - float(self.current_amount)) * 365 / float(self.current_balance)
        return jc_need_days


class YxFormula:
    """
    yx_value:基础户年日均门槛值，该值由setting.json设置。
    current_amount:账户现年日均值。使用yx_amount_formula和yx_need_days_formula方法时必须需提供该值。
    current_balance:账户现余额。使用yx_need_days_formula方法时必须提供该值。
    yx_days:客户资金预计留存天数。使用yx_amount_formula方法时必须提供该值。
    """

    def __init__(self, yx_value, current_amount, current_balance=0, yx_days=0):
        self.yx_value = float(yx_value)
        self.current_amount = float(current_amount)
        self.current_balance = float(current_balance)
        self.yx_days = float(yx_days)

    def yx_amount_formula(self):
        yx_need_amount = (self.yx_value - self.current_amount) * 365 / self.yx_days
        return yx_need_amount

    def yx_need_days_formula(self):
        yx_need_days = (self.yx_value - self.current_amount) * 365 / self.current_balance
        return yx_need_days
