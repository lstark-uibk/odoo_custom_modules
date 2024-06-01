# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CustomPartner_inheritance(models.Model):
    # _name = "inheritance.test"
    _inherit = ["res.partner"]
    firstname = fields.Char(string="Vorname", required = True,tracking=True)
    surename = fields.Char(string="Nachname", required = True,tracking=True)
    # persontype = fields.Selection([
    #     ('private','Privatperson'),
    #     ('enterprise','Unternehmen')],
    #      default = 'private'
    # ,required = True,tracking=True)
    # email = fields.Char(string="Mail Adresse", required = True,tracking=True)
    # gibts schon 'is_company'
    customer_number = fields.Integer(string="Kundennummer", required = True,tracking=True)
    # ust_number = fields.Integer(string="USt. Nummer",tracking=True) gibts schon 'vat'
    #gibts schon 'street'
    street = fields.Char(string="Straße", required = True,tracking=True)
    housenumber = fields.Char(string="Hausnummer", required=True, tracking=True)
    top = fields.Char(string="Top",tracking=True)
    # postalcode = fields.Integer(string="Postleitzahl", required = True,tracking=True)
    # city = fields.Char(string="Ort/Stadt", required = True,tracking=True)
    bank_account_name = fields.Char(string="Name des Bankaccounts", required = True,tracking=True)
    iban = fields.Char(string="Postleitzahl", required = True,tracking=True)
    bic = fields.Char(string="BIC",tracking=True)
    meteringpoint = fields.Char(string="Zählpunktnummer",required = True,tracking=True)
    networkprovider = fields.Char(string="Netzbetreiber",required = True,tracking=True)
    metering_equal_adress = fields.Boolean(string='Zählpunkt gleich Hausnummer', default=True,required = True,tracking=True)
    meteringpoint_street = fields.Char(string="Zählpunkt Straße", required=True, tracking=True)
    meteringpoint_housenumber = fields.Char(string="Zählpunkt Hausnummer", required=True, tracking=True)
    meteringpoint_top = fields.Char(string="Zählpunkt Top",  tracking=True)
    meteringpoint_postalcode = fields.Char(string="Zählpunkt Postleitzahl", required=True, tracking=True)
    meteringpoint_city = fields.Char(string="Zählpunkt Ort/Stadt", required=True, tracking=True)
    annualconsumption = fields.Float(string="Jahresverbrauch geschätzt",tracking=True)
    consumption_type = fields.Selection([
        ('household','Haushalt'),
        ('enterprise','Gewerbe')],
         default = 'household'
    ,tracking=True)
    energysource = fields.Selection([
        ('pv','Photovoltaik'),
        ('wind','Windkraft'),
        ('water','Wasserkraft')],
         default = 'pv',
        string="Energiequelle"
    ,tracking=True)
    power = fields.Float(string="Leistung (kWp)",tracking=True)
    annual_yield = fields.Float(string="Jahresverzeugung geschätzt",tracking=True)
    yield_profile = fields.Selection([
        ('pv_south','PV Südseitig'),
        ('pv_e_w','PV Ost West')],
         default = 'pv_south'
    ,tracking=True)
    othercomments = fields.Char(string="Andere Anmerkungen", tracking=True)




    def action_send_mail(self):
        print("here")
        template_new_customer = self.env.ref("custom_inheritance.new_prod_kons_created")
        template_us = self.env.ref("custom_inheritance.new_prod_kons_created_for_us")
        print(template_new_customer)
        print(template_us)
        for rec in self:
            template_new_customer.send_mail(rec.id,force_send=True)
            template_us.send_mail(rec.id, force_send=True)
