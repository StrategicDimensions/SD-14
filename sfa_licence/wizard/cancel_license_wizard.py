from odoo import models, fields, api, _


class CancelLicenseWizard(models.TransientModel):
    _name = 'cancel.license.wizard'
    _description = 'Cancel License Wizard'

    cancel_reason_id = fields.Many2one("license.cancel.reason", string="License Cancel Reason")
    application_reason_id = fields.Many2one("application.cancel.reason", string="Application Cancel Reason")
    license_id = fields.Many2one("license.license", string="License")
    application_id = fields.Many2one("license.application", string="Application")

    def cancel_license(self):
        if self.cancel_reason_id.id and self.license_id.id:
            self.license_id.write({
                'stage_id': self.license_id.stage_id.search([('name', '=', 'Cancelled')]).id,
                'cancel_reason': self.cancel_reason_id.name or '',
            })

    def cancel_application(self):
        if self.application_reason_id.id and self.application_id.id:
            self.application_id.write({
                'stage_id': self.application_id.stage_id.search([('name', '=', 'Cancelled')]).id,
                'cancel_reason': self.application_reason_id.name or '',
            })
