from odoo import fields, models, api, _


class Application(models.Model):
    _name = 'license.application'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Applications'
    _order = 'stage_id'

    def _read_group_stage_ids(self, stages, domain, order):
        return self.env['license.application.stage'].search([])

    def _get_default_stage_id(self):
        return self.env['license.application.stage'].search([],order='sequence',limit=1).id

    name = fields.Char('Name')
    stage_id = fields.Many2one('license.application.stage', 'Application Stage', group_expand='_read_group_stage_ids', default=_get_default_stage_id, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    cancel_reason = fields.Char(string="Cancel Reason", )
    partner_id = fields.Many2one('res.partner', 'Applicant')

    def cancel_application(self):
        ctx = self._context.copy()
        ctx.update({'for_application': False,'default_application_id': self.id})
        return {
            'name': _('Cancel Appplication'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'cancel.license.wizard',
            'res_id':False,
            'view_id': self.env.ref('sfa_licence.cancel_license_wizard_view').id,
            'target': 'new',
            'context': ctx,
        }


class LicenseStages(models.Model):
    _name = 'license.stage'
    _description = "Licence Stages"
    _order = 'sequence'
    _fold_name = 'folded_in_kanban'

    name = fields.Char(string='Name')
    sequence = fields.Integer(string='Sequence')
    folded_in_kanban = fields.Boolean(string="Folded in Kanban")
    active = fields.Boolean('Active', default=True, tracking=True)


class ApplicationStages(models.Model):
    _name = 'license.application.stage'
    _description = "Application Stages"
    _order = 'sequence'
    _fold_name = 'folded_in_kanban'

    name = fields.Char(string='Name')
    sequence = fields.Integer(string='Sequence')
    folded_in_kanban = fields.Boolean(string="Folded in Kanban")
    active = fields.Boolean('Active', default=True, tracking=True)

class Licence(models.Model):
    _name = 'license.license'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = "Licences"
    _order = 'stage_id'

    def _read_group_stage_ids(self, stages, domain, order):
        return self.env['license.stage'].search([])

    def _get_default_stage_id(self):
        return self.env['license.stage'].search([],order='sequence',limit=1).id

    name = fields.Char('Name')
    license_status = fields.Selection([('Not Available', 'Unavailable'), ('available', 'Available'),('Reserved', 'Reserved'),('issued', 'Active')],string="Status")
    stage_id = fields.Many2one('license.stage', 'License Stage', group_expand='_read_group_stage_ids', default=_get_default_stage_id, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    cancel_reason = fields.Char(string="Cancel Reason", )
    partner_id = fields.Many2one('res.partner', 'Licence Holder')

    def cancel_license(self):
        ctx = self._context.copy()
        ctx.update({'default_license_id': self.id,'for_license': True})
        return {
            'name': _('Cancel Appplication'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'cancel.license.wizard',
            'res_id':False,
            'view_id': self.env.ref('sfa_licence.cancel_license_wizard_view').id,
            'target': 'new',
            'context': ctx,
        }

class LicenceSite(models.Model):
    _name = 'license.site'
    _description = "Sites"

    name = fields.Char(string='Name')
    active = fields.Boolean('Active', default=True, tracking=True)

class LicenceType(models.Model):
    _name = 'license.type'
    _description = "Licence Types"

    name = fields.Char(string='Name')
    active = fields.Boolean('Active', default=True, tracking=True)

class LicenceSpeciesGroup(models.Model):
    _name = 'license.species.group'
    _description = "Species Group"

    name = fields.Char(string='Name')
    active = fields.Boolean('Active', default=True, tracking=True)


class CancelReason(models.Model):
    _name = 'license.cancel.reason'
    _description = "License Cancel Reason"

    name = fields.Char(string="Reason", )

class CancelReason(models.Model):
    _name = 'application.cancel.reason'
    _description = "Application Cancel Reason"

    name = fields.Char(string="Reason", )
