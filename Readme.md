Instructions:
```
git clone https://github.com/fuomag9/GithubSSH.git /opt/
sudo chown root:root /opt/GithubSSH
sudo chmod +x /opt/GithubSSH/main.py
echo "AuthorizedKeysCommand /opt/GithubSSH/main.py" | sudo tee /etc/ssh/sshd_config.d/githubSSH.conf
echo "AuthorizedKeysCommandUser root" | sudo tee -a /etc/ssh/sshd_config.d/githubSSH.conf
sudo systemctl restart sshd
```