## 1. Launch VM Instance (GCP)
- Go to Google Cloud Console → Compute Engine → VM instances
- Click Create Instance

**Basic Configuration:**
- Name: (e.g., my-ubuntu-vm)
- Region / Zone: Choose nearest region (e.g., us-central1)
- Machine family: General-purpose
- Series: E2
- Machine type:
	- e2-micro (free tier eligible)
	- e2-small
	- e2-medium

**Boot Disk:** 
- Click Change
- Operating system: Ubuntu
- Version: Ubuntu 24.04 LTS
- Boot disk type: Balanced persistent disk
- Size: 10–20 GB (as needed)

**Networking:**
- Network: default
- External IPv4:
- Ephemeral (default)
- Reserve a Static IP (recommended)
→ VPC Network → IP addresses → Reserve Static External IP

**Firewall Rules (Allow):**
- ✔️ Allow HTTP traffic
- ✔️ Allow HTTPS traffic

(SSH is enabled by default)

## 2. Connect to VM
- Click SSH (Browser-based)
- Click Authorize

```
mrittunjoy_k_das@exam-hub-nacc:~$ cd ..
mrittunjoy_k_das@exam-hub-nacc:/home$ cd ubuntu/
mrittunjoy_k_das@exam-hub-nacc:/home/ubuntu$ pwd
/home/ubuntu
mrittunjoy_k_das@exam-hub-nacc:/home/ubuntu$ 
```


## 3. Update System + Install Core Packages
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git nginx python3-pip python3-venv build-essential curl
```


## 4. Install MySQL Server on EC2
```bash
sudo apt install -y mysql-server

sudo mysql_secure_installation
```
```text
Recommended answers:

	VALIDATE PASSWORD? → No
	Remove anonymous users? → Yes
	Disallow remote login? → Yes
	Remove test DB? → Yes
	Reload privileges? → Yes
```

## 5. Create MySQL Database + User
```bash
sudo mysql
```
For **simple-signup** Application:
```mysql
CREATE DATABASE register;
CREATE USER 'tester'@'localhost' IDENTIFIED BY 'Abc123456!';
GRANT ALL PRIVILEGES ON register.* TO 'tester'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## 6. Install Node.js (for React build)
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```


## 7. Clone Your GitHub Repo
```bash
sudo git clone https://github.com/mrittun/simple-signup.git
```

## 8. Backend Setup (Flask + Production Environment)
```bash	
sudo su -
cd /home/ubuntu/simple-signup/backend
sudo python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Create a **.env** file for production:
```bash
$ sudo apt install -y vim
```

(venv) root@simple-signup-1:/home/ubuntu/simple-signup/backend:
```bash
$vim .env
```
```text
FLASK_ENV=production
SECRET_KEY=mydeveloperkey
DATABASE_URL=mysql+pymysql://tester:Abc123456!@127.0.0.1/register
JWT_SECRET=mysignupkey
JWT_EXP_SECONDS=3600
```
	
## 9. Test backend With Gunicorn (before systemd)
```bash
pip install gunicorn
gunicorn --bind 127.0.0.1:5000 'app:create_app()'
```

For exit,press from keyboard : **ctrl + c**

## 10. Create a systemd Service for Gunicorn
```bash
sudo vim /etc/systemd/system/gunicorn.service
```
```text
[Unit]
Description=Gunicorn for Flask app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/simple-signup/backend
EnvironmentFile=/home/ubuntu/simple-signup/backend/.env
ExecStart=/home/ubuntu/simple-signup/backend/venv/bin/gunicorn --workers 4 --bind 127.0.0.1:5000 'app:create_app()'
Restart=always

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

## 11. Build the app:
```bash
cd /home/ubuntu/simple-signup/frontend
npm install
```	
create a .env file:
```bash	
vim .env
```
```text    
REACT_APP_BASE_URL=https://mrittunjoykumardas.online
```
```bash	
npm run build
```

## 12.Configure Nginx (Reverse Proxy + React Static)
```bash
sudo rm /etc/nginx/sites-enabled/default

sudo vim /etc/nginx/sites-available/simple-signup
```
```text
server {
		listen 80;
		server_name mrittunjoykumardas.online www.mrittunjoykumardas.online;  # or your domain

		root /home/ubuntu/simple-signup/frontend/build;
		index index.html;
		add_header Referrer-Policy "strict-origin-when-cross-origin" always;

		# Serve React
		location / {
				try_files $uri /index.html;
				}

		# API proxy to Flask-Gunicorn
		location /api/ {
					proxy_pass http://127.0.0.1:5000;
					proxy_set_header Host $host;
					proxy_set_header X-Real-IP $remote_addr;
					proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
					}

		client_max_body_size 50M;
}
```

```bash					
sudo ln -s /etc/nginx/sites-available/simple-signup /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 13. Add HTTPS (Recommended)

```bash
sudo snap install core
sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

Before running the following command, you should add 2 A records(@ & www) in your DNS using the AWS EC2's public IP(34.10.216.62):
I have used this "https://ap.www.namecheap.com/Domains/DomainControlPanel/mrittunjoykumardas.online/advancedns"

```bash
sudo certbot --nginx -d mrittunjoykumardas.online -d www.mrittunjoykumardas.online
```
  
## 14. Optional Firewall (UFW)
```bash
sudo apt install ufw -y
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```


## 15. Don't forget to do the following steps:
```bash
sudo chmod o+x /home/ubuntu
sudo chown -R ubuntu:www-data /home/ubuntu/simple-signup/frontend
sudo find /home/ubuntu/simple-signup/frontend -type d -exec chmod 755 {} \;
sudo find /home/ubuntu/simple-signup/frontend -type f -exec chmod 644 {} \;

sudo nginx -t
sudo systemctl restart nginx
sudo systemctl status nginx

curl -I https://mrittunjoykumardas.online/
```



🎉 Deployment Completed

The application is now fully deployed with:

- ✔ Flask backend on Gunicorn
- ✔ Nginx reverse proxy
- ✔ React build served statically
- ✔ MySQL installed + database imported
- ✔ HTTPS (if domain added)
- ✔ Auto-start services
- ✔ Proper security configuration

```bash
sudo certbot --nginx -d mrittunjoykumardas.online -d www.mrittunjoykumardas.online --dry-run
```

## 16.for simple-signup(ORM)

```bash
export FLASK_APP=app.py
flask db upgrade
```

Example:
```
(venv) root@simple-signup:/home/ubuntu/simple-signup# cd backend/
(venv) root@simple-signup:/home/ubuntu/simple-signup/backend# export FLASK_APP=app.py
(venv) root@simple-signup:/home/ubuntu/simple-signup/backend# flask db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 1258af2b4029, init
INFO  [alembic.runtime.migration] Running upgrade 1258af2b4029 -> 3210d5b223a5, Removed remarks field from the users table.
INFO  [alembic.runtime.migration] Running upgrade 3210d5b223a5 -> 603a64f60953, Added a new table 'marks'
(venv) root@simple-signup:/home/ubuntu/simple-signup/backend# 
```