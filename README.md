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

	- Criar novo S3
		https://www.dropbox.com/s/dtd1v37bkvgfla1/quickcast-15-03-2016-01-19-19.mp4?dl=0
		- Configurar S3
		http://quick.as/g1gpizqlg

	- Criar novo branche
		- Customizar Front-End
		- Customizar template de E-mail

	- Criar nova aplicação no Heroku
		https://dashboard.heroku.com/apps
			- Configurar Deploy via Github
			- Instalar Plugin Mailgun - Starter Free
				- Criar e-mail do cliente
					Mailgun> Domains > Manage SMTP credentials > New SMTP credential
			- Instalar Plugin Logentries - TryIt Free
			- Instalar Plugin Redis To Go - Nano Free
			- Instalar Plugin Heroku Scheduler
				- Configurar igual do Upline Virtual

			- Instalar Conversor de Mídia ( Deve ter o Heroku CLI intalado na máquina)
				heroku buildpacks:set https://github.com/ddollar/heroku-buildpack-multi.git  --app nome-da-app (Exemplo: upline-lattitude)

	- Gerar chave Push Google (PUSH_NOTIFICATIONS_SETTINGS)

	- Ajustar configurações
		- settings.py
			- Alterar endereço do DB (DATABASES)
			- Alterar S3 AWS (AWS_STORAGE_BUCKET_NAME)
			- Alterar dados e-mail
		- worker.py
			- Alterar Redis (REDISTOGO_URL)
				Heroku > Apps > Settings > Config Variables
