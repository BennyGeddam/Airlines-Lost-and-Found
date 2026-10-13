         ___        ______     ____ _                 _  ___
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/
 -----------------------------------------------------------------


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

for connecting to rds
    psql -h laf-database-1.czc4ii6q8cs9.us-east-1.rds.amazonaws.com -U geddam -d postgres -W


    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'geddam',
        'PASSWORD': '[REDACTED]',
        'HOST': 'laf-database-1.czc4ii6q8cs9.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
for rds table errors primary key related
python manage.py sqlflush

for ebs deploy
    pip3 install --upgrade --user awsebcli
    eb init -r us-east-1 -p python-3.9 Airlines_L_A_F
    eb create AIR-env --service-role LabRole --instance_profile LabInstanceProfile
    eb use AIR-env
    eb deploy alaf-env-clone
    eb status
    eb terminate venv
git add .ebextensions/
git commit -m "Elastic Beanstalk config files"

for s3
aws s3 mb s3://myairlaf
aws s3 cp /home/ec2-user/environment/Airlines_L_A_F/media/spot_items/images s3://myairlaf/media/spot_items/images/ --recursive
aws s3 ls s3://myairlaf/media/spot_items/images/ --recursive
cd spot_items/static/spot_items/
aws s3 cp master.css s3://myairlaf/spot_items/master.css


sns and sqs
aws sns create-topic --name item-r
aws sns subscribe --topic-arn arn:aws:sns:us-east-1:975049949964:item-r --protocol email --notification-endpoint x23328231@student.ncirl.ie
aws sqs create-queue --queue-name mysqs

 Git RE
git init
git add .gitignore

git clone https://github.com/Comrade-Glitch-cloud/Airlines-LAF.git
cd ALAF
git remote add origin https://github.com/Comrade-Glitch-cloud/Airlines-LAF.git

user name: Comrade-Glitch-cloud
[GitHub token removed for security]
