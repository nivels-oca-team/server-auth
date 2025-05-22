# Copyright 2023 Onestein (<https://www.onestein.eu>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.addons.base.tests.common import BaseCommon


class PasswordSecurityCommon(BaseCommon):
    def setUp(self):
        super().setUp()

        self.main_comp = self.env.ref("base.main_company")
        self.main_comp.password_expiration = 60
        self.main_comp.password_lower = 1
        self.main_comp.password_upper = 1
        self.main_comp.password_numeric = 1
        self.main_comp.password_special = 1
        self.main_comp.password_history = 30
        self.main_comp.password_minimum = 24
