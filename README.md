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

Contribution: 2025-09-29 19:40:00

Contribution: 2025-09-29 16:03:00

Contribution: 2025-09-29 01:59:00

Contribution: 2025-09-29 10:50:00

Contribution: 2025-09-29 13:42:00

Contribution: 2025-09-30 21:57:00

Contribution: 2025-09-30 03:14:00

Contribution: 2025-09-30 14:18:00

Contribution: 2025-09-30 15:08:00

Contribution: 2025-09-30 17:21:00

Contribution: 2025-09-30 19:09:00

Contribution: 2025-09-30 04:55:00

Contribution: 2025-09-30 14:31:00

Contribution: 2025-10-01 00:35:00

Contribution: 2025-10-01 18:17:00

Contribution: 2025-10-01 04:43:00

Contribution: 2025-10-01 08:55:00

Contribution: 2025-10-01 00:16:00

Contribution: 2025-10-01 06:09:00

Contribution: 2025-10-01 13:34:00

Contribution: 2025-10-02 22:07:00

Contribution: 2025-10-02 18:40:00

Contribution: 2025-10-02 03:35:00

Contribution: 2025-10-02 10:06:00

Contribution: 2025-10-02 10:09:00

Contribution: 2025-10-03 10:30:00

Contribution: 2025-10-03 10:43:00

Contribution: 2025-10-03 08:09:00

Contribution: 2025-10-03 08:22:00

Contribution: 2025-10-03 22:34:00

Contribution: 2025-10-03 01:52:00

Contribution: 2025-10-03 06:47:00

Contribution: 2025-10-03 19:08:00

Contribution: 2025-10-03 18:40:00

Contribution: 2025-10-03 11:25:00

Contribution: 2025-10-04 16:19:00

Contribution: 2025-10-04 16:19:00

Contribution: 2025-10-04 00:04:00

Contribution: 2025-10-05 21:50:00

Contribution: 2025-10-05 14:01:00

Contribution: 2025-10-05 13:08:00

Contribution: 2025-10-06 05:28:00

Contribution: 2025-10-06 05:03:00

Contribution: 2025-10-06 03:00:00

Contribution: 2025-10-07 21:49:00

Contribution: 2025-10-07 11:59:00

Contribution: 2025-10-07 13:52:00

Contribution: 2025-10-07 19:08:00

Contribution: 2025-10-07 01:26:00

Contribution: 2025-10-07 08:03:00

Contribution: 2025-10-07 12:57:00

Contribution: 2025-10-07 00:21:00

Contribution: 2025-10-07 07:00:00

Contribution: 2025-10-08 05:27:00

Contribution: 2025-10-08 02:31:00

Contribution: 2025-10-08 08:28:00

Contribution: 2025-10-08 11:54:00

Contribution: 2025-10-08 23:57:00

Contribution: 2025-10-08 23:55:00

Contribution: 2025-10-09 08:54:00

Contribution: 2025-10-09 07:53:00

Contribution: 2025-10-09 12:55:00

Contribution: 2025-10-09 05:27:00

