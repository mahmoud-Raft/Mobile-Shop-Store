# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MobileShopStore(models.Model):
    _name = 'mobileshop.mobile'
    _description = 'Mobile Iformation'

    name = fields.Char(string="Name")
    image = fields.Binary("Image")
    company_id = fields.Many2one("mobileshop.company", "Company", ondelete="cascade")
    processor = fields.Char(string="Processor")
    ram_storage = fields.Char(sting="Ram / Storage")
    camera = fields.Char(string="Camera")
    screensize = fields.Char(string="Screen Size")
    oper_system = fields.Char(string="Operating System")
    battery_size = fields.Integer(string="Battery Size")
    color = fields.Selection([('1est', 'White'), ('2end', 'Black'),
                              ('3rd', 'Orange'), ('4th', 'Red'),
                              ('5th', 'Grey'), ('6th', 'Brown'),
                              ('7th', 'Red'), ('8th', 'Green'),
                              ('9th', 'Selver'), ('10th', 'Purple'),
                              ('11th', 'Blue'), ('12th', 'Yellow')
                              ], "Color", Default="1est")
    numberinstore = fields.Integer(string="Number In store")
    simcard = fields.Selection([('1simcard','1 Sim Card'),
                                         ('2simcard', '2 Sim Card')], "Sim Card", default="2simcard")
    externalmomerycard = fields.Selection([('nomemcard','No Momery Card'),
                                           ('1memplace2simcard', 'Momery Card Instead of second sim'),
                                           ('1memcard', 'Momery Card'),

                                           ],"External Momery Card", default="1memcard")
    price = fields.Float(string="Price")
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    advantages_ids = fields.Many2many('mobileshop.advantage', 'mobile_advantage_rel', "mobile_id", "advantage_id", "Advantages Information")
    invoice_ids = fields.One2many('mobileshop.invoice', 'mobile_id', 'Invoice')


class MobileAdvantages(models.Model):
    _name = 'mobileshop.advantage'
    _description = 'Advantages'

    name = fields.Char(string='name')
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    mobiles_ids = fields.Many2many('mobileshop.mobile', 'mobile_advantage_rel', "advantage_id", "mobile_id", "Mobiles Information", readonly=True)






class MobileScreens(models.Model):
    _name = 'mobileshop.screen'
    _description = 'Screen'

    name = fields.Char(string="name")
    image = fields.Binary("Image")
    screentype = fields.Selection([('1est', 'Plastic Screen'), ('2end', 'Normal Glass Screen'),
                                   ('3rd', 'Glass Screen Curved limbs'), ('4th', 'Screen Curved limbs 5D'),
                                   ('5th', 'Gelatin Screen'), ('6th', 'Nano Screen'),
                                   ('7th', 'laser Screen'), ('8th', 'Ceramic Screen')
                                   ], "Screen Type", Default="1est")
    price = fields.Float(string="Price")
    numberinstore = fields.Integer(string="Number In store")
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    mobile_id = fields.Many2one("mobileshop.mobile", "Mobile")


class UsbCoversandOthers(models.Model):
    _name = 'mobileshop.usbcovers'
    _description = 'UsbCovers'

    name = fields.Char(string="name")
    image = fields.Binary("Image")
    usborcovertype = fields.Selection([('1est', 'UsbType Micro'), ('2end', 'UsbType C'),
                                       ('3rd', 'Product for All'), ('4th', 'Covers form Male'),
                                       ('5th', 'Covers for Female')
                                       ], "Product Type", Default="1est")
    color = fields.Selection([('1est', 'White'), ('2end', 'Black'),
                              ('3rd', 'Orange'), ('4th', 'Red'),
                              ('5th', 'White with Black lines'), ('6th', 'Brown'),
                              ('7th', 'Red'), ('8th', 'Green'),
                              ('9th', 'Selver'), ('10th', 'Purple'),
                              ('11th', 'Blue'), ('12th', 'Yellow')
                              ], "Color", Default="1est")
    price = fields.Float(string="Price")
    numberinstore = fields.Integer(string="Number In store")
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    productmobile_id = fields.Many2one("mobileshop.mobile", "Mobile")


class MobileproductsCompany(models.Model):
    _name = 'mobileshop.company'
    _description = 'Company'

    name = fields.Char(string='name')
    image = fields.Binary("Image")
    companycountry = fields.Char(string='Company Country')
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    mobile_ids = fields.One2many("mobileshop.mobile", "company_id", "Mobile")
    adapter_ids = fields.One2many("mobileshop.adapter", "company_id", "Adapter")
    headphone_ids = fields.One2many("mobileshop.headphone", "company_id", "HeadPhone")


class MobileAdapters(models.Model):
    _name = 'mobileshop.adapter'
    _description = 'Adapters'

    name = fields.Char(string='name')
    image = fields.Binary("Image")
    adapertype = fields.Selection([('1est', 'UsbType Micro'), ('2end', 'UsbType C'),
                                       ('3rd', 'Another type')
                                       ], "Adapter Type", Default="1est")
    color = fields.Selection([('1est', 'White'), ('2end', 'Black'),
                              ('3rd', 'Orange'), ('4th', 'Red'),
                              ('5th', 'White with Black lines'), ('6th', 'Brown'),
                              ('7th', 'Red'), ('8th', 'Green'),
                              ('9th', 'Selver'), ('10th', 'Purple'),
                              ('11th', 'Blue'), ('12th', 'Yellow')
                              ], "Color", Default="1est")
    adapterspeed = fields.Selection([('1est', 'Normal Speed'), ('2end', 'High speed charge')
                                       ], "Adapter speed", Default="1est")
    price = fields.Float(string="Price")
    numberinstore = fields.Integer(string="Number In store")
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    company_id = fields.Many2one('mobileshop.company', "Company")

class MobileHeadphones(models.Model):
    _name = 'mobileshop.headphone'
    _description = 'HeadPhone'

    name = fields.Char(string='name')
    image = fields.Binary("Image")
    color = fields.Selection([('1est', 'White'), ('2end', 'Black'),
                              ('3rd', 'Orange'), ('4th', 'Red'),
                              ('5th', 'White with Black lines'), ('6th', 'Brown'),
                              ('7th', 'Red'), ('8th', 'Green'),
                              ('9th', 'Selver'), ('10th', 'Purple'),
                              ('11th', 'Blue'), ('12th', 'Yellow')
                              ], "Color", Default="1est")
    price = fields.Float(string="Price")
    numberinstore = fields.Integer(string="Number In store")
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    company_id = fields.Many2one('mobileshop.company', "Company")

class MobileInvoices(models.Model):
    _name = 'mobileshop.invoice'
    _description = 'Invoices'

    name = fields.Char(string="Name", required='True')
    customername = fields.Char(string="Customer Name", required="True")
    customermobile = fields.Char(string="Customer mobile number", required="True")
    invoicedate= fields.Date(string="Invoice Date", default=fields.Date.today)
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True, default=lambda self: self.env.user)

    mobile_id = fields.Many2one('mobileshop.mobile', 'Mobile')
    mobileprice = fields.Float(string='Mobile Price')
    mobilequantity = fields.Integer(string="Quantity", default=1)
    mobiletax = fields.Float(string='Tax')
    mobiletotalprice = fields.Float(string='Mobile Total price')

    adapter_id = fields.Many2one('mobileshop.adapter', 'Adapter')
    adapterprice = fields.Float(string='Adapter Price')
    adapterquantity = fields.Integer(string="Quantity", default=1)
    adaptertotalprice = fields.Float(string='Adapter Total price')

    headphone_id = fields.Many2one('mobileshop.headphone', 'Headphone')
    headphoneprice = fields.Float(string='Headphone Price')
    headphonequantity = fields.Integer(string="Quantity", default=1)
    headphonetotalprice = fields.Float(string='Headphone Total price')

    usbcovers_id = fields.Many2one('mobileshop.usbcovers', 'UsbCovers')
    usbcoversprice = fields.Float(string='UsbCovers Price')
    usbcoversquantity = fields.Integer(string="Quantity", default=1)
    usbcoverstotalprice = fields.Float(string='UsbCovers Total price')

    screen_id = fields.Many2one('mobileshop.screen', 'Screen')
    screenprice = fields.Float(string='Screen Price')
    screenquantity = fields.Integer(string="Quantity", default=1)
    screentotalprice = fields.Float(string='Screen Total price')


    totalprice = fields.Float(string="Total Price: ")


    @api.onchange('mobile_id')
    def onchange_mobile(self):
        self.mobileprice = self.mobile_id.price

    @api.onchange('mobileprice')
    def onchange_mobileprice(self):
        if self.mobileprice > 3000.00:
            self.mobiletax = 0.001 * self.mobileprice
        else:
            self.mobiletax = 0.002 * self.mobileprice

    @api.onchange('mobile_id', 'mobileprice', 'mobilequantity', 'mobiletax')
    def _compute_totalmobileprice(self):
        self.mobiletotalprice = (self.mobileprice + self.mobiletax) * self.mobilequantity

    @api.onchange('adapter_id')
    def onchange_adapter(self):
        self.adapterprice = self.adapter_id.price

    @api.onchange('adapter_id', 'adapterprice', 'adapterquantity')
    def _compute_totaladapterprice(self):
        self.adaptertotalprice = self.adapterprice * self.adapterquantity

    @api.onchange('headphone_id')
    def onchange_headphone(self):
        self.headphoneprice = self.headphone_id.price

    @api.onchange('headphone_id', 'headphoneprice', 'headphonequantity')
    def _compute_totalheadphoneprice(self):
        self.headphonetotalprice = self.headphoneprice * self.headphonequantity

    @api.onchange('usbcovers_id')
    def onchange_usbcovers(self):
        self.usbcoversprice = self.usbcovers_id.price

    @api.onchange('usbcovers_id', 'usbcoversprice', 'usbcoversquantity')
    def _compute_totalusbcoversprice(self):
        self.usbcoverstotalprice = self.usbcoversprice * self.usbcoversquantity

    @api.onchange('screen_id')
    def onchange_screen(self):
        self.screenprice = self.screen_id.price

    @api.onchange('screen_id', 'screenprice', 'screenquantity')
    def _compute_totalscreenprice(self):
        self.screentotalprice = self.screenprice * self.screenquantity

    @api.onchange('mobiletotalprice', 'adaptertotalprice', 'usbcoverstotalprice', 'screentotalprice', 'headphonetotalprice')
    def _compute_totalinvoiceprice(self):
        self.totalprice = self.mobiletotalprice + self.adaptertotalprice + self.usbcoverstotalprice + self.screentotalprice + self.headphonetotalprice


# class mobileshop(models.Model):
#     _name = 'mobileshop.mobileshop'
#     _description = 'mobileshop.mobileshop'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
