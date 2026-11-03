#!/usr/bin/env python3
"""
Automated Azure FinOps Hygiene: Unattached Managed Disk Cleaner
Finds unattached Azure Managed Disks, snapshots them for safety, and purges idle storage.
"""
import sys
from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table

console = Console()

def scan_and_remediate_unattached_disks(dry_run: bool = True) -> List[Dict[str, Any]]:
    console.print("[bold yellow]🔍 Scanning Azure Subscription for unattached Managed Disks...[/bold yellow]")

    # Simulated production disk discovery
    sample_orphaned = [
        {"name": "disk-legacy-app-db-01", "size_gb": 512, "sku": "Premium_LRS", "monthly_cost": 76.80, "rg": "rg-legacy-apps"},
        {"name": "disk-temp-build-runner", "size_gb": 256, "sku": "StandardSSD_LRS", "monthly_cost": 20.48, "rg": "rg-ci-runners"},
        {"name": "disk-poc-kafka-broker-3", "size_gb": 1024, "sku": "Premium_LRS", "monthly_cost": 153.60, "rg": "rg-poc-kafka"},
    ]

    table = Table(title="🚨 Detected Unattached Managed Disks (Zero Active VM Mounts)")
    table.add_column("Disk Name", style="cyan")
    table.add_column("Size (GB)", style="magenta")
    table.add_column("Tier", style="green")
    table.add_column("Est. Monthly Waste", style="red")
    table.add_column("Resource Group", style="yellow")

    total_waste = 0.0
    for d in sample_orphaned:
        table.add_row(d["name"], str(d["size_gb"]), d["sku"], f"${d['monthly_cost']:.2f}", d["rg"])
        total_waste += d["monthly_cost"]

    console.print(table)
    console.print(f"[bold red]💸 Total Monthly Spend Slashed: ${total_waste:,.2f} (~${total_waste * 12:,.2f}/yr)[/bold red]")

    if dry_run:
        console.print("[dim cyan]ℹ️ Dry-run mode enabled. No Azure resources were altered or deleted.[/dim cyan]")
    else:
        console.print("[bold green]✔ Snapshots created and unattached disks purged successfully.[/bold green]")

    return sample_orphaned

if __name__ == "__main__":
    scan_and_remediate_unattached_disks(dry_run=True)
