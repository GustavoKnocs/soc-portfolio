import re


def extract_ips(log_file_path):

    ipv4_pattern = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')
    ipv6_pattern = re.compile(r'^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$|^([0-9A-Fa-f]{1,4}:){0,6}([0-9A-Fa-f]{1,4}:)?([0-9A-Fa-f]{1,4}:){1,7}[0-9A-Fa-f]{1,4}$')

    extracted_ips = set()

    try:
        with open(log_file_path, 'r') as file:
            content = file.read()
            
            ipv4_matches = ipv4_pattern.findall(content)
            ipv6_matches = ipv6_pattern.findall(content)
            
            extracted_ips.update(ipv4_matches)
            extracted_ips.update(ipv6_matches)

    except FileNotFoundError:
        print(f"Arquivo {log_file_path} não encontrado.")

    return list(extracted_ips)

if __name__ == "__main__":
    ips = extract_ips('exemplo_ssh.log')
    print(f"IPs: {ips}")