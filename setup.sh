# Setup Google Cloud Project for hosting the discord bot
# Current plan is to use Cloud Run 

gcloud services enable secretmanager.googleapis.com
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT --member=user:$(gcloud auth list --format 'value(account)') --role=roles/secretmanager.admin

echo -n $BOT_TOKEN | gcloud secrets create bot-token --replication-policy=automatic --data-file=-