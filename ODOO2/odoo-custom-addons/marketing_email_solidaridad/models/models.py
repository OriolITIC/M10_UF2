from odoo import models, fields, api




class Empresa(models.Model):
   _name = 'email.marketing.empresa'
   _description = 'Empresa para email marketing'




   name = fields.Char(string='Nombre', required=True)
   email = fields.Char(string='Correo Electrónico', required=True)
   description = fields.Text(string='Descripción')
   contact_type = fields.Selection([
       ('empresa', 'Empresa'),
       ('particular', 'Particular')
   ], string='Tipo de Contacto', default='empresa', required=True)




class EmailTemplate(models.Model):
   _name = 'email.marketing.template'
   _description = 'Plantilla de Correo Electrónico'




   name = fields.Char(string='Nombre', required=True)
   subject = fields.Char(string='Asunto', required=True)
   body_html = fields.Html(string='Cuerpo del Mensaje', required=True)




class EmailEnviado(models.Model):
   _name = 'email.marketing.enviado'
   _description = 'Correos electrónicos enviados'




   destinatarios_ids = fields.Many2many('email.marketing.empresa', string='Destinatarios', required=True)
   asunto = fields.Char(string='Asunto', required=True)
   mensaje = fields.Html(string='Mensaje', required=True)
   fecha_envio = fields.Datetime(string='Fecha de Envío', default=fields.Datetime.now)
   empresa_id = fields.Many2one('email.marketing.empresa', string='Empresa')
   template_id = fields.Many2one('email.marketing.template', string='Plantilla de Correo', ondelete='set null')
   destinatario_emails = fields.Char(string='Destinatarios Emails', compute='_compute_destinatario_emails')




   @api.depends('destinatarios_ids')
   def _compute_destinatario_emails(self):
       for record in self:
           record.destinatario_emails = ", ".join(dest.email for dest in record.destinatarios_ids)




   @api.onchange('template_id')
   def _onchange_template_id(self):
       if self.template_id:
           self.asunto = self.template_id.subject
           self.mensaje = self.template_id.body_html




   @api.model
   def create(self, vals):
       record = super(EmailEnviado, self).create(vals)
       self.env['email.marketing.statistics'].create({'email_id': record.id})
       return record




class EmailStatistics(models.Model):
   _name = 'email.marketing.statistics'
   _description = 'Estadísticas de Correos Electrónicos'




   email_id = fields.Many2one('email.marketing.enviado', string='Correo Enviado', required=True)
   email_asunto = fields.Char(string='Asunto del Correo', related='email_id.asunto', store=True)
   destinatario_emails = fields.Char(string='Destinatarios', related='email_id.destinatario_emails', store=True)
   open_rate = fields.Float(string='Tasa de Apertura', compute='_compute_open_rate')
   click_rate = fields.Float(string='Tasa de Clics', compute='_compute_click_rate')
   total_recipients = fields.Integer(string='Total de Destinatarios', compute='_compute_total_recipients', store=True)
   opens = fields.Integer(string='Aperturas')
   clicks = fields.Integer(string='Clics')




   @api.depends('opens', 'total_recipients')
   def _compute_open_rate(self):
       for record in self:
           if record.total_recipients > 0:
               record.open_rate = (record.opens / record.total_recipients) * 100
           else:
               record.open_rate = 0




   @api.depends('clicks', 'total_recipients')
   def _compute_click_rate(self):
       for record in self:
           if record.total_recipients > 0:
               record.click_rate = (record.clicks / record.total_recipients) * 100
           else:
               record.click_rate = 0




   @api.depends('email_id.destinatarios_ids')
   def _compute_total_recipients(self):
       for record in self:
           record.total_recipients = len(record.email_id.destinatarios_ids)




   def simulate_open(self):
       for record in self:
           record.opens += 1





   def simulate_click(self):
       for record in self:
           record.clicks += 1








class Donante(models.Model):
    _name = 'accounting.donante'
    _description = 'Registro de Donantes'

    name = fields.Char(string='Nombre del Donante', default='Anónimo')
    fecha_donacion = fields.Date(string='Fecha de la Donación', required=True, default=fields.Date.today)
    tipo_donacion = fields.Selection([
        ('dinero', 'Dinero'),
        ('ropa', 'Ropa'),
        ('comida', 'Comida'),
        ('otros', 'Otros')
    ], string='Tipo de Donación', required=True)
    cantidad_dinero = fields.Float(string='Cantidad de Dinero')
    descripcion_donacion = fields.Text(string='Descripción de la Donación')
    uso_especifico = fields.Char(string='Uso Específico')
