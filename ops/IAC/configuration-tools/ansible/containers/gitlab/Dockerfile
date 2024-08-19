# Use the official GitLab Community Edition image
FROM gitlab/gitlab-ce:latest

# Set environment variables to configure GitLab
ENV GITLAB_OMNIBUS_CONFIG="\
  external_url 'http://crazytechgeek.info';\
  letsencrypt['enable'] = true;\
  letsencrypt['contact_emails'] = ['admin@linuxtechi.com'];\
  letsencrypt['auto_renew'] = true;\
  letsencrypt['auto_renew_hour'] = 5;\
  letsencrypt['auto_renew_day_of_month'] = '*/6';\
"

# Expose web & ssh
EXPOSE 80 443 22

# When the container starts, reconfigure and restart GitLab
CMD (/opt/gitlab/bin/gitlab-ctl reconfigure && /opt/gitlab/bin/gitlab-ctl restart) && tail -f /dev/null
