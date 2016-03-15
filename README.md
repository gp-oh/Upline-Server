# Upline-Server
Admin and API for Upline App

API
http://docs.uplinevirtual.apiary.io/#

REPLICAÇÃO DE AMBIENTE - PASSOS
	- Criar novo DB RDS AWS
		- Replicar as tabelas
			http://quick.as/lbgwh6bmx
			http://quick.as/7gq8s4j19 
			- Limpar as tabelas (Executar script)
	
	- Criar novo branche
		- Customizar Front-End
		- Customizar template de E-mail
	
	- Criar nova aplicação no Heroku
		https://dashboard.heroku.com/apps
			- Configurar Deploy via Github
			- Ativar Plugin Mailgun
				- Criar e-mail do cliente
					Mailgun> Domains > Manage SMTP credentials > New SMTP credential
	
	- Ajustar configurações 
		- settings.py
			- Alterar endereço do DB (DATABASES)
			- Alterar S3 AWS (AWS_STORAGE_BUCKET_NAME)
			- Alterar dados e-mail
		- worker.py
			- Alterar Redis (REDISTOGO_URL)
				Heroku > Apps > Settings > Config Variables
