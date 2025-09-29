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

- `Ubuntu EC2 Machine`
- `git`
- `unzip`
- `Internet access`

If unzip is not installed, use following command to install it
```bash
sudo apt-get update
```
```bash
sudo apt-get install unzip -y
```
---


## 📁 Project Structure
```
meshramAI/
├── meshram              # Main CLI script (symlinked to /usr/local/bin/meshram)
├── modules/
│   ├── ec2.sh
│   ├── vpc.sh
│   ├── s3.sh
│   └── s3/
│       ├── create.sh
│       ├── list.sh
│       └── delete.sh
├── logs/                # Auto-created by the CLI
├── regions.conf         # Region mappings (e.g., mumbai=ap-south-1)
└── README.md
```




## 📌 One-Time Setup



#### Switch to ubuntu user
```bash
sudo su ubuntu
```
#### Navigate to home directory
```bash
cd /home/ubuntu
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

#### Clone the Meshram CLI repository
```bash
git clone https://github.com/shubmeshaws/meshramAI.git
```

#### Go inside the meshramAI directory
```bash
cd meshramAI
```

#### Make the script executable
```bash
chmod +x meshram
```

#### Create Symlink for the script to /usr/local/bin for global access
```bash
sudo ln -sf "$(pwd)/meshram" /usr/local/bin/meshram
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




Contribution: 2025-09-26 06:06:00

Contribution: 2025-09-27 00:56:00

Contribution: 2025-09-27 01:03:00

Contribution: 2025-09-28 13:13:00

Contribution: 2025-09-28 06:00:00

Contribution: 2025-09-28 06:27:00

Contribution: 2025-09-28 01:31:00

Contribution: 2025-09-28 05:38:00

Contribution: 2025-09-28 11:21:00

Contribution: 2025-09-29 11:09:00

