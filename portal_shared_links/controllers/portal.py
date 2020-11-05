from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomerPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values ['shared_link_count'] = request.env['documents.share'].sudo().search_count([('partner_id','=',partner.id)])
        return values

    @http.route(['/my/links'], type='http', auth="user", website=True)
    def portal_shared_links(self):
        values = self._prepare_portal_layout_values()
        if values.get('shared_link_count',0):
            searchbar_sortings = {
                'date': {'label': _('Newest'), 'order': 'create_date desc'},
                'name': {'label': _('Name'), 'order': 'name'},
            }
            partner = request.env.user.partner_id
            links = request.env['documents.share'].sudo().search([('partner_id','=',partner.id)])
            values.update({
                'shared_links':links,
                'page_name':'shared_links',
                'searchbar_sortings':searchbar_sortings,
                'sortby':'date'
            })
        return request.render('portal_shared_links.layout_portal_shared_links',values)
