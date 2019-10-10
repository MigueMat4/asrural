from django.db import models
from django.contrib.auth.models import User

TIPO_VEHICULO=(
	(1, 'AUTOMOVIL'),
	(2, 'CAMIONETA'),
	(3, 'PICK UP'),
	(4, 'MINIVAN'),
)


class Empleado (models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nombre_Empleado = models.CharField(max_length=100)
	codigo_Empleado = models.IntegerField(default=0)
	iniciales = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre_Empleado

class Cliente (models.Model):
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
	nombre_Cliente = models.CharField(max_length=100)
	celular_Cliente = models.IntegerField(default=0)
	correo_Cliente = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre_Cliente


class Vehiculo (models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	marca = models.CharField(max_length=20)
	linea = models.CharField(max_length=50)
	tipo = models.PositiveSmallIntegerField(choices=TIPO_VEHICULO)
	asientos = models.IntegerField(default=0)
	valor = models.FloatField(default=0)

	def __str__(self):
		return self.marca

class Cotizacion (models.Model):
	vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, default=Vehiculo.objects.last())
	deducible = models.FloatField(default=0)
	deducible_robo = models.FloatField(default=0)
	lesiones = models.IntegerField(default=0)
	accidentes = models.IntegerField(default=0)
	anual_valor_Seguro = models.FloatField(default=0)
	semestral_valor_Seguro = models.FloatField(default=0)
	trimestral_valor_Seguro = models.FloatField(default=0)
	mensual_valor_Seguro = models.FloatField(default=0)

	def __str__(self):
		respuesta = 'Cotización para Vehiculo ' + self.vehiculo.marca
		return respuesta

	def lesiones_calculo(self):
		self.lesiones=self.vehiculo.asientos*20000
		return self.lesiones

	def accidentes_calculo(self):
		self.accidentes=self.vehiculo.asientos*20000
		return self.accidentes

	def save(self, *args, **kwargs):
		self.cotizar_vehiculo()
		super(Cotizacion, self).save(*args, **kwargs)

	def cotizar_vehiculo(self):
		self.lesiones_calculo()
		self.accidentes_calculo()
		if (self.vehiculo.tipo==1):
			self.deducible=self.vehiculo.valor*0.03
			if (self.deducible<2000):
				self.deducible=2000
			"""DEDUCIBLE ROBO"""
			self.deducible_robo=self.vehiculo.valor*0.03
			if (self.deducible_robo<2000):
				self.deducible_robo=2000
			self.anual_automovil()
			self.semestral_automovil()
			self.trimestral_automovil()
			self.mensual_automovil()

		if (self.vehiculo.tipo==2):
			"""DEDUCIBLE ACCIDENTES"""
			self.deducible=self.vehiculo.valor*0.03
			if (self.deducible<2000):
				self.deducible=2000
			"""DEDUCIBLE ROBO"""
			self.deducible_robo=	self.vehiculo.valor*0.10
			if (self.deducible_robo<2000):
				self.deducible_robo=2000
			self.anual_camioneta()
			self.semestral_camioneta()
			self.trimestral_camioneta()
			self.mensual_camioneta()

		if (self.vehiculo.tipo==3):
			"""DEDUCIBLE ACCIDENTES"""
			self.deducible=self.vehiculo.valor*0.03
			if (self.deducible<2000):
				self.deducible=2000
			"""DEDUCIBLE ROBO"""
			self.deducible_robo=	self.vehiculo.valor*0.15
			if (self.deducible_robo<2000):
				self.deducible_robo=2000
			self.anual_pickup()
			self.semestral_pickup()
			self.trimestral_pickup()
			self.mensual_pickup()

		if (self.vehiculo.tipo==4):
			"""DEDUCIBLE ACCIDENTES"""
			self.deducible=self.vehiculo.valor*0.03
			if (self.deducible<2000):
				self.deducible=2000
			"""DEDUCIBLE ROBO"""
			self.deducible_robo=	self.vehiculo.valor*0.03
			if (self.deducible_robo<2000):
				self.deducible_robo=2000
			self.anual_mini()
			self.semestral_mini()
			self.trimestral_mini()
			self.mensual_mini()

	def anual_automovil(self):
		if (self.vehiculo.valor<=30000):
			self.anual_valor_Seguro=(1600+(1600*.05))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0491)*1.05)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0451)*1.05)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0421)*1.05)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.04)*1.05)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0382)*1.05)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0369)*1.05)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.035)*1.05)*1.12
		self.anual_valor_Seguro = round(self.anual_valor_Seguro, 2)
		return round(self.anual_valor_Seguro, 2)

	def semestral_automovil(self):

		if (self.vehiculo.valor<=30000):
			self.semestral_valor_Seguro=(1600+(1600*.05)+(1600*.065))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0491)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0451)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0421)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.04)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0382)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0369)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.035)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		self.semestral_valor_Seguro = round(self.semestral_valor_Seguro, 2)
		return self.semestral_valor_Seguro

	def trimestral_automovil(self):

		if (self.vehiculo.valor<=30000):
			self.trimestral_valor_Seguro=(1600+(1600*.05)+(1600*.095))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0491)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0451)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0421)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.04)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0382)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0369)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.035)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		self.trimestral_valor_Seguro = round(self.trimestral_valor_Seguro, 2)
		return self.trimestral_valor_Seguro

	def mensual_automovil(self):

		if (self.vehiculo.valor<=30000):
			self.mensual_valor_Seguro=(1600+(1600*.05)+(1600*.1347))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0491)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0451)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0421)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.04)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0382)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0369)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.035)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		self.mensual_valor_Seguro = round(self.mensual_valor_Seguro, 2)
		return self.mensual_valor_Seguro



	def anual_camioneta(self):
		
		if (self.vehiculo.valor<=30000):
			self.anual_valor_Seguro=(1600+(1600*.05))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0491)*1.05)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0451)*1.05)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0421)*1.05)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.04)*1.05)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0382)*1.05)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0369)*1.05)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.035)*1.05)*1.12
		return self.anual_valor_Seguro

	def semestral_camioneta(self):

		if (self.vehiculo.valor<=30000):
			self.semestral_valor_Seguro=(1600+(1600*.05)+(1600*.065))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0491)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0451)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0421)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.04)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0382)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0369)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.035)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		return self.semestral_valor_Seguro

	def trimestral_camioneta(self):

		if (self.vehiculo.valor<=30000):
			self.trimestral_valor_Seguro=(1600+(1600*.05)+(1600*.095))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0491)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0451)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0421)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.04)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0382)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.0369)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.035)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		return self.trimestral_valor_Seguro

	def mensual_camioneta(self):

		if (self.vehiculo.valor<=30000):
			self.mensual_valor_Seguro=(1600+(1600*.05)+(1600*.1347))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0491)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=60000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0451)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>60000 and self.vehiculo.valor<=70000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0421)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.04)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0382)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.0369)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.035)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		return self.mensual_valor_Seguro


	
	def anual_pickup(self):
		
		if (self.vehiculo.valor<=30000):
			self.anual_valor_Seguro=(1700+(1700*.05))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.055)*1.05)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=70000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.052)*1.05)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.051)*1.05)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.05)*1.05)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.048)*1.05)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.045)*1.05)*1.12
		return self.anual_valor_Seguro

	def semestral_pickup(self):

		if (self.vehiculo.valor<=30000):
			self.semestral_valor_Seguro=(1700+(1700*.05)+(1700*.065))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.055)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=70000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.052)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.051)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.05)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.048)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.045)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		return self.semestral_valor_Seguro

	def trimestral_pickup(self):

		if (self.vehiculo.valor<=30000):
			self.trimestral_valor_Seguro=(1700+(1700*.05)+(1700*.095))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.055)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=70000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.052)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.051)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.05)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.048)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.trimestral_valor_Seguro=(((self.vehiculo.valor*0.045)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		return self.trimestral_valor_Seguro

	def mensual_pickup(self):

		if (self.vehiculo.valor<=30000):
			self.mensual_valor_Seguro=(1700+(1700*.05)+(1700*.1347))*1.12
		if (self.vehiculo.valor>30000 and self.vehiculo.valor<=38000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.055)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>38000 and self.vehiculo.valor<=70000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.052)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=80000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.51)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>80000 and self.vehiculo.valor<=90000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.05)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>90000 and self.vehiculo.valor<=100000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.048)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>100000 and self.vehiculo.valor<=250000):
			self.mensual_valor_Seguro=(((self.vehiculo.valor*0.045)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		return self.mensual_valor_Seguro	



	def anual_mini(self):
		
		if (self.vehiculo.valor<=44444.44):
			self.anual_valor_Seguro=(2000+(2000*.05))*1.12
		if (self.vehiculo.valor>44444.44 and self.vehiculo.valor<=70000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.045)*1.05)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=250000):
			self.anual_valor_Seguro=((self.vehiculo.valor*0.0425)*1.05)*1.12
		return self.anual_valor_Seguro
		
	def semestral_mini(self):

		if (self.vehiculo.valor<=44444.44):
			self.semestral_valor_Seguro=(2000+(2000*.05)+(2000*.065))*1.12
		if (self.vehiculo.valor>44444.44 and self.vehiculo.valor<=70000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.045)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=250000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0425)*1.05)+(self.vehiculo.valor*.035)*.065)*1.12
		return self.semestral_valor_Seguro

	def trimestral_mini(self):

		if (self.vehiculo.valor<=44444.44):
			self.trimestral_valor_Seguro=(2000+(2000*.05)+(2000*.095))*1.12
		if (self.vehiculo.valor>44444.44 and self.vehiculo.valor<=70000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.045)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=250000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0425)*1.05)+(self.vehiculo.valor*.035)*.095)*1.12
		return self.trimestral_valor_Seguro

	def mensual_mini(self):

		if (self.vehiculo.valor<=44444.44):
			self.mensual_valor_Seguro=(2000+(2000*.05)+(2000*.1347))*1.12
		if (self.vehiculo.valor>44444.44 and self.vehiculo.valor<=70000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.045)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		if (self.vehiculo.valor>70000 and self.vehiculo.valor<=250000):
			self.semestral_valor_Seguro=(((self.vehiculo.valor*0.0425)*1.05)+(self.vehiculo.valor*.035)*.1347)*1.12
		return self.mensual_valor_Seguro	