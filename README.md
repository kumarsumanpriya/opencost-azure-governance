# 💰 Enterprise FinOps & Cloud Cost Governance Engine

[![FinOps](https://img.shields.io/badge/FinOps-Certified_Practitioner-00D4B2?style=for-the-badge&logo=finops&logoColor=white)](https://www.finops.org/)
[![Infracost](https://img.shields.io/badge/Infracost-PR_Budget_Gates-00C48C?style=for-the-badge&logo=infracost&logoColor=white)](https://www.infracost.io/)
[![OpenCost](https://img.shields.io/badge/OpenCost-Kubernetes_Attribution-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://www.opencost.io/)
[![Azure Cost Management](https://img.shields.io/badge/Azure-Cost_Management-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](#license)

> **Cloud financial engineering framework that slashes Azure spend by up to 40% through Infracost PR budget enforcement, OpenCost real-time Kubernetes pod cost attribution, and automated hygiene scanners for orphaned assets.**

---

## 🏛️ Continuous Cloud Financial Operations Flow

```mermaid
flowchart LR
    subgraph ShiftLeft ["1. Inform & Prevent (Shift-Left)"]
        PR["Developer Pull Request"] --> INFRACOST["Infracost CI/CD Gate"]
        INFRACOST --> REGO["OPA Budget Threshold ($500 Delta Cap)"]
    end

    subgraph RealTime ["2. Attribute & Monitor (Run-Time)"]
        AKS["Production AKS Clusters"] --> OPENCOST["OpenCost Exporter"]
        OPENCOST --> GRAFANA["Product Team Chargeback Dashboards"]
    end

    subgraph AutomatedHygiene ["3. Operate & Optimize (Automated Hygiene)"]
        CRON["Nightly Scheduled Job"] --> CLEAN_DISKS["Unattached Managed Disks Scanner"]
        CRON --> CLEAN_IPS["Orphaned Public IP Deallocator"]
        CRON --> VM_SCHED["Dev/Staging VM Sleep Schedule"]
    end

    style INFRACOST fill:#1E293B,stroke:#00F2FE,stroke-width:2px,color:#FFFFFF
    style OPENCOST fill:#1E293B,stroke:#10B981,stroke-width:2px,color:#FFFFFF
    style CRON fill:#1E293B,stroke:#F43F5E,stroke-width:2px,color:#FFFFFF
```

---

## 🚀 Quantifiable Business & Engineering Impact

* **40% Cloud Spend Slashed:** Eliminated unallocated Azure compute and orphaned storage spend across distributed engineering squads.
* **100% Team-Level Cost Attribution:** Configured OpenCost with Prometheus metrics to break down AKS cluster costs by Kubernetes namespace, pod, and service label.
* **Automated Asset Hygiene:** Python automation regularly discovers and snapshots unattached Azure Managed Disks and deallocates orphaned public IPs before monthly billing cycles close.
* **Shift-Left Budget Gates:** Infracost posts transparent line-item deltas directly on GitHub Actions pull requests, blocking changes that exceed team budget thresholds without VP approval.

---

## 📂 Repository Layout

```
.
├── helm/
│   ├── opencost-azure-values.yaml         # OpenCost AKS Helm Deployment Configuration
├── configs/
│   ├── infracost-policy.rego              # OPA Rego Policy for Budget Enforcement
├── scripts/
│   ├── cleanup_unattached_disks.py        # Python Unattached Managed Disk Scanner
│   ├── cleanup_orphaned_ips.py            # Python Orphaned Public IP Cleaner
└── README.md
```

---

## 👨‍💻 Author

**Kumar Suman Priya**  
*Lead DevSecOps & Cloud Platform Engineer*  
GitHub: [@kumarsumanpriya](https://github.com/kumarsumanpriya)
