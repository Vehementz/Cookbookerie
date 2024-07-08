graph TB
    Client -->|Request| DNS[DNS (51.68.58.70)]
    DNS -->|Redirects to| VPS_Server[VPS Server (51.68.58.70)]

    subgraph GitHub ["GitHub Workflow"]
        Dev[Developer] -->|Push updates| GH[GitHub]
        GH -->|Trigger CI/CD| Docker_Staging[Docker Staging [Docker Hub]]
        Docker_Staging -->|Notify staging deployment| Webhook_Service[Webhook Service]
    end

    Webhook_Service -->|Deploy to staging| VPS_Server

    subgraph VPS_Staging["Staging Environment"]
        VPS_Server --> Caddy[Caddy Server]
        Caddy --> React_Staging[React App [Staging]]
        Caddy --> API_Staging[API [Staging]]
        React_Staging -->|Interacts with| API_Staging
        API_Staging -->|Uses DB| Postgres_Staging[Postgres [Staging]]
    end

    subgraph VPS_Production["Production Environment"]
        Docker_Staging -->|Deploy to production| Docker_Production[Docker Production]
        Docker_Production -->|Deploy to production| VPS_Server
        VPS_Server --> Caddy
        Caddy --> React_Prod[React App [Production]]
        Caddy --> API_Prod[API [Production]]
        React_Prod -->|Interacts with| API_Prod
        API_Prod -->|Uses DB| Postgres_Prod[Postgres [Production]]
    end

    style DNS fill:#f9e0ae,stroke:#333,stroke-width:2px
    style Client fill:#f4cccc,stroke:#333,stroke-width:2px
    style VPS_Server fill:#d9ead3,stroke:#333,stroke-width:2px
    style Webhook_Service fill:#cfe2f3,stroke:#333,stroke-width:2px
    style Caddy fill:#fff2cc,stroke:#333,stroke-width:2px
    style React_Staging fill:#d5a6bd,stroke:#333,stroke-width:2px
    style API_Staging fill:#b6d7a8,stroke:#333,stroke-width:2px
    style Postgres_Staging fill:#c9daf8,stroke:#333,stroke-width:2px
    style React_Prod fill:#d5a6bd,stroke:#333,stroke-width:2px
    style API_Prod fill:#b6d7a8,stroke:#333,stroke-width:2px
    style Postgres_Prod fill:#c9daf8,stroke:#333,stroke-width:2px
    style Docker_Staging fill:#b4a7d6,stroke:#333,stroke-width:2px
    style Docker_Production fill:#b4a7d6,stroke:#333,stroke-width:2px
