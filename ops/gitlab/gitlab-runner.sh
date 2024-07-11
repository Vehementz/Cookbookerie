apt update
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash ### Download GitLab Runner Installer Script 
apt install gitlab-runner 
gitlab-runner -version
gitlab-runner status
gitlab-runner start
gitlab-runner enable  # Start on system boot by enabling the service.
