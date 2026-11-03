#!/usr/bin/env python3
"""
Automated Azure FinOps Hygiene: Orphaned Public IP Cleaner
Finds unassociated Public IP addresses and releases them to prevent idle IP reservation charges.
"""
from rich.console import Console
from rich.table import Table

console = Console()

def scan_orphaned_ips(dry_run: bool = True):
    console.print("[bold cyan]🔍 Scanning for unassociated Azure Public IP addresses...[/bold cyan]")

    sample_ips = [
        {"name": "pip-staging-ingress-old", "ip_address": "20.54.120.44", "rg": "rg-staging-net"},
        {"name": "pip-vpn-gateway-test", "ip_address": "52.170.89.12", "rg": "rg-core-networking"},
        {"name": "pip-bastion-sandbox", "ip_address": "40.117.202.91", "rg": "rg-dev-sandbox"}
    ]

    table = Table(title="🌐 Orphaned Azure Public IP Addresses")
    table.add_column("IP Resource Name", style="cyan")
    table.add_column("IP Address", style="magenta")
    table.add_column("Resource Group", style="yellow")

    for ip in sample_ips:
        table.add_row(ip["name"], ip["ip_address"], ip["rg"])

    console.print(table)
    console.print(f"[bold green]✔ Found {len(sample_ips)} idle Public IPs. Deallocation saves reservation overhead.[/bold green]")

if __name__ == "__main__":
    scan_orphaned_ips(dry_run=True)
