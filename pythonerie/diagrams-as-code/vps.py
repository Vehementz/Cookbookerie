from diagrams import Cluster, Diagram
from diagrams.aws.network import Route53
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.devtools import Codebuild
from diagrams.aws.devtools import Codepipeline
from diagrams.aws.storage import S3
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.onprem.client import User
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Caddy

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL 
from diagrams.onprem.monitoring import Grafana, Prometheus

from diagrams.onprem.compute import Server 
from diagrams.generic.compute import Rack

# diagrams.onprem.client.Client ## Laptop screen

with Diagram("CI/CD Pipeline Architecture", show=False):
    client = User("Developper")

    with Cluster("Staging Environment"):
        staging_server = EC2("Staging Server")
        dockerhub = Docker("Docker Hub")
        github = Github("GitHub")
        caddy = Caddy("Caddy")
        web_service = Jenkins("WebHook Service")
        db_staging = RDS("PostgreSQL Staging")

        github >> Codepipeline("Deploy Pipeline") >> Codebuild("Test -> Build & Push") >> dockerhub
        dockerhub >> caddy
        caddy >> web_service
        web_service >> db_staging

    with Cluster("Virtual Private Server"):
        server = Server("VPS")
        staging_server = EC2("Staging Server")
        production_server = EC2("Production Server")

        caddy >> server

    with Cluster("Production Environment"):
        production_server = EC2("Production Server")
        docker_production = Docker("Docker Production")
        db_production = RDS("PostgreSQL Production")
        dockerhub >> docker_production >> production_server
        production_server >> caddy
        caddy >> db_production

    client  >> github
