#!/usr/bin/env python3

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import time
import json

def scan_ports_with_post(domain, start_port, end_port, url):
    results = []
    for port in range(start_port, end_port + 1):
        data = MultipartEncoder(
            fields={
                'bookurl': f'http://{domain}:{port}',
                'bookfile': ('', '', 'application/octet-stream')
            }
        )
        headers = {'Content-Type': data.content_type}

        try:
            start_time = time.time()
            response = requests.post(url, data=data, headers=headers, timeout=5)
            response_time = time.time() - start_time
            content_length = len(response.content)

            results.append({
                'port': port,
                'status_code': response.status_code,
                'content_length': content_length,
                'response_time': response_time,
                'sample_of_response': response.text[:200]  # Ajusta según lo necesario para obtener una buena muestra
            })

        except requests.exceptions.RequestException as e:
            results.append({
                'port': port,
                'error': str(e)
            })

    # Guardar los resultados en un archivo JSON
    with open('scan_results.json', 'w') as f:
        json.dump(results, f, indent=4)

    return results

# Configuración de dominio y rango de puertos
domain = '127.0.0.1'
start_port = int(input("Enter initial port: "))
end_port = int(input("Enter end port: "))
url = input("Enter the URL: ")

print("[+] Exploring ports...")
results = scan_ports_with_post(domain, start_port, end_port, url)
print("Scan completed. Results saved to 'scan_results.json'.")
