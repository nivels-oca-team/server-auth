# Copyright 2016 LasLabs Inc.
# Copyright 2017 Kaushal Prajapati <kbprajapati@live.com>.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models
from odoo.tools import config
from odoo.modules import module


class ResCompany(models.Model):
    _inherit = "res.company"

    def _default_company_password_security_setting(self, value):
        ''' Disable password checking when tests are running '''
        if config['test_enable'] or config['test_file'] or module.current_test:
            return 0
        return value

    password_expiration = fields.Integer(
        "Days",
        default=lambda self: self._default_company_password_security_setting(60),
        help="How many days until passwords expire",
    )
    password_lower = fields.Integer(
        "Lowercase",
        default=lambda self: self._default_company_password_security_setting(1),
        help="Require number of lowercase letters",
    )
    password_upper = fields.Integer(
        "Uppercase",
        default=lambda self: self._default_company_password_security_setting(1),
        help="Require number of uppercase letters",
    )
    password_numeric = fields.Integer(
        "Numeric",
        default=lambda self: self._default_company_password_security_setting(1),
        help="Require number of numeric digits",
    )
    password_special = fields.Integer(
        "Special",
        default=lambda self: self._default_company_password_security_setting(1),
        help="Require number of unique special characters",
    )
    password_history = fields.Integer(
        "History",
        default=lambda self: self._default_company_password_security_setting(30),
        help="Disallow reuse of this many previous passwords - use negative "
        "number for infinite, or 0 to disable",
    )
    password_minimum = fields.Integer(
        "Minimum Hours",
        default=lambda self: self._default_company_password_security_setting(24),
        help="Amount of hours until a user may change password again",
    )
