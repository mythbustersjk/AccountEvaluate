"""
客户指标计算公式
"""


class Formula:
    """
    yx_value:基础户年日均门槛值，该值由setting.json设置。
    current_amount:账户现年日均值。使用yx_amount_formula和yx_need_days_formula方法时必须需提供该值。
    current_balance:账户现余额。使用yx_need_days_formula方法时必须提供该值。
    yx_days:客户资金预计留存天数。使用yx_amount_formula方法时必须提供该值。
    """

    def __init__(self, value, current_amount, current_balance=0, days=0):
        self.value = float(value)
        self.current_amount = float(current_amount)
        self.current_balance = float(current_balance)
        self.days = float(days)

    def need_amount_formula(self):
        yx_need_amount = (self.value - self.current_amount) * 365 / self.days
        return yx_need_amount

    def need_days_formula(self):
        yx_need_days = (self.value - self.current_amount) * 365 / self.current_balance
        return yx_need_days
