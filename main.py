# -*- coding: utf-8 -*-

import sys,os
import psutil

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import webbrowser


class PerformanceMonitor(FlowLauncher):

    def query(self, query):
        # RAM
        ram_usage = psutil.virtual_memory()

        # CPU 
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Disk
        partition_disk_size = []
        partition_disk_usage = []
        for disk in psutil.disk_partitions():
            if disk.fstype and disk.opts != 'removable':
                partition_disk_size.append(psutil.disk_usage(disk.mountpoint).total)
                partition_disk_usage.append(psutil.disk_usage(disk.mountpoint).used)
        disk_usage = round(sum(partition_disk_usage)/sum(partition_disk_size), 2)
        
        return [
            {
                "Title": f"RAM: {ram_usage.percent}% | CPU: {cpu_usage}% | Disk: {disk_usage*100}%",
                "SubTitle": "(No update in real-time)",
                "IcoPath": "Images/app.png"
            }
        ]

    def context_menu(self, data):
        return [
            {
                "Title": "Performance Monitor's Repository",
                "SubTitle": "Press enter to open the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/x200706/Flow.Launcher.Plugin.PerformanceMonitor"]
                }
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    PerformanceMonitor()
