# 🤖 meshramAI

**meshramAI** is a powerful CLI tool designed to help you create cloud infrastructure easily — even if you have no prior knowledge of AWS or DevOps. It simplifies cloud setup through an intuitive and scriptable command-line interface.

---

# 🚀 Meshram CLI

Meshram is a lightweight and easy-to-use CLI tool to simplify your project management and infrastructure provisioning tasks on Ubuntu-based systems.

---

## 📥 Installation

Follow the steps below to install and configure the **Meshram CLI** on your Ubuntu system.

---

### 🔧 Prerequisites

Ensure the following tools are installed:

- Ubuntu OS
- `git`
- `unzip`
- Internet access

---

## 📌 One-Time Setup



#### Switch to ubuntu user
```bash
sudo su ubuntu
```
#### Navigate to home directory
```bash
cd /home/ubuntu
```

#### Clone the Meshram CLI repository
```bash
git clone https://github.com/shubmeshaws/meshramAI.git
```

#### Download AWS CLI v2
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

#### Unzip the AWS CLI package
```bash
unzip awscliv2.zip
```

#### Install AWS CLI
```bash
sudo ./aws/install
```

#### Rename the CLI script
```bash
mv cli.sh meshram
```

#### Make the script executable
```bash
chmod +x meshram
```

#### Move the script to /usr/local/bin for global access
```bash
sudo mv meshram /usr/local/bin/
```

#### Test the CLI tool
```bash
meshram help
```
<br>
<br>
<br>
<br>
<br>



## 🤝 Contributing

1. Fork this repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes
4. Open a pull request
<br>

## 🙋‍♂️ Support
Reach out to me at [shubmeshaws@gmail.com]

## 📄 License
This project is licensed under the MIT License.




