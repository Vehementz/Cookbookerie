apt update -y
apt upgrade -y
apt install curl -y
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash ### Download GitLab Runner Installer Script 
apt install gitlab-runner 
gitlab-runner -version
gitlab-runner status
gitlab-runner start
gitlab-runner enable  # Start on system boot by enabling the service.

# Once you have installed GitLab Runner, you need to register it with your Gitlab account. This links your runner with the projects on your Gitlab account and helps in the execution of CI/CD tasks.
# As a prerequisite, you need to have a GitLab account with a pre-existing project and a Project Runner in place.
gitlab-runner register token-number ## You'll need to copy the token-number from gitlab
