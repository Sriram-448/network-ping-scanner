import asyncio
import platform
import ipaddress
from datetime import datetime

# Determine ping parameters based on OS
def get_ping_command(ip):
    system = platform.system().lower()
    if system == "windows":
        return ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        return ["ping", "-c", "1", "-W", "1", str(ip)]

# Async ping function
async def ping_host(ip):
    cmd = get_ping_command(ip)

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL
    )

    stdout, _ = await process.communicate()

    alive = process.returncode == 0
    return ip, alive

# Scan entire subnet concurrently
async def scan_network(cidr):
    network = ipaddress.ip_network(cidr, strict=False)
    tasks = [ping_host(ip) for ip in network.hosts()]

    results = await asyncio.gather(*tasks)
    return results

# Real-time scanner loop
async def realtime_scan(cidr, interval=3):
    while True:
        results = await scan_network(cidr)

        print("\033c", end="")  # Clear terminal
        print(f"Real-Time Network Scan: {cidr}")
        print(f"Timestamp: {datetime.now()}\n")
        print(f"{'IP Address':<18} Status")
        print("-" * 30)

        for ip, alive in results:
            status = "UP" if alive else "DOWN"
            print(f"{str(ip):<18} {status}")

        await asyncio.sleep(interval)

# Entry point
if __name__ == "__main__":
    CIDR_RANGE = "192.168.1.0/24" # change to your local subnet
    asyncio.run(realtime_scan(CIDR_RANGE))
