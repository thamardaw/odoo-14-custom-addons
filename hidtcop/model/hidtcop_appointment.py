from odoo import fields, models

class hidtcop_appointment(models.Model):
	_name = "hidtcop.appointment"

	name = fields.Char(string="Name" ,copy=True)
	patient_name= fields.Char()
	doctor_name= fields.Char()
	# patient_id = fields.Many2one('hidtcop.patient','Patient',required=True)
	# doctor_id = fields.Many2one('hidtcop.doctor','Doctor',required=True)
	patient_status = fields.Selection([
			('ambulatory', 'Ambulatory'),
			('outpatient', 'Outpatient'),
			('inpatient', 'Inpatient'),
		], 'Patient status', sort=False,default='outpatient')

	urgency_level = fields.Selection([
			('a', 'Normal'),
			('b', 'Urgent'),
			('c', 'Medical Emergency'),
		], 'Urgency Level', sort=False,default="b")
	appointment_date = fields.Datetime('Appointment Date',required=True,default = fields.Datetime.now)
	appointment_end = fields.Datetime('Appointment End',required=True)
